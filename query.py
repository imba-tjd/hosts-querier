#!/usr/bin/env python3
import logging
import requests
from utls import get_to_resolve, handle_args

api = 'https://dns.google/resolve?edns_client_subnet=111.0.0.0&name='
s = requests.session()
logger = logging.getLogger(__name__)
logger.disabled = True


def resolve(domain: str):
    '''query one domain from Google DoH'''
    data = s.get(api+domain, timeout=5).json()
    if not data['Status'] and not data.get("Authority"):
        return (ans['data'] for ans in data['Answer'] if ans['type'] == 1)
    else:
        logger.warning(f'resolve {domain} failed.')


if __name__ == "__main__":
    logger.disabled = False
    to_resolve = get_to_resolve(handle_args(resolve.__doc__))
    for domain in to_resolve:
        for entry in resolve(domain):
            print(entry+' '+domain)
