**Unreleased**
* Converted the app to the Splunk SOAR SDK.
* **Breaking:** Python 3.9 is no longer supported. The app now requires Python 3.13 or 3.15.
* **Breaking:** The minimum supported Splunk SOAR version is now 7.0.0 (previously 6.2.2).
* **Breaking:** Failed actions now prefix the error message with `Action failure in <action name>:`, for example `Action failure in whois ip: Whois query failed. Error: ...`. Playbooks that match on the exact error text need updating.
* **Breaking:** The `whois ip` results table no longer has a Status column.
* **Breaking:** The `whois ip` output datapaths that were also declared as plain strings are removed in favor of their list or object paths. The returned data is unchanged. Removed examples: `action_result.data.*.network.status`, `action_result.data.*.objects.*.roles`, `action_result.data.*.objects.*.contact.email`. Use `...status.*`, `...roles.*` and `...contact.email.*.value` instead.
* **Breaking:** `action_result.data.*.objects` is now an empty list instead of an empty object when no related objects are returned.
