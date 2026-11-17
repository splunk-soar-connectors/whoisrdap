**Unreleased**
* Converted the app to the Splunk SOAR SDK.
* The app now requires Splunk SOAR 7.0.0 or later (previously 6.2.2).
* The `whois ip` results table no longer has a Status column, and its "Whois details" title and fixed size are no longer set.
* The 21 `whois ip` output datapaths that were also declared as plain strings (for example `action_result.data.*.network.status` and `action_result.data.*.objects.*.roles`) are no longer listed in the app manifest. The returned data is unchanged. Use the `.*` paths instead, for example `action_result.data.*.network.status.*`.
* `action_result.data.*.objects` is now an empty list instead of an empty object when no related objects are returned.