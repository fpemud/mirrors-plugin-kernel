#!/usr/bin/python3
# -*- coding: utf-8; tab-width: 4; indent-tabs-mode: t -*-

import sys
import json
import subprocess


def main():
    rsyncSource = "rsync://rsync.kernel.org/pub"

    cfg = json.loads(sys.argv[1])["config"]
    dataDir = json.loads(sys.argv[1])["storage-file"]["data-directory"]

    mode = cfg.get("mode", "recent-kernel-only")
    if mode == "full":
        patternList = []
    elif mode == "kernel-only":
        patternList = [
            "+ /linux",
            "+ /linux/kernel",
            "+ /linux/kernel/v*",
            "+ /linux/kernel/v*/***",
            "- /**",
        ]
    elif mode == "recent-kernel-only":
        # FIXME: currently it is the same as "kernel-only"
        patternList = [
            "+ /linux",
            "+ /linux/kernel",
            "+ /linux/kernel/v*",
            "+ /linux/kernel/v*/***",
            "- /**",
        ]
    else:
        raise Exception("invalid mode")

    cmd = "/usr/bin/rsync -v -a -z --delete --delete-excluded --partial "
    for p in patternList:
        cmd += "-f '%s' " % (p)
    cmd += "%s %s" % (rsyncSource, dataDir)
    subprocess.run(cmd, shell=True, check=True)


###############################################################################

if __name__ == "__main__":
    main()
