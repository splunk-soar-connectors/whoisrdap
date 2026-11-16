# Copyright (c) 2016-2026 Splunk Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under
# the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
# either express or implied. See the License for the specific language governing permissions
# and limitations under the License.

from soar_sdk.abstract import SOARClient
from soar_sdk.app import App
from soar_sdk.asset import BaseAsset
from soar_sdk.exceptions import ActionFailure
from soar_sdk.logging import getLogger

from .actions import register_actions
from .helpers import lookup_rdap

logger = getLogger()

WHOIS_SUCCESS_CONNECTIVITY_TEST = "Connectivity test passed"
WHOIS_ERROR_CONNECTIVITY_TEST = "Connectivity test failed"
CONNECTIVITY_TEST_IP = "8.8.8.8"


class Asset(BaseAsset):
    pass


def create_whois_rdap_app() -> App:
    app = App(
        name="WHOIS RDAP",
        app_type="information",
        logo="logo_splunk.svg",
        logo_dark="logo_splunk_dark.svg",
        product_vendor="Generic",
        product_name="Whois RDAP",
        publisher="Splunk",
        appid="7241ecbd-4a79-4a86-99eb-b2ed8f3e7686",
        fips_compliant=True,
        encrypt_cache_state=True,
        encrypt_ingest_state=True,
        asset_cls=Asset,
    )

    @app.test_connectivity()
    def test_connectivity(soar: SOARClient, asset: Asset) -> None:
        logger.debug(f"Validating/Querying IP '{CONNECTIVITY_TEST_IP}'")
        logger.info("Querying...")
        whois_response = lookup_rdap(CONNECTIVITY_TEST_IP)

        logger.info("Parsing response")
        if whois_response.get("query") == CONNECTIVITY_TEST_IP:
            logger.debug("identity test passed")
            soar.set_message(WHOIS_SUCCESS_CONNECTIVITY_TEST)
            return

        logger.debug("identity test failed")
        raise ActionFailure(WHOIS_ERROR_CONNECTIVITY_TEST)

    return register_actions(app)


app: App = create_whois_rdap_app()


if __name__ == "__main__":
    app.cli()
