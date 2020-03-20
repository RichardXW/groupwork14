#!/usr/bin/env python3

"""grab the unbuffered output from the git command
   note the -P (no pager) the rest is just the git
   command as you would use it on the commandline.
   subprocess not only takes a command (here in cmd)
   but also allows you to specify the directory in
   which it will be exeucted (cwd means Change Working
   Directory). The output of the git command here is
   placed into a pipe that is then later read by
   p.communicate - we could wait until the subprocess
   completed (using p.wait()) but as we are reading
   the results from a pipe we do not actually need to
   do that here.
   From the pipe we receive a byte-string not a string 
   so we need to explicidly decode it here. Note that
   we are ignoring the return value of p.communicate() """

from subprocess import Popen, PIPE, check_output
import numpy as np

def gitFileDynamics(fileName, kernelRange, repo):
    cmd = ["git", "-P", "log", "--stat","--oneline","--follow", kernelRange, fileName]
    p = Popen(cmd, cwd=repo, stdout=PIPE)
    data, res = p.communicate()
    # print the git output as one blob
    #print(data.decode("utf-8"))
    # ...or print it split into lines
    for line in data.decode("utf-8").split("\n"):
       print(line)

gitFileDynamics("kernel/sched/core.c", "v4.4..v4.5", "linux-stable")



