# File: whois_rdap_connector.py
# Copyright (c) 2016-2021 Splunk Inc.
#
# SPLUNK CONFIDENTIAL - Use or disclosure of this material in whole or in part
# without a valid written license from Splunk Inc. is PROHIBITED.

# Phantom imports
import phantom.app as phantom

from phantom.base_connector import BaseConnector
from phantom.action_result import ActionResult

# THIS Connector imports
from whois_rdap_consts import *

import json
try:
    from urllib2 import ProxyHandler, build_opener
except ImportError:
    from urllib.request import ProxyHandler, build_opener
from ipwhois import IPWhois
from ipwhois import IPDefinedError
from os import environ


class WhoisRDAPConnector(BaseConnector):

    # actions supported by this script
    ACTION_ID_WHOIS_IP = "whois_ip"
    ACTION_ID_TEST_CONNECTIVITY = 'test_connectivity'

    def __init__(self):

        # Call the BaseConnectors init first
        super(WhoisRDAPConnector, self).__init__()

    def _whois_ip(self, param):

        ip = param[phantom.APP_JSON_IP]

        action_result = self.add_action_result(ActionResult(dict(param)))

        action_result.set_param({phantom.APP_JSON_IP: ip})

        self.debug_print("Validating/Querying IP '{0}'".format(ip))

        self.save_progress("Querying...")

        status, whois_response = self._lookup_rdap(action_result, ip)

        if phantom.is_fail(status):
            return action_result.get_status()

        self.save_progress("Parsing response")

        # the format screws with the object model since the keys change with every run
        # but the keys aren't needed since they are also stored in object.[key].handle
        # changing this to a list

        if whois_response["objects"]:
            objects = whois_response["objects"]
            new_objects = [objects[key] for key in objects]
            whois_response["objects"] = new_objects

        action_result.add_data(whois_response)

        summary = action_result.update_summary({})

        # Create the summary and the message
        if ('asn_registry' in whois_response):
            summary.update({WHOIS_JSON_ASN_REGISTRY: whois_response['asn_registry']})

        if ('asn' in whois_response):
            summary.update({WHOIS_JSON_ASN: whois_response['asn']})

        if ('asn_country_code' in whois_response):
            summary.update({WHOIS_JSON_COUNTRY_CODE: whois_response['asn_country_code']})

        if ('network' in whois_response):
            nets = whois_response['network']
            wanted_keys = ['start_address', 'end_address']
            summary[WHOIS_JSON_NETS] = []
            summary_net = {x: nets[x] for x in wanted_keys}
            summary[WHOIS_JSON_NETS].append(summary_net)

        action_result.set_status(phantom.APP_SUCCESS)

    def _test_asset_connectivity(self, param):
        ip = '8.8.8.8'

        self.debug_print("Validating/Querying IP '{0}'".format(ip))

        self.save_progress("Querying...")

        status, whois_response = self._lookup_rdap(self, ip)
        if not status:
            return status

        self.save_progress("Parsing response")

        if whois_response["query"] and whois_response["query"] == ip:
            self.debug_print("identity test passed")
            return self.set_status_save_progress(phantom.APP_SUCCESS, WHOIS_SUCC_CONNECTIVITY_TEST)

        self.debug_print("identity test failed")
        return self.set_status_save_progress(phantom.APP_ERROR, WHOIS_ERR_CONNECTIVITY_TEST)

    def _lookup_rdap(self, action_result, ip):

        proxy = {}
        if environ.get('HTTP_PROXY'):
            proxy['http'] = environ['HTTP_PROXY']
        if environ.get('HTTPS_PROXY'):
            proxy['https'] = environ['HTTPS_PROXY']

        try:
            if proxy:
                self.debug_print("Found proxy env. Using proxy for connection.")
                handler = ProxyHandler(proxy)
                opener = build_opener(handler)
                obj_whois = IPWhois(ip, proxy_opener=opener)
            else:
                obj_whois = IPWhois(ip)
            whois_response = obj_whois.lookup_rdap()
            return phantom.APP_SUCCESS, whois_response
        except IPDefinedError as e_defined:
            self.debug_print("Got IPDefinedError: {0}".format(str(e_defined)))
            action_result.set_status(phantom.APP_SUCCESS, str(e_defined))
            return phantom.APP_ERROR, None
        except Exception as e:
            self.debug_print("Got exception: type: {0}, str: {1}".format(type(e).__name__, str(e)))
            return action_result.set_status(phantom.APP_ERROR, WHOIS_ERR_QUERY, e), None

    def handle_action(self, param):
        """Function that handles all the actions

        Args:

        Return:
            A status code
        """

        result = None
        action = self.get_action_identifier()

        if (action == self.ACTION_ID_WHOIS_IP):
            result = self._whois_ip(param)
        elif (action == self.ACTION_ID_TEST_CONNECTIVITY):
            self._test_asset_connectivity(param)
        else:
            result = self.unknown_action()

        return result


if __name__ == '__main__':

    import sys
    import pudb

    pudb.set_trace()

    with open(sys.argv[1]) as f:
        in_json = f.read()
        in_json = json.loads(in_json)
        print(json.dumps(in_json, indent=' ' * 4))

        connector = WhoisRDAPConnector()
        connector.print_progress_message = True
        ret_val = connector._handle_action(json.dumps(in_json), None)
        print(json.dumps(json.loads(ret_val), indent=4))

    exit(0)
