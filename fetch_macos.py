#!/usr/bin/env python3
# fetch_macos.py
import os, json, sys, urllib.request

PLATFORM = os.environ.get("PLATFORM", "mac")        # mac / mac_arm64
CHANNEL  = os.environ.get("CHANNEL", "stable")      # stable/beta/dev/canary
API = f"https://versionhistory.googleapis.com/v1/chrome/platforms/{PLATFORM}/channels/{CHANNEL}/versions"

def latest_version():
    req = urllib.request.Request(API, headers={"User-Agent":"mac-chrome-mirror"})
    with urllib.request.urlopen(req, timeout=20) as r:
        data = json.load(r)
    # versions 已按新->旧排列，取第一个
    return data["versions"][0]["version"]

ver = latest_version()
print(ver)
# 供 GitHub Actions 读取
out = os.environ.get("GITHUB_OUTPUT")
if out:
    with open(out, "a") as f:
        f.write(f"version={ver}\n")
