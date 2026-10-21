"""Adds the Maven Central publishing plugin to the generated java/pom.xml.

Maven cannot deploy without a destination, and the Java generator has no option that produces one:
`config-help -g java` offers groupId, artifactId, scm and developer fields, and nothing about
publishing. So `mvn deploy` on the generated pom fails with "repository element was not specified
in the POM inside distributionManagement element".

Central's own plugin is what supplies that destination. It installs as a build extension and takes
over the deploy phase, which is also why the default maven-deploy-plugin needs no skip: it never
runs. The credentials come from the `central` server id that setup-java writes into settings.xml
during the release workflow.

Everything else about the pom — coordinates, metadata, the GPG profile Central requires — is
already generated from sdks.json, so this injects one plugin and touches nothing else. It runs
inside generate.sh for the same reason the PHP root manifest and the Go module path do: an edit
made by hand is an edit the next regeneration throws away.
"""

import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent

manifest = json.loads((ROOT / "sdks.json").read_text(encoding="utf-8"))
version = manifest["centralPublishingPluginVersion"]

pom_path = ROOT / "java" / "pom.xml"
pom = pom_path.read_text(encoding="utf-8")

MARKER = "<artifactId>central-publishing-maven-plugin</artifactId>"
if MARKER in pom:
    print(f"  pom.xml: central-publishing-maven-plugin {version} already present")
    raise SystemExit(0)

# autoPublish releases the deployment instead of parking it behind a button in the Portal: the tag
# is the decision, and a release that needs a human afterwards is a release that half happened.
# waitUntil=validated fails the job on anything Central rejects — a bad signature, missing
# javadoc — without holding a runner open for the propagation that follows.
PLUGIN = f"""            <plugin>
                <groupId>org.sonatype.central</groupId>
                <artifactId>central-publishing-maven-plugin</artifactId>
                <version>{version}</version>
                <extensions>true</extensions>
                <configuration>
                    <publishingServerId>central</publishingServerId>
                    <autoPublish>true</autoPublish>
                    <waitUntil>validated</waitUntil>
                </configuration>
            </plugin>
"""

# The first <build><plugins> is the project's own; the later one belongs to the sign-artifacts
# profile, and the plugin must not be confined to a profile that only the release run activates.
ANCHOR = "    <build>\n        <plugins>\n"
if pom.count(ANCHOR) != 1:
    raise SystemExit(f"expected exactly one project <build><plugins> in {pom_path}")

pom_path.write_text(pom.replace(ANCHOR, ANCHOR + PLUGIN, 1), encoding="utf-8")
print(f"  pom.xml: central-publishing-maven-plugin {version}")
