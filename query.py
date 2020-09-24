#!/usr/bin/env python3
import logging
import requests
from utls import get_to_resolve, handle_args

api = 'https://dns.google.com/resolve?name={}&type=A&ecs=111.0.0.0'
helpmsg = '''Automatically query hosts from Google DNS.
    Usage: hosts_query.py domains.txt > hosts
       Or: echo example.com | hosts_query.py
       Or: hosts_query.py then input one domain for a line and then ctrl+Z
    Empty lines, comments and orders won't be kept.
    Chain compact.py if you want.'''
s = requests.session()


def resolve(domain: str):
    '''query one domain'''
    data = s.get(api.format(domain), timeout=10).json()
    if data['Status'] == 0 and not data.get("Authority"):
        return (ans['data']+' '+domain for ans in data['Answer'] if ans['type'] == 1)
    else:
        logging.warning(f'resolve {domain} failed.')


if __name__ == "__main__":
    to_resolve = get_to_resolve(handle_args(helpmsg))
    for domain in to_resolve:
        for entry in resolve(domain):
            print(entry)
