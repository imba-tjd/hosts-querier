# Hosts Querier

Query and generate ipv4 hosts to stdout via Google DoH with ecs.

One domain for a line. Empty lines, comments(`#`) and order won't be kept.

No more new features will be added.

Requirements: Python3, requests, access to `https://dns.google`

```bash
./query.py example.com
# --or--
cat domains.txt | ./query.py | ./compact.py | ./border.sh Title > hosts
```
