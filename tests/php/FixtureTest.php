<?php

declare(strict_types=1);

namespace Growwer\Api\Fixtures;

use Growwer\Api\Api\AccountApi;
use Growwer\Api\Api\BuyerOrdersApi;
use Growwer\Api\Api\CatalogueApi;
use Growwer\Api\Api\SellerMediasApi;
use Growwer\Api\Api\WebhooksApi;
use Growwer\Api\ApiException;
use Growwer\Api\Configuration;
use Growwer\Api\Model\CatalogueMedia;
use Growwer\Api\Model\CatalogueMediaBestPrice;
use Growwer\Api\Model\CatalogueOfferOrNull;
use Growwer\Api\Model\CreateWebhookRequest;
use Growwer\Api\Model\Error;
use Growwer\Api\Model\GetMe200Response;
use Growwer\Api\Model\ListOrders200Response;
use Growwer\Api\Model\Money;
use Growwer\Api\Model\MoneyOrNull;
use Growwer\Api\Model\Order;
use Growwer\Api\Model\ProjectCatalogueMedia;
use Growwer\Api\Model\SellerFeesOrNull;
use Growwer\Api\Model\SellerMedia;
use Growwer\Api\Model\SellerMediaCompetitiveFeesByLinkTypeInner;
use Growwer\Api\Model\SellerMediaSaved;
use Growwer\Api\Model\SellerMediaSavedAllOfWarnings;
use Growwer\Api\Model\UpdateSellerMediaRequest;
use Growwer\Api\Model\UpdateWebhookRequest;
use Growwer\Api\Model\WebhookEvent;
use Growwer\Api\Model\WebhookEventData;
use Growwer\Api\Model\WebhookEventType;
use Growwer\Api\Model\WebhookWithSecret;
use Growwer\Api\ObjectSerializer;
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
    private const WEBHOOK_ID = '9d4c3f5b-6e7a-4b82-9d2e-3f4a5b6c7d8e';
    private const PROJECT_ID = '5e0c2b7a-3d4f-4a1b-9c8d-7e6f5a4b3c2d';

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

    private static function event(string $name): WebhookEvent
    {
        $event = ObjectSerializer::deserialize(json_decode(self::fixture($name)), WebhookEvent::class);
        self::assertInstanceOf(WebhookEvent::class, $event);
        self::assertInstanceOf(WebhookEventData::class, $event->getData());

        return $event;
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
        self::assertSame(5000, $me->getCatalogue()->getDailyCap());
        self::assertNull($me->getCatalogue()->getRemainingToday());
        self::assertSame('live', $me->getMode());
    }

    public function testGetMeWithATestKeyReadsTestModeAndNoSeller(): void
    {
        $me = (new AccountApi(...$this->answer(200, self::fixture('me-test-key.json'))))->getMe();

        self::assertInstanceOf(GetMe200Response::class, $me);
        self::assertSame('test', $me->getMode());
        self::assertNull($me->getSeller());
        self::assertSame(100000, $me->getBuyer()->getBalance()->getAvailable()->getAmount());
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
        $page = (new BuyerOrdersApi(...$this->answer(200, self::fixture('orders-page.json'))))->listOrders(limit: 2);

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
        $order = (new BuyerOrdersApi(...$this->answer(200, self::fixture('order-with-unknown-field.json'))))
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
        $order = (new BuyerOrdersApi(...$this->answer(200, self::fixture('link-addition-order-with-unknown-field.json'))))
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
        self::assertNull($media->getBestPrice());
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

    public function testACatalogueMediaReadsItsBestPriceBadge(): void
    {
        $media = (new CatalogueApi(...$this->answer(200, self::fixture('catalogue-media-null-link-type.json'))))
            ->getCatalogueMedia(self::MEDIA_ID);

        $bestPrice = $media->getBestPrice();
        self::assertInstanceOf(CatalogueMediaBestPrice::class, $bestPrice);
        self::assertSame([], $bestPrice->listInvalidProperties());
        self::assertSame(CatalogueMediaBestPrice::BADGE_CHEAPER, $bestPrice->getBadge());
        self::assertSame(3, $bestPrice->getPlatformCount());
        self::assertSame('2026-11-12', $bestPrice->getCheckedOn()->format('Y-m-d'));
    }

    public function testAProjectMediaReadsAnOnlyHereBadge(): void
    {
        $page = (new CatalogueApi(...$this->answer(200, self::fixture('project-medias-page.json'))))
            ->searchProjectMedias(self::PROJECT_ID, best_price: true);

        self::assertSame('/api/v1/projects/' . self::PROJECT_ID . '/medias', $this->sent()->getUri()->getPath());
        self::assertContains('bestPrice=true', explode('&', $this->sent()->getUri()->getQuery()));
        $media = $page->getItems()[0];
        self::assertInstanceOf(ProjectCatalogueMedia::class, $media);
        self::assertSame([], $media->listInvalidProperties());
        $bestPrice = $media->getBestPrice();
        self::assertInstanceOf(CatalogueMediaBestPrice::class, $bestPrice);
        self::assertSame(CatalogueMediaBestPrice::BADGE_ONLY_HERE, $bestPrice->getBadge());
        self::assertSame(2, $bestPrice->getPlatformCount());
        self::assertSame('2026-11-11', $bestPrice->getCheckedOn()->format('Y-m-d'));
    }

    public function testListFlashOffersSendsBooleanFiltersAsTrueAndFalse(): void
    {
        $page = (new CatalogueApi(...$this->answer(200, self::fixture('project-medias-page.json'))))
            ->listFlashOffers(self::PROJECT_ID, best_price: true, favourite: false);

        self::assertSame('/api/v1/flash-offers', $this->sent()->getUri()->getPath());
        $query = explode('&', $this->sent()->getUri()->getQuery());
        self::assertContains('bestPrice=true', $query);
        self::assertContains('favourite=false', $query);
        self::assertCount(1, $page->getItems());
    }

    public function testTheDefaultConfigurationStillSendsBooleanFiltersAsIntegersWhenAskedTo(): void
    {
        $default = Configuration::getDefaultConfiguration();
        $previous = $default->getBooleanFormatForQueryString();
        $default->setBooleanFormatForQueryString(Configuration::BOOLEAN_FORMAT_INT);
        try {
            (new CatalogueApi(...$this->answer(200, self::fixture('project-medias-page.json'))))
                ->listFlashOffers(self::PROJECT_ID, best_price: true, favourite: false);
        } finally {
            $default->setBooleanFormatForQueryString($previous);
        }

        $query = explode('&', $this->sent()->getUri()->getQuery());
        self::assertContains('bestPrice=1', $query);
        self::assertContains('favourite=0', $query);
    }

    public function testAProjectMediaWithoutABadgeReadsANullBestPrice(): void
    {
        $page = (new CatalogueApi(...$this->answer(200, self::fixture('project-medias-page-no-badge.json'))))
            ->searchProjectMedias(self::PROJECT_ID);

        $media = $page->getItems()[0];
        self::assertInstanceOf(ProjectCatalogueMedia::class, $media);
        self::assertNull($media->getBestPrice());
        self::assertSame([], $media->listInvalidProperties());
        self::assertSame('blog.example', $media->getDomain());
    }

    public function testASellerMediaReadsNullCompetitiveFees(): void
    {
        $media = (new SellerMediasApi(...$this->answer(200, self::fixture('seller-media.json'))))
            ->getSellerMedia(self::MEDIA_ID);

        self::assertInstanceOf(SellerMedia::class, $media);
        self::assertNull($media->getCompetitiveFees());
        self::assertNull($media->getCompetitiveFeesByLinkType());
        self::assertSame([], $media->listInvalidProperties());
        self::assertNull($media->getLinkAdditionOffer());
        $option = $media->getPostOffer()->getPricingOptions()[0];
        self::assertSame(6000, $option->getFeeWhenSellerWritesPost()->getAmount());
        self::assertNull($option->getFeeWhenSellerDoesNotWritePost());
        self::assertNull($option->getCurrentCost());
        self::assertSame(1500, $media->getPostOffer()->getExtraServices()[0]->getCost()->getAmount());
        self::assertSame('15.00', $media->getPostOffer()->getExtraServices()[0]->getCost()->getAmountDecimal());
    }

    public function testASellerMediaReadsCompetitiveFeesWithOneSideNull(): void
    {
        $media = (new SellerMediasApi(...$this->answer(200, self::fixture('seller-media-competitive-fees.json'))))
            ->getSellerMedia(self::MEDIA_ID);

        self::assertSame([], $media->listInvalidProperties());
        $fees = $media->getCompetitiveFees();
        self::assertInstanceOf(SellerFeesOrNull::class, $fees);
        self::assertSame(5400, $fees->getFeeWhenSellerWritesPost()->getAmount());
        self::assertNull($fees->getFeeWhenSellerDoesNotWritePost());
    }

    public function testASellerMediaReadsCompetitiveFeesByLinkTypePerLinkType(): void
    {
        $media = (new SellerMediasApi(...$this->answer(200, self::fixture('seller-media-competitive-fees-by-link-type.json'))))
            ->getSellerMedia(self::MEDIA_ID);

        self::assertSame([], $media->listInvalidProperties());
        $fees = $media->getCompetitiveFeesByLinkType();
        self::assertCount(2, $fees);
        self::assertContainsOnlyInstancesOf(SellerMediaCompetitiveFeesByLinkTypeInner::class, $fees);
        self::assertSame('dofollow', $fees[0]->getLinkType());
        self::assertInstanceOf(MoneyOrNull::class, $fees[0]->getFeeWhenSellerWritesPost());
        self::assertSame(5400, $fees[0]->getFeeWhenSellerWritesPost()->getAmount());
        self::assertSame('54.00', $fees[0]->getFeeWhenSellerWritesPost()->getAmountDecimal());
        self::assertNull($fees[0]->getFeeWhenSellerDoesNotWritePost());
        self::assertSame('nofollow', $fees[1]->getLinkType());
        self::assertNull($fees[1]->getFeeWhenSellerWritesPost());
        self::assertSame(3600, $fees[1]->getFeeWhenSellerDoesNotWritePost()->getAmount());
        self::assertSame('36.00', $fees[1]->getFeeWhenSellerDoesNotWritePost()->getAmountDecimal());
        self::assertSame(5400, $media->getCompetitiveFees()->getFeeWhenSellerWritesPost()->getAmount());
        self::assertSame(3600, $media->getCompetitiveFees()->getFeeWhenSellerDoesNotWritePost()->getAmount());
    }

    public function testASellerMediaSaveReadsASavedNotRecommendedWarning(): void
    {
        $saved = (new SellerMediasApi(...$this->answer(200, self::fixture('seller-media-saved-not-recommended.json'))))
            ->updateSellerMedia(self::MEDIA_ID, 'key-1', new UpdateSellerMediaRequest());

        self::assertInstanceOf(SellerMediaSaved::class, $saved);
        self::assertSame([], $saved->listInvalidProperties());
        $warnings = $saved->getWarnings();
        self::assertCount(1, $warnings);
        self::assertInstanceOf(SellerMediaSavedAllOfWarnings::class, $warnings[0]);
        self::assertSame(SellerMediaSavedAllOfWarnings::CODE_SAVED_NOT_RECOMMENDED, $warnings[0]->getCode());
        $fees = $warnings[0]->getDetails()->getCompetitiveFees();
        self::assertSame(5400, $fees->getFeeWhenSellerWritesPost()->getAmount());
        self::assertNull($fees->getFeeWhenSellerDoesNotWritePost());
        self::assertSame(['Prensalink'], $warnings[0]->getDetails()->getCompetitors());
        self::assertSame('blog.example', $saved->getDomain());
    }

    public function testAnOrderEventParsesWithFieldsThisClientDoesNotKnow(): void
    {
        $event = self::event('webhook-order-created.json');

        self::assertSame('6a1f0c2e-3b4d-4e5f-8a9b-0c1d2e3f4a5b', $event->getId());
        self::assertSame('order.created', $event->getType());
        self::assertSame('live', $event->getMode());
        self::assertSame('v1', $event->getApiVersion());
        self::assertEquals(new \DateTime('2026-10-01T09:30:05+00:00'), $event->getCreatedAt());
        // The oneOf is one merged model: the order member's field is set and the others' are not.
        $data = $event->getData();
        self::assertInstanceOf(Order::class, $data->getOrder());
        self::assertNull($data->getWallet());
        self::assertNull($data->getThreshold());
        self::assertNull($data->getWebhookId());
        self::assertSame(self::ORDER_ID, $data->getOrder()->getId());
        self::assertSame('pending_acceptance', $data->getOrder()->getState());
        self::assertSame(12500, $data->getOrder()->getPrice()->getAmount());
        self::assertSame('Choosing running shoes', $data->getOrder()->getBriefing()->getTitle());
    }

    public function testABalanceLowEventParsesWithFieldsThisClientDoesNotKnow(): void
    {
        $event = self::event('webhook-balance-low.json');

        self::assertSame('balance.low', $event->getType());
        self::assertSame('live', $event->getMode());
        $data = $event->getData();
        self::assertNull($data->getOrder());
        self::assertNull($data->getWebhookId());
        self::assertSame(4500, $data->getWallet()->getAvailableBalance()->getAmount());
        self::assertSame('EUR', $data->getWallet()->getCurrency());
        self::assertSame(5000, $data->getThreshold()->getAmount());
    }

    public function testAWebhookTestEventParsesWithFieldsThisClientDoesNotKnow(): void
    {
        $event = self::event('webhook-test.json');

        self::assertSame('webhook.test', $event->getType());
        self::assertSame('live', $event->getMode());
        $data = $event->getData();
        self::assertNull($data->getOrder());
        self::assertNull($data->getWallet());
        self::assertNull($data->getThreshold());
        self::assertSame(self::WEBHOOK_ID, $data->getWebhookId());
    }

    public function testCreateWebhookSendsTheBodyAndKeyAndReadsTheSecret(): void
    {
        $events = [WebhookEventType::ORDER_CREATED, WebhookEventType::ORDER_COMPLETED, WebhookEventType::BALANCE_LOW];
        $webhook = (new WebhooksApi(...$this->answer(201, self::fixture('webhook-with-secret.json'))))->createWebhook(
            'create-webhook-1',
            new CreateWebhookRequest([
                'url' => 'https://hooks.shop.example/growwer',
                'events' => $events,
                'low_balance_threshold' => new Money(['amount' => 5000, 'currency' => 'EUR']),
            ]),
        );

        self::assertSame('POST', $this->sent()->getMethod());
        self::assertSame('https://tool.growwer.com/api/v1/webhooks', (string) $this->sent()->getUri());
        self::assertSame('create-webhook-1', $this->sent()->getHeaderLine('Idempotency-Key'));
        self::assertSame(
            [
                'url' => 'https://hooks.shop.example/growwer',
                'events' => ['order.created', 'order.completed', 'balance.low'],
                'lowBalanceThreshold' => ['amount' => 5000, 'currency' => 'EUR'],
            ],
            json_decode((string) $this->sent()->getBody(), true),
        );
        self::assertInstanceOf(WebhookWithSecret::class, $webhook);
        self::assertSame(self::WEBHOOK_ID, $webhook->getId());
        self::assertStringStartsWith('whsec_', (string) $webhook->getSecret());
        self::assertSame($events, $webhook->getEvents());
        self::assertSame(5000, $webhook->getLowBalanceThreshold()->getAmount());
        self::assertTrue($webhook->getEnabled());
        self::assertNull($webhook->getDisabledReason());
        self::assertNull($webhook->getFailingSince());
    }

    public function testUpdateWebhookSendsTheAmountDecimalOfAMoneyItRead(): void
    {
        $read = (new WebhooksApi(...$this->answer(200, self::fixture('webhook-with-secret.json'))))
            ->rotateWebhookSecret(self::WEBHOOK_ID, 'rotate-webhook-1');
        $threshold = $read->getLowBalanceThreshold();
        self::assertSame('50.00', $threshold->getAmountDecimal());

        (new WebhooksApi(...$this->answer(200, self::fixture('webhook-with-secret.json'))))->updateWebhook(
            self::WEBHOOK_ID,
            'update-webhook-1',
            new UpdateWebhookRequest(['low_balance_threshold' => $threshold]),
        );

        self::assertSame('PATCH', $this->sent()->getMethod());
        self::assertSame('https://tool.growwer.com/api/v1/webhooks/' . self::WEBHOOK_ID, (string) $this->sent()->getUri());
        self::assertSame(
            ['lowBalanceThreshold' => ['amount' => 5000, 'currency' => 'EUR', 'amountDecimal' => '50.00']],
            json_decode((string) $this->sent()->getBody(), true),
        );
    }

    public function testTheErrorEnvelopeIsReadableFromTheException(): void
    {
        $api = new CatalogueApi(...$this->answer(429, self::fixture('error.json'), [
            'Content-Type' => 'application/json',
            'Retry-After' => '3600',
            'X-Request-Id' => '0b8f6c2e-4a1d-4f3b-9c7e-5d2a8e1f6b34',
        ]));

        try {
            $api->getCatalogueMedia(self::MEDIA_ID);
            self::fail('a 429 must throw');
        } catch (ApiException $exception) {
            self::assertSame(429, $exception->getCode());
            self::assertSame(['3600'], $exception->getResponseHeaders()['Retry-After']);
            self::assertSame(['0b8f6c2e-4a1d-4f3b-9c7e-5d2a8e1f6b34'], $exception->getResponseHeaders()['X-Request-Id']);
            $error = $exception->getResponseObject();
            self::assertInstanceOf(Error::class, $error);
            self::assertSame('catalogue_daily_cap_reached', $error->getCode());
            self::assertSame('0b8f6c2e-4a1d-4f3b-9c7e-5d2a8e1f6b34', $error->getRequestId());
            self::assertEquals(['remaining' => 0], (array) $error->getDetails());
        }
    }

    public function testABinaryDownloadReturnsTheExactBytes(): void
    {
        $body = self::fixture('briefing.bin');
        $file = (new BuyerOrdersApi(...$this->answer(200, $body, [
            'Content-Type' => 'application/octet-stream',
            'Content-Disposition' => 'attachment; filename="briefing.docx"',
        ])))->downloadOrderBriefing(self::ORDER_ID);

        self::assertStringEndsWith('/api/v1/orders/' . self::ORDER_ID . '/briefing', (string) $this->sent()->getUri());
        self::assertInstanceOf(\SplFileObject::class, $file);
        self::assertSame($body, (string) file_get_contents($file->getPathname()));
    }
}
