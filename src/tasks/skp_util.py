import os, sys, json, re
from pprint import pprint

def run_with_exit(c, cmd):
    res = c.run(cmd, warn=True)
    if res.failed:
        print("Fail to Run: {}".format(res.stderr.strip()))
        sys.exit(-1)
    return res.stdout.strip()

def run_without_exit(c, cmd):
    res = c.run(cmd, warn=True)
    if res.failed:
        print("Fail to Run: {}".format(res.stderr.strip()))
    return res.stdout.strip()

def is_macos(c):
    uname = run_with_exit(c, "uname")
    if "Darwin" in uname:
        return True
    return False

def is_ubuntu(c):
    uname = run_with_exit(c, "uname -a")
    if "Ubuntu" in uname:
        return True
    return False

def mkdir_usr(c, base):
    path_usr = f"{base}/usr"
    cmd = f"mkdir -p {path_usr}"
    run_with_exit(c, cmd)

