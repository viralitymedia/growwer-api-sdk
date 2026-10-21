<?php

declare(strict_types=1);

namespace Growwer\Api\Fixtures;

use Growwer\Api\Api\AccountApi;
use Growwer\Api\Api\CatalogueApi;
use Growwer\Api\Api\OrdersApi;
use Growwer\Api\Api\SellerMediasApi;
use Growwer\Api\ApiException;
use Growwer\Api\Configuration;
use Growwer\Api\Model\CatalogueMedia;
use Growwer\Api\Model\CatalogueOfferOrNull;
use Growwer\Api\Model\Error;
use Growwer\Api\Model\GetMe200Response;
use Growwer\Api\Model\ListOrders200Response;
use Growwer\Api\Model\MoneyOrNull;
use Growwer\Api\Model\Order;
use Growwer\Api\Model\SellerFeesOrNull;
use Growwer\Api\Model\SellerMedia;
use GuzzleHttp\Client;
use GuzzleHttp\Handler\MockHandler;
use GuzzleHttp\HandlerStack;
use GuzzleHttp\Middleware;
use GuzzleHttp\Psr7\Response;
use PHPUnit\Framework\TestCase;
use Psr\Http\Message\RequestInterface;

/**
 * Deserialises the shared response fixtures through the generated PHP client, offline.
 *
 * Each call is answered from tests/fixtures/ by Guzzle's MockHandler, so the whole client path
 * runs: URL, headers, status handling and the models.
 */
final class FixtureTest extends TestCase
{
    private const MEDIA_ID = 'c1d2e3f4-a5b6-4c7d-8e9f-a0b1c2d3e4f5';
    private const ORDER_ID = '0b9c6a4e-6f1d-4c39-9a51-2f5d7c1e8a01';

    /** @var list<array{request: RequestInterface}> */
    private array $history = [];

    private static function fixture(string $name): string
    {
        return (string) file_get_contents(__DIR__ . '/../fixtures/' . $name);
    }

    /**
     * @param array<string, string> $headers
     * @return array{Client, Configuration}
     */
    private function answer(int $status, string $body, array $headers = ['Content-Type' => 'application/json']): array
    {
        $this->history = [];
        $stack = HandlerStack::create(new MockHandler([new Response($status, $headers, $body)]));
        $stack->push(Middleware::history($this->history));

        return [new Client(['handler' => $stack]), (new Configuration())->setAccessToken('test-key')];
    }

    private function sent(): RequestInterface
    {
        self::assertCount(1, $this->history);

        return $this->history[0]['request'];
    }

    public function testGetMeCallsProductionWithTheBearerKey(): void
    {
        $me = (new AccountApi(...$this->answer(200, self::fixture('me.json'))))->getMe();

        self::assertSame('GET', $this->sent()->getMethod());
        self::assertSame('https://tool.growwer.com/api/v1/me', (string) $this->sent()->getUri());
        self::assertSame('Bearer test-key', $this->sent()->getHeaderLine('Authorization'));
        self::assertInstanceOf(GetMe200Response::class, $me);
        self::assertSame(250000, $me->getBuyer()->getBalance()->getAvailable()->getAmount());
        self::assertSame('EUR', $me->getBuyer()->getBalance()->getAvailable()->getCurrency());
        self::assertNull($me->getSeller()->getHolidayEndDate());
        self::assertTrue($me->getCatalogue()->getEligible());
    }

    public function testTheBaseUrlIsOverridable(): void
    {
        [$client, $config] = $this->answer(200, self::fixture('me.json'));
        (new AccountApi($client, $config->setHost('https://sandbox.example')))->getMe();

        self::assertSame('https://sandbox.example/api/v1/me', (string) $this->sent()->getUri());
    }

