#!/usr/bin/python3
"""script that fetches https://alu-intranet.hbtn.io/status"""

import urllib.request

if __name__ = "__main__":
    with urllib.request.urlopen("https://alu-intranet.hbtn.io/status") as res:
        body_res = res.read()
        print("Body response:")
        print("\t- type:{}".format(type(body_res)))
        print("\t- content: {}".format(body_res))
        print("\t- utf8 content: {}".format(body_res.decode("utf-8")))