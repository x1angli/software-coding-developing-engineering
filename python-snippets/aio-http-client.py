# -*- coding: utf-8 -*-

__author__ = 'x1ang.li'

"""
This module attempts to download contents from multiple URLs by using aiohttp.
See http://aiohttp.readthedocs.org/en/stable/
Unfortunately, we are unable to limit the number of concurrent connections. That is, the "limit" parameter for the TCPConnector doesn't work.
So we no longer use this module.
Please let me know if there is any solution...
"""

import os
import asyncio

import aiohttp

FIDDLER = False
BASE = os.path.join(os.environ['USERPROFILE'], 'Desktop') # User's Desktop, for MicroSoft Windows
CHUNK_SIZE = 134217728 # buffer size: 128MB
CONCURRENT_CONN = 2

START_INDEX = 2006
END_INDEX = START_INDEX + 3

url = 'http://localhost:8900/Main.asmx'

headers_str = '''
User-Agent: Mozilla/4.0 (compatible; MSIE 6.0; MS Web Services Client Protocol 2.0.50727.5485)
Content-Type: text/xml; charset=utf-8
Content-Length: 851
Expect: 100-continue
'''
# Don't worry. Just leave Content-Length or auth info here, because such headers will be overridden based on actual info

payload_str = """
<?xml version="1.0" encoding="utf-8"?><soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema"><soap:Body><GetData xmlns="http://tempuri.org/">This is the soap method</GetData></soap:Body></soap:Envelope>
""".strip()
# peak year: 2013; total: 252440 entries. That's why we set the annual max to 300000


def parse_headers():
    HEADERS_TO_REMOVE = ['Content-Length', 'Expect', 'HOST']

    headers = {}
    for line in headers_str.splitlines():
        line = line.strip()
        if line == '':
            continue
        line_parts = line.split(': ', maxsplit=1)
        headers[line_parts[0]] = line_parts[1]

    for header in HEADERS_TO_REMOVE:
        headers.pop(header, None)

    return headers

headers = parse_headers()
print(headers)

def fetch_page(conn, year):

    response = yield from aiohttp.post(url, headers=headers, data=payload_str.format(year = year).encode('utf-8'), connector=conn)

    if response.status == 200:
        print("Start receiving response for: %d" % year)

        with open(os.path.join(BASE, '%d.xml' % year), 'wb') as fout:
            while True:
                chunk = yield from response.content.read(CHUNK_SIZE)
                if not chunk:
                    break
                fout.write(chunk)
        print("Finished serializing response for: %d" % year)
    else:
        print("data fetch failed for: %d" % year)
        err_msg = yield from response.content.read()
        print(response.status, err_msg)

    response.close()

def main_loop():
    coros = []
    conn = (aiohttp.ProxyConnector(proxy="http://127.0.0.1:8888", limit = CONCURRENT_CONN)) if FIDDLER else (aiohttp.TCPConnector(limit = CONCURRENT_CONN))

    for year in range(START_INDEX, END_INDEX):
        coros.append(asyncio.Task(fetch_page(conn, year)))
    yield from asyncio.gather(*coros)

    conn.close()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main_loop())