    public function testListOrdersReadsItemsAndTotalWithBothOrderTypes(): void
    {
        $page = (new OrdersApi(...$this->answer(200, self::fixture('orders-page.json'))))->listOrders(limit: 2);

        self::assertStringContainsString('limit=2', $this->sent()->getUri()->getQuery());
        self::assertInstanceOf(ListOrders200Response::class, $page);
        self::assertSame(42, $page->getTotal());
        [$post, $linkAddition] = $page->getItems();

        self::assertInstanceOf(Order::class, $post);
        self::assertSame('post', $post->getType());
        self::assertNull($post->getPendingAction());
        self::assertNull($post->getDelivery());
        self::assertNull($post->getDraft());
        self::assertNull($post->getScheduledPublicationDate());
        self::assertSame(12500, $post->getPrice()->getAmount());
        self::assertEquals(new \DateTime('2026-10-01T09:30:00+00:00'), $post->getCreatedAt());
        self::assertNull($post->getBriefing()->getTitle());
        self::assertSame('dofollow', $post->getBriefing()->getLinks()[0]->getType());
        self::assertNull($post->getStateHistory()[0]->getReason());
        self::assertSame('api', $post->getChannel()->getCreated());

        self::assertSame('link_addition', $linkAddition->getType());
        self::assertNull($linkAddition->getPendingAction());
        self::assertNull($linkAddition->getDelivery());
        self::assertNull($linkAddition->getDraft());
        self::assertNull($linkAddition->getProject()->getId());
        self::assertSame('https://blog.example/best-trails', $linkAddition->getBriefing()->getLinkingFrom());
        self::assertNull($linkAddition->getBriefing()->getLink()->getAnchor());
        self::assertSame('no_seller_response', $linkAddition->getStateHistory()[1]->getReason()->getCode());
        self::assertNull($linkAddition->getStateHistory()[1]->getReason()->getAdditionalInfo());
    }

    public function testAnOrderWithFieldsThisClientDoesNotKnowStillDeserialises(): void
    {
        $order = (new OrdersApi(...$this->answer(200, self::fixture('order-with-unknown-field.json'))))
            ->getOrder(self::ORDER_ID);

        self::assertStringEndsWith('/api/v1/orders/' . self::ORDER_ID, (string) $this->sent()->getUri());
        self::assertSame(self::ORDER_ID, $order->getId());
        self::assertSame('seller', $order->getPendingAction());
        self::assertTrue($order->getDraft()->getHasFile());
        self::assertSame('api', $order->getChannel()->getCreated());
        self::assertSame('Choosing running shoes', $order->getBriefing()->getTitle());
        self::assertSame('dofollow', $order->getBriefing()->getLinks()[0]->getType());
        self::assertNull($order->getBriefing()->getLinkingFrom());
    }

    public function testALinkAdditionOrderWithFieldsThisClientDoesNotKnowStillDeserialises(): void
    {
        $order = (new OrdersApi(...$this->answer(200, self::fixture('link-addition-order-with-unknown-field.json'))))
            ->getOrder(self::ORDER_ID);

        self::assertSame('link_addition', $order->getType());
        $briefing = $order->getBriefing();
        self::assertSame('https://blog.example/best-trails', $briefing->getLinkingFrom());
        self::assertSame('trail shoes', $briefing->getLink()->getAnchor());
        self::assertSame('nofollow', $briefing->getLink()->getType());
        self::assertNull($briefing->getLinks());
    }

    public function testACatalogueMediaReadsANullPreviousPriceAndLinkAdditionOffer(): void
    {
        $media = (new CatalogueApi(...$this->answer(200, self::fixture('catalogue-media.json'))))
            ->getCatalogueMedia(self::MEDIA_ID);

        self::assertInstanceOf(CatalogueMedia::class, $media);
        self::assertNull($media->getLinkAdditionOffer());
        self::assertNull($media->getFlashOffer());
        self::assertNull($media->getCountry());
        self::assertNull($media->getMetrics()->getReferringDomains());
        self::assertEquals(15400, $media->getMetrics()->getOrganicTraffic());
        self::assertSame(9000, $media->getPostOffer()->getPrice()->getAmount());
        self::assertNull($media->getPostOffer()->getPreviousPrice());
        self::assertSame(7000, $media->getPostOffer()->getPrices()['nofollow']->getAmount());
        self::assertNull($media->getPostOffer()->getExtras()->getHomepageListing());
        self::assertNull($media->getPostOffer()->getExtras()->getSensitiveTopic()->getExtraPrice());
    }

