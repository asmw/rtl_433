#!/usr/bin/env python3

"""
Push messages via gotify example

rtl_433 ... -F json | examples/rtl_433_gotify.py
"""

import requests
import sys
import fire
import json

def main(host, token, protocol='https', port=443, priority=8, models=[]):
    print(f"Running, host: {host}:{port}, model filter: {models}")

    for line in sys.stdin:
        print(f"Parsing: {line}")
        try:
            data = json.loads(line)
            if data["model"] not in models:
                continue

            req = requests.post(f'{protocol}://{host}:{port}/message?token={token}', json={
                "message": data["time"],
                "priority": priority,
                "title": data["model"]
            })
            print(req)
        except json.decoder.JSONDecodeError as e:
            print("Parse error: %s" % e.msg)
            continue
    

if __name__ == '__main__':
  fire.Fire(main)
