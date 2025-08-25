#!/usr/bin/env python3
# fetch_macos.py
import json, os, sys, urllib.request

def latest_ver(url):
    req = urllib.request.Request(url, headers={"User-Agent":"mac-chrome-mirror"})
    with urllib.request.urlopen(req, timeout=20) as r:
        data = json.load(r)
    return data["versions"][0]["version"]

mac  = latest_ver("https://versionhistory.googleapis.com/v1/chrome/platforms/mac/channels/stable/versions")
arm  = latest_ver("https://versionhistory.googleapis.com/v1/chrome/platforms/mac_arm64/channels/stable/versions")
ver  = max([mac, arm], key=lambda s: [int(x) for x in s.split(".")])

print(ver)
out = os.environ.get("GITHUB_OUTPUT")
if out:
    with open(out, "a") as f:
        f.write(f"version={ver}\n")
