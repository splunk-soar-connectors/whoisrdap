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
from soar_sdk.action_results import ActionOutput, OutputField, PermissiveActionOutput
from soar_sdk.logging import getLogger
from soar_sdk.params import Param, Params

from ..helpers import lookup_rdap

logger = getLogger()


class WhoisIpParams(Params):
    ip: str = Param(
        description="IPv4 or IPv6 address to query",
        primary=True,
        cef_types=["ip", "ipv6"],
        column_name="IP",
    )


class EventOutput(ActionOutput):
    action: str | None
    actor: str | None
    timestamp: str | None


class EventActorOutput(ActionOutput):
    action: str | None
    timestamp: str | None


class NoticeOutput(ActionOutput):
    description: str | None
    links: list[str] | None
    title: str | None


class ContactEntryOutput(ActionOutput):
    type: str | None
    value: str | None


class ContactOutput(ActionOutput):
    address: list[ContactEntryOutput] | None
    email: list[ContactEntryOutput] | None
    kind: str | None
    name: str | None
    phone: list[ContactEntryOutput] | None
    role: str | None
    title: str | None


class NetworkOutput(ActionOutput):
    cidr: str | None = OutputField(column_name="CIDR")
    country: str | None = OutputField(column_name="Country")
    name: str | None = OutputField(column_name="Name")
    start_address: str | None = OutputField(
        cef_types=["ip", "ipv6"], column_name="Start Address"
    )
    end_address: str | None = OutputField(
        cef_types=["ip", "ipv6"], column_name="End Address"
    )
    events: list[EventOutput] | None
    handle: str | None
    ip_version: str | None
    links: list[str] | None
    notices: list[NoticeOutput] | None
    parent_handle: str | None
    raw: str | None
    remarks: list[NoticeOutput] | None
    status: list[str] | None
    type: str | None


class ObjectOutput(ActionOutput):
    contact: ContactOutput | None
    entities: list[str] | None
    events: list[EventOutput] | None
    events_actor: list[EventActorOutput] | None
    handle: str | None
    links: list[str] | None
    notices: list[NoticeOutput] | None
    raw: str | None
    remarks: list[NoticeOutput] | None
    roles: list[str] | None
    status: list[str] | None


class NirContactOutput(ActionOutput):
    email: str | None = OutputField(example_values=["test@testcorp.com"])
    fax: str | None = OutputField(example_values=["9999-47-4360"])
    phone: str | None = OutputField(example_values=["9999-48-1134"])
    updated: str | None = OutputField(example_values=["2020-08-05T07:02:05"])
    division: str | None = OutputField(example_values=["testdivision"])
    organization: str | None = OutputField(example_values=["Iki City"])


class NirContactsOutput(ActionOutput):
    tech: NirContactOutput | None
    admin: NirContactOutput | None


class NirNetOutput(ActionOutput):
    cidr: str | None = OutputField(example_values=["223.130.192.0/20"])
    name: str | None = OutputField(example_values=["Test Cloud Corp."])
    range: str | None = OutputField(example_values=["223.130.192.0 - 223.130.207.255"])
    handle: str | None = OutputField(example_values=["NBP-NET"])
    address: str | None = OutputField(
        example_values=["Gyeonggi-do Bundang-gu, Seongnam-si Bundangnaegok-ro 131"]
    )
    country: str | None = OutputField(example_values=["KR"])
    created: str | None = OutputField(example_values=["2017-06-16T00:00:00"])
    updated: str | None
    contacts: NirContactsOutput | None
    nameservers: str | None
    postal_code: str | None = OutputField(example_values=["99999"])


class NirOutput(ActionOutput):
    raw: str | None
    nets: list[NirNetOutput] | None
    query: str | None = OutputField(example_values=["223.130.195.200"])


class WhoisIpOutput(PermissiveActionOutput):
    asn: str | None = OutputField(column_name="ASN")
    asn_cidr: str | None = OutputField(column_name="ASN CIDR")
    asn_country_code: str | None = OutputField(column_name="ASN Country Code")
    asn_date: str | None = OutputField(column_name="ASN Date")
    asn_description: str | None = OutputField(example_values=["DNIC-AS-99999, US"])
    asn_registry: str | None = OutputField(column_name="ASN Registry")
    network: NetworkOutput | None
    entities: list[str] | None
    nir: NirOutput | None
    objects: list[ObjectOutput] | None
    query: str | None
    raw: str | None


class SummaryNetworkOutput(ActionOutput):
    start_address: str | None = OutputField(example_values=["8.0.0.0"])
    end_address: str | None = OutputField(example_values=["8.255.255.255"])


class WhoisIpSummary(ActionOutput):
    registry: str | None
    asn: str | None
    country_code: str | None
    network: list[SummaryNetworkOutput] | None


def whois_ip(params: WhoisIpParams, soar: SOARClient[WhoisIpSummary]) -> WhoisIpOutput:
    ip = params.ip
    logger.debug(f"Validating/Querying IP '{ip}'")
    logger.info("Querying...")
    whois_response = lookup_rdap(ip)

    logger.info("Parsing response")
    whois_response["objects"] = list((whois_response.get("objects") or {}).values())

    network = whois_response.get("network")
    soar.set_summary(
        WhoisIpSummary(
            registry=whois_response.get("asn_registry"),
            asn=whois_response.get("asn"),
            country_code=whois_response.get("asn_country_code"),
            network=[
                SummaryNetworkOutput(
                    start_address=network.get("start_address"),
                    end_address=network.get("end_address"),
                )
            ]
            if network
            else None,
        )
    )
    return WhoisIpOutput(**whois_response)
