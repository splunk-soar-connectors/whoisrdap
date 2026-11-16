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

from os import environ
from urllib.request import ProxyHandler, build_opener

from ipwhois import IPDefinedError, IPWhois
from soar_sdk.exceptions import ActionFailure
from soar_sdk.logging import getLogger

logger = getLogger()

WHOIS_ERROR_QUERY = "Whois query failed. Error: {}"


def lookup_rdap(ip: str) -> dict:
    proxy = {}
    if environ.get("HTTP_PROXY"):
        proxy["http"] = environ["HTTP_PROXY"]
    if environ.get("HTTPS_PROXY"):
        proxy["https"] = environ["HTTPS_PROXY"]

    try:
        if proxy:
            logger.debug("Found proxy env. Using proxy for connection.")
            obj_whois = IPWhois(ip, proxy_opener=build_opener(ProxyHandler(proxy)))
        else:
            obj_whois = IPWhois(ip)
        return obj_whois.lookup_rdap(inc_nir=False)
    except IPDefinedError as e:
        logger.error(f"Got IPDefinedError: {e}")
        raise ActionFailure(str(e)) from e
    except Exception as e:
        logger.error(f"Got exception object: {e}")
        raise ActionFailure(WHOIS_ERROR_QUERY.format(e)) from e
