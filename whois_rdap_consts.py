# File: whois_rdap_consts.py
#
# Copyright (c) 2016-2021 Splunk Inc.
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
#
#
# Json keys
WHOIS_ERR_QUERY = "Whois query failed"
WHOIS_SUCC_QUERY = "Whois query successful"
WHOIS_SUCC_CONNECTIVITY_TEST = "Connectivity test passed"
WHOIS_ERR_CONNECTIVITY_TEST = "Connectivity test failed"
WHOIS_ERR_QUERY_RETURNED_NO_DATA = "Whois query did not return any information"
WHOIS_ERR_PARSE_REPLY = "Unable to parse whois response"
WHOIS_ERR_PARSE_INPUT = "Unable to parse input data"
WHOIS_ERR_INVALID_DOMAIN = "Input does not seem to be a valid domain"

WHOIS_JSON_ASN_REGISTRY = "registry"
WHOIS_JSON_ASN = "asn"
WHOIS_JSON_COUNTRY_CODE = "country_code"
WHOIS_JSON_NETS = "network"
WHOIS_JSON_SUBDOMAINS = "subdomains"
WHOIS_JSON_CACHE_UPDATE_TIME = "cache_update_time"
WHOIS_JSON_CACHE_EXP_DAYS = "update_days"
