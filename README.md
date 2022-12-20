[comment]: # "Auto-generated SOAR connector documentation"
# WHOIS RDAP

Publisher: Splunk  
Connector Version: 2\.1\.0  
Product Vendor: Generic  
Product Name: Whois RDAP  
Product Version Supported (regex): "\.\*"  
Minimum Product Version: 5\.3\.5  

This app implements investigative actions using RDAP

[comment]: # " File: README.md"
[comment]: # "  Copyright (c) 2016-2022 Splunk Inc."
[comment]: # ""
[comment]: # "Licensed under the Apache License, Version 2.0 (the 'License');"
[comment]: # "you may not use this file except in compliance with the License."
[comment]: # "You may obtain a copy of the License at"
[comment]: # ""
[comment]: # "    http://www.apache.org/licenses/LICENSE-2.0"
[comment]: # ""
[comment]: # "Unless required by applicable law or agreed to in writing, software distributed under"
[comment]: # "the License is distributed on an 'AS IS' BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,"
[comment]: # "either express or implied. See the License for the specific language governing permissions"
[comment]: # "and limitations under the License."
[comment]: # ""
## SDK and SDK Licensing details for the app

## ipwhois

This app uses the python-ipwhois module, which is licensed under the BSD License, Copyright (c)
2013-2020 Philip Hane.

## dnspython

This app uses the python-dnspython module, which is licensed under the Freeware (BSD-like),
Copyright (C) 2003-2007, 2009-2011 Nominum, Inc.


