# Hosts Querier

Query and generate ipv4 hosts to stdout via Google DoH with ecs.

Empty lines, comments(`#`) and order won't be kept.

No more new features will be added.

Requirements: Python3, requests, access to `https://dns.google`

```bash
./query.py domains.txt | ./compact.py | ./border.sh Title
```
