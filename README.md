## Description

This program queries Opennic Tier2 DNS servers and returns the top 10 closest based on geographic location that also anonymize logs and have greater than 95% uptime. It then passes this list to namebench whcih tests and recommends the fastest acceptible DNS servers.

## Requirements

This program uses subprocess.run() which requires Python 3.5 or later
Requires Namebench be installed - https://code.google.com/archive/p/namebench/downloads

## Testing

Has been test to work on macOS Sierra