### Supported Actions  
[whois ip](#action-whois-ip) - Execute a whois lookup on the given IP  
[test connectivity](#action-test-connectivity) - Validate the asset configuration for connectivity using supplied configuration  

## action: 'whois ip'
Execute a whois lookup on the given IP

Type: **investigate**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**ip** |  required  | IPv4 or IPv6 address to query | string |  `ip`  `ipv6` 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.status | string | 
action\_result\.parameter\.ip | string |  `ip`  `ipv6` 
action\_result\.data\.\*\.asn | string | 
action\_result\.data\.\*\.asn\_cidr | string | 
action\_result\.data\.\*\.asn\_country\_code | string | 
action\_result\.data\.\*\.asn\_date | string | 
action\_result\.data\.\*\.asn\_description | string | 
action\_result\.data\.\*\.asn\_registry | string | 
action\_result\.data\.\*\.entities\.\* | string | 
action\_result\.data\.\*\.network\.cidr | string | 
action\_result\.data\.\*\.network\.country | string | 
action\_result\.data\.\*\.network\.end\_address | string |  `ip`  `ipv6` 
action\_result\.data\.\*\.network\.events\.\*\.action | string | 
action\_result\.data\.\*\.network\.events\.\*\.actor | string | 
action\_result\.data\.\*\.network\.events\.\*\.timestamp | string | 
action\_result\.data\.\*\.network\.handle | string | 
action\_result\.data\.\*\.network\.ip\_version | string | 
action\_result\.data\.\*\.network\.links\.\* | string | 
action\_result\.data\.\*\.network\.name | string | 
action\_result\.data\.\*\.network\.notices\.\*\.description | string | 
action\_result\.data\.\*\.network\.notices\.\*\.links | string | 
action\_result\.data\.\*\.network\.notices\.\*\.links\.\* | string | 
action\_result\.data\.\*\.network\.notices\.\*\.title | string | 
action\_result\.data\.\*\.network\.parent\_handle | string | 
action\_result\.data\.\*\.network\.raw | string | 
action\_result\.data\.\*\.network\.remarks | string | 
action\_result\.data\.\*\.network\.remarks\.\*\.description | string | 
action\_result\.data\.\*\.network\.remarks\.\*\.links | string | 
action\_result\.data\.\*\.network\.remarks\.\*\.links\.\* | string | 
action\_result\.data\.\*\.network\.remarks\.\*\.title | string | 
action\_result\.data\.\*\.network\.start\_address | string |  `ip`  `ipv6` 
action\_result\.data\.\*\.network\.status\.\* | string | 
action\_result\.data\.\*\.network\.type | string | 
action\_result\.data\.\*\.nir | string | 
action\_result\.data\.\*\.objects\.\*\.contact\.address\.\*\.type | string | 
action\_result\.data\.\*\.objects\.\*\.contact\.address\.\*\.value | string | 
action\_result\.data\.\*\.objects\.\*\.contact\.email | string | 
action\_result\.data\.\*\.objects\.\*\.contact\.email\.\*\.type | string | 
action\_result\.data\.\*\.objects\.\*\.contact\.email\.\*\.value | string | 
action\_result\.data\.\*\.objects\.\*\.contact\.kind | string | 
action\_result\.data\.\*\.objects\.\*\.contact\.name | string | 
action\_result\.data\.\*\.objects\.\*\.contact\.phone | string | 
action\_result\.data\.\*\.objects\.\*\.contact\.phone\.\*\.type | string | 
action\_result\.data\.\*\.objects\.\*\.contact\.phone\.\*\.value | string | 
action\_result\.data\.\*\.objects\.\*\.contact\.role | string | 
action\_result\.data\.\*\.objects\.\*\.contact\.title | string | 
action\_result\.data\.\*\.objects\.\*\.entities | string | 
action\_result\.data\.\*\.objects\.\*\.entities\.\* | string | 
action\_result\.data\.\*\.objects\.\*\.events\.\*\.action | string | 
action\_result\.data\.\*\.objects\.\*\.events\.\*\.actor | string | 
action\_result\.data\.\*\.objects\.\*\.events\.\*\.timestamp | string | 
action\_result\.data\.\*\.objects\.\*\.events\_actor | string | 
action\_result\.data\.\*\.objects\.\*\.events\_actor\.\*\.action | string | 
action\_result\.data\.\*\.objects\.\*\.events\_actor\.\*\.timestamp | string | 
action\_result\.data\.\*\.objects\.\*\.handle | string | 
action\_result\.data\.\*\.objects\.\*\.links\.\* | string | 
action\_result\.data\.\*\.objects\.\*\.notices | string | 
action\_result\.data\.\*\.objects\.\*\.notices\.\*\.description | string | 
action\_result\.data\.\*\.objects\.\*\.notices\.\*\.links\.\* | string | 
action\_result\.data\.\*\.objects\.\*\.notices\.\*\.title | string | 
action\_result\.data\.\*\.objects\.\*\.raw | string | 
action\_result\.data\.\*\.objects\.\*\.remarks | string | 
action\_result\.data\.\*\.objects\.\*\.remarks\.\*\.description | string | 
action\_result\.data\.\*\.objects\.\*\.remarks\.\*\.links | string | 
action\_result\.data\.\*\.objects\.\*\.remarks\.\*\.links\.\* | string | 
action\_result\.data\.\*\.objects\.\*\.remarks\.\*\.title | string | 
action\_result\.data\.\*\.objects\.\*\.roles\.\* | string | 
action\_result\.data\.\*\.objects\.\*\.status | string | 
action\_result\.data\.\*\.objects\.\*\.status\.\* | string | 
action\_result\.data\.\*\.query | string | 
action\_result\.data\.\*\.raw | string | 
action\_result\.data\.\*\.nir\.raw | string | 
action\_result\.data\.\*\.nir\.nets\.\*\.cidr | string | 
action\_result\.data\.\*\.nir\.nets\.\*\.name | string | 
action\_result\.data\.\*\.nir\.nets\.\*\.range | string | 
action\_result\.data\.\*\.nir\.nets\.\*\.handle | string | 
action\_result\.data\.\*\.nir\.nets\.\*\.address | string | 
action\_result\.data\.\*\.nir\.nets\.\*\.country | string | 
action\_result\.data\.\*\.nir\.nets\.\*\.created | string | 
action\_result\.data\.\*\.nir\.nets\.\*\.updated | string | 
action\_result\.data\.\*\.nir\.nets\.\*\.contacts\.tech | string | 
action\_result\.data\.\*\.nir\.nets\.\*\.contacts\.admin\.email | string | 
action\_result\.data\.\*\.nir\.nets\.\*\.nameservers | string | 
action\_result\.data\.\*\.nir\.nets\.\*\.postal\_code | string | 
action\_result\.data\.\*\.nir\.nets\.\*\.contacts\.tech\.email | string | 
action\_result\.data\.\*\.nir\.nets\.\*\.contacts\.admin | string | 
action\_result\.data\.\*\.nir\.query | string | 
action\_result\.data\.\*\.network\.events | string | 
action\_result\.data\.\*\.objects\.\*\.events | string | 
action\_result\.data\.\*\.nir\.nets\.\*\.contacts\.tech\.fax | string | 
action\_result\.data\.\*\.nir\.nets\.\*\.contacts\.tech\.phone | string | 
action\_result\.data\.\*\.nir\.nets\.\*\.contacts\.tech\.updated | string | 
action\_result\.data\.\*\.nir\.nets\.\*\.contacts\.tech\.division | string | 
action\_result\.data\.\*\.nir\.nets\.\*\.contacts\.tech\.organization | string | 
action\_result\.data\.\*\.nir\.nets\.\*\.contacts\.admin\.fax | string | 
action\_result\.data\.\*\.nir\.nets\.\*\.contacts\.admin\.phone | string | 
action\_result\.data\.\*\.nir\.nets\.\*\.contacts\.admin\.updated | string | 
action\_result\.data\.\*\.nir\.nets\.\*\.contacts\.admin\.division | string | 
action\_result\.data\.\*\.nir\.nets\.\*\.contacts\.admin\.organization | string | 
action\_result\.data\.\*\.network\.status | string | 
action\_result\.data\.\*\.objects\.\*\.roles | string | 
action\_result\.data\.\*\.objects\.\*\.notices\.\*\.links | string | 
action\_result\.data\.\*\.objects\.\*\.contact\.address | string | 
action\_result\.data\.\*\.objects\.\*\.links | string | 
action\_result\.summary\.asn | string | 
action\_result\.summary\.country\_code | string | 
action\_result\.summary\.network\.\*\.end\_address | string | 
action\_result\.summary\.network\.\*\.start\_address | string | 
action\_result\.summary\.registry | string | 
action\_result\.message | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'test connectivity'
Validate the asset configuration for connectivity using supplied configuration

Type: **test**  
Read only: **True**

#### Action Parameters
No parameters are required for this action

#### Action Output
No Output