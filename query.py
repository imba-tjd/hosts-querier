import json
import logging
from urllib.request import urlopen
from utls import get_to_resolve, handle_args

api = 'https://dns.google.com/resolve?name={}&type=A&ecs=111.0.0.0'
helpmsg = '''Automatically query hosts from Google DNS.
    Usage: hosts_query.py domains.txt > hosts
       Or: echo example.com | hosts_query.py
       Or: hosts_query.py then input one domain for a line and then ctrl+Z
    Empty lines and comments will be ignored.
    Chain compact.py if you want.'''


def resolve(domain: str):
    '''query one domain'''
    response = urlopen(api.format(domain), timeout=5).read().decode('utf-8')
    data = json.loads(response)
    if data['Status'] == 0:
        return (ans['data']+' '+domain for ans in data['Answer'])
    else:
        logging.warning(f'resolve {domain} failed.')


if __name__ == "__main__":
    to_resolve = get_to_resolve(handle_args(helpmsg))
    for domain in to_resolve:
        for entry in resolve(domain):
            print(entry)