    public function testACatalogueMediaReadsANullLinkTypeBesidePresentOffers(): void
    {
        $media = (new CatalogueApi(...$this->answer(200, self::fixture('catalogue-media-null-link-type.json'))))
            ->getCatalogueMedia(self::MEDIA_ID);

        $postOffer = $media->getPostOffer();
        self::assertNull($postOffer->getLinkType());
        self::assertSame([], $postOffer->listInvalidProperties());
        self::assertSame([], $postOffer->getPrices());
        self::assertInstanceOf(MoneyOrNull::class, $postOffer->getPreviousPrice());
        self::assertSame(20000, $postOffer->getPreviousPrice()->getAmount());
        self::assertSame(2500, $postOffer->getExtras()->getHomepageListing()->getAmount());
        self::assertSame(3000, $postOffer->getExtras()->getSensitiveTopic()->getExtraPrice()->getAmount());
        $offer = $media->getLinkAdditionOffer();
        self::assertInstanceOf(CatalogueOfferOrNull::class, $offer);
        self::assertNull($offer->getLinkType());
        self::assertSame([], $offer->listInvalidProperties());
        self::assertSame(6000, $offer->getPrice()->getAmount());
        self::assertNull($offer->getPreviousPrice());
    }

    public function testASellerMediaReadsNullCompetitiveFees(): void
    {
        $media = (new SellerMediasApi(...$this->answer(200, self::fixture('seller-media.json'))))
            ->getSellerMedia(self::MEDIA_ID);

        self::assertInstanceOf(SellerMedia::class, $media);
        self::assertNull($media->getCompetitiveFees());
        self::assertNull($media->getLinkAdditionOffer());
        $option = $media->getPostOffer()->getPricingOptions()[0];
        self::assertSame(6000, $option->getFeeWhenSellerWritesPost()->getAmount());
        self::assertNull($option->getFeeWhenSellerDoesNotWritePost());
        self::assertNull($option->getCurrentCost());
        self::assertSame(1500, $media->getPostOffer()->getExtraServices()[0]->getCost()->getAmount());
    }

    public function testASellerMediaReadsCompetitiveFeesWithOneSideNull(): void
    {
        $media = (new SellerMediasApi(...$this->answer(200, self::fixture('seller-media-competitive-fees.json'))))
            ->getSellerMedia(self::MEDIA_ID);

        $fees = $media->getCompetitiveFees();
        self::assertInstanceOf(SellerFeesOrNull::class, $fees);
        self::assertSame(5400, $fees->getFeeWhenSellerWritesPost()->getAmount());
        self::assertNull($fees->getFeeWhenSellerDoesNotWritePost());
    }

    public function testTheErrorEnvelopeIsReadableFromTheException(): void
    {
        $api = new CatalogueApi(...$this->answer(429, self::fixture('error.json'), [
            'Content-Type' => 'application/json',
            'Retry-After' => '3600',
            'X-Request-Id' => '4f1c2a9e8b7d6c5e',
        ]));

        try {
            $api->getCatalogueMedia(self::MEDIA_ID);
            self::fail('a 429 must throw');
        } catch (ApiException $exception) {
            self::assertSame(429, $exception->getCode());
            self::assertSame(['3600'], $exception->getResponseHeaders()['Retry-After']);
            self::assertSame(['4f1c2a9e8b7d6c5e'], $exception->getResponseHeaders()['X-Request-Id']);
            $error = $exception->getResponseObject();
            self::assertInstanceOf(Error::class, $error);
            self::assertSame('catalogue_daily_cap_reached', $error->getCode());
            self::assertSame('4f1c2a9e8b7d6c5e', $error->getRequestId());
            self::assertEquals(['remaining' => 0], (array) $error->getDetails());
        }
    }

    public function testABinaryDownloadReturnsTheExactBytes(): void
    {
        $body = self::fixture('briefing.bin');
        $file = (new OrdersApi(...$this->answer(200, $body, [
            'Content-Type' => 'application/octet-stream',
            'Content-Disposition' => 'attachment; filename="briefing.docx"',
        ])))->downloadOrderBriefing(self::ORDER_ID);

        self::assertStringEndsWith('/api/v1/orders/' . self::ORDER_ID . '/briefing', (string) $this->sent()->getUri());
        self::assertInstanceOf(\SplFileObject::class, $file);
        self::assertSame($body, (string) file_get_contents($file->getPathname()));
    }
}
