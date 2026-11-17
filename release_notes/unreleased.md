**Unreleased**
* Converted the app to the Splunk SOAR SDK.
* **Breaking:** The app now requires Splunk SOAR 7.0.0 or later (previously 6.2.2) and Python 3.13 or 3.15. Python 3.9 is no longer supported.
* **Breaking:** Failed actions now prefix the error message with `Action failure in <action name>:`, for example `Action failure in whois ip: Whois query failed. Error: ...`. Playbooks that match on the exact error text need updating.
* **Breaking:** `action_result.data.*.objects` is now an empty list instead of an empty object when no related objects are returned.
* The `whois ip` results table no longer has a Status column, and its "Whois details" title and fixed size are no longer set.
* The 21 `whois ip` output datapaths that were also declared as plain strings (for example `action_result.data.*.network.status` and `action_result.data.*.objects.*.roles`) are no longer listed in the app manifest. The returned data is unchanged. Use the `.*` paths instead, for example `action_result.data.*.network.status.*`.
