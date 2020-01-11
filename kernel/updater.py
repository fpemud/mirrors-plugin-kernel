#!/usr/bin/python3
# -*- coding: utf-8; tab-width: 4; indent-tabs-mode: t -*-

import os
import sys
import time
import subprocess


def run(self):
    url = "http://mirrors.tuna.tsinghua.edu.cn/kernel"
    dataDir = sys.argv[1]
    logDir = sys.argv[2]
    logFile = os.path.join(logDir, "wget.log")
    cmd = "/usr/bin/wget -m --no-parent -e robots=off -nH --cut-dirs=1 --wait 1 --reject \"index.html\" -P \"%s\" %s >%s 2>&1" % (dataDir, url, logFile)
    _Util.shellCall(cmd)


class _Util:

    @staticmethod
    def shellCall(cmd):
        # call command with shell to execute backstage job
        # scenarios are the same as FmUtil.cmdCall

        ret = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                             shell=True, universal_newlines=True)
        if ret.returncode > 128:
            # for scenario 1, caller's signal handler has the oppotunity to get executed during sleep
            time.sleep(1.0)
        if ret.returncode != 0:
            ret.check_returncode()
        return ret.stdout.rstrip()


###############################################################################

if __name__ == "__main__":
    run()
