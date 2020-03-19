#!/usr/bin/env python3

from subprocess import Popen, PIPE, check_output


path = "C:\\Users\\17301\\Desktop\\linux-stable"
import git

def gitFileDynamics(fileName, kernelRange, repo):
    cmd = ["git", "-P", "log", "--stat","--oneline","--follow", kernelRange, fileName]
    p = Popen(cmd, cwd=repo, stdout=PIPE)
    data, res = p.communicate()
    # print the git output as one blob
    # print(data.decode("utf-8"))
    # ...or print it split into lines
    for line in data.decode("utf-8").split("\n"):
        print(line)


gitFileDynamics("kernel/sched/core.c", "v4.4..v4.5", path)
