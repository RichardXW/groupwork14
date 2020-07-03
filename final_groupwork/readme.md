Assumption1：The companies or organizations where developers work.

Theoretically, people who work for better companies are more likely to do better than people who work for other companies.

$ git log | grep -E -e "<(\\w+)(\\.\\w+)*(\\@\\w+){1}(\\.[a-z]{2,3}){1,2}>" | cut -f 2 -d ":" | uniq

<snip>
Dan Williams <dan.j.williams@intel.com>
 Tony Luck <tony.luck@intel.com>
 Greg Kroah-Hartman <gregkh@linuxfoundation.org>
 zhong jiang <zhongjiang@huawei.com>
 Greg Kroah-Hartman <gregkh@linuxfoundation.org>
 Pablo Neira Ayuso <pablo@netfilter.org>
 wenxu <wenxu@ucloud.cn>
Max Filippov <jcmvbkbc@gmail.com>
 Saeed Mahameed <saeedm@mellanox.com>
<snip>
	
Using python, extract the company name, e.g. mellanox, gmail, arndb. Most of them are companies and organizations. However, we cannot infer that developers works or worked in this company, some developers just use this company’s email service, e.g. Max Filippov <jcmvbkbc@gmail.com>  I cannot find any recording that this person works or worked in google. In the result, we can just take the email name as an indicator.


Assumption2：The total commits of developers

$ git log | grep "^Author: " | awk '{print $2}' | sort | uniq -c | sort -k1,1rn

<snip>
  32842 Linus
  25345 David
  11214 Paul
	……………
      1 张君
      1 张忠山
      1 이건호
<snip>


Assumption3：The frequency of commits:

        e.g: 7 commits per month & only 9commits in a particular week. We assume that the second person submitted one file but there were many bugs so that this guy submitted other commits to fix the bug. The code quality may be bad. But the first person continues committing each month, we can assume this guy continues maintaining the kernel and the code quality may be high with fewer bugs.

$ git log --pretty=format:"%ct" -1000

We think timestamp is a good way to do this. Using timestamp, we can change it into local time in anywhere with python. Because we want to submit the frequency, so subtract the adjacent timestamp to get the time interval. If it is in hours, it is divided by 3600; if it is in days, it is divided by 3600*24. To minimize the sample size, we just use first 100 git commit as example.
 

Assumption4：The number of bugs created by developers

$ git log --oneline --grep="reported-by:"  -i | wc -l

Although it is not the cause of the bug, we think it can be a good indicator of the existence of the bug, not meaning the occurrence of bug. In the git report, ‘reported-by’ tells us which bugs were found and needs to be solved by the developer.

.
Assumption5：The number of bugs fixed by developers

$ git log | grep -c -E -e "^[[:space:]]+Fixes:"

43626
In all git commit, total number of fixes tag is 43626.
Check some of their git log.


Assumption6：The new functions added by developers:

lines added>0 lines deleted = 0 or use tags and regular expressions like "new functions" to count new functions they added. We assume that maybe more new functions developers add, more comprehensive the code is and more meticulous thoughts developers have.

$ git log --grep="new function" --stat

<snip>
include/linux/bpf.h       |  10 ++-
 include/linux/bpf_types.h |   2 +
 include/linux/btf.h       |   5 ++
 include/uapi/linux/bpf.h  |   1 +
 kernel/bpf/btf.c          | 152 +++++++++++++++++++++++++++++++++++++++++++++-
 kernel/bpf/syscall.c      |  15 ++++-
 kernel/bpf/trampoline.c   |  41 ++++++++++++-
 kernel/bpf/verifier.c     |  85 ++++++++++++++++++++------
 8 files changed, 283 insertions(+), 28 deletions(-)
<snip>
Chech the git log, found most of them are insertions is greater than deletions. But some exceptions exist as well, e.g.
<snip>
include/linux/zlib.h            |  6 ++++++
 lib/zlib_deflate/deflate.c      |  6 ++++++
 lib/zlib_deflate/deflate_syms.c |  1 +
 lib/zlib_dfltcc/dfltcc.h        | 11 +++++++++++
 lib/zlib_dfltcc/dfltcc_util.h   |  9 ---------
<snip>
	
dfltcc_util.h was deleted 9 lines.

Assumption7：How long did it take to fix each bug

There is a problem that git doesn’t tell us the bug process, so we cannot find the same bug directly by the git log. So we need the analysis of comment and extract the most important nouns. A every easy way to find the most important nouns is counting the frequency. 
Then git log --grep=”WORD” to find the most initial git commit.

$ git log | grep -E -e "^[[:space:]]+Fixes:"

e.g. Fixes: 0aec4867dca14	

<snip>
I didn't know about messy programs like svgatextmode...  Couldn't this be
    integrated in some linux/drivers/video/console/svgacon.c ?...  So because
    of the existence of the svgatextmode program, the kernel is not supposed to touch to CRT_OVERFLOW/SYNC_END/DISP/DISP_END/OFFSET ?
………
Disabling the check in vgacon_resize() might help indeed, but I'm really
    not sure whether it will work for any chipset: in my patch, CRT registers
    are set at each console switch, since stty rows/cols apply to consoles
    separately...
<snip>

Try some key words, e.g. vgacon_resize, svgatextmode.

$ git log --grep="vgacon_resize" --pretty=format:"%h %ct" |sort -k2 -r

<snip>
d0f73520b378 1427381367
f80561e4d1f9 1403223759
0aec4867dca1 1129564750
6d36ba629e0e 1126797849
<snip>
	
$ git log 6d36ba629e0e

<snip>
[PATCH] vgacon: Fix sanity checking in vgacon_resize
    "I routinely switch the console font during bootup to
    8x8 so I can get 50 lines per screen.  Until 09 Sept,
    just changing to the small font automatically gave me
    all 50 lines -- but now I'm only getting 25 lines even
    with the small font.  The bottom half of the screen
    displays the text that already scrolled off the top."
<snip>

I cannot compare the two commits are talking about the same bug.
The fact is I cannot figure out the key words,  some key words is not in the original bug.


Assumption8：The number of commits on linux kernel patch level:

There are many candidate releases in Linux kernel. Check the number of commits on stable release of developers.

$ for V in `git tag | grep v4.4 | sort -n -k3 -t "." `;do echo "$V:"; git log $V | wc -l; done

<snip>
v4.4:
9393873
v4.4-rc1:
9352724
v4.4-rc2:
9361373
v4.4-rc3:
9367260
……
<snip>
{VERSION}{PATCHLEVEL}{SUBLEVEL}{EXTRAVERSION}{LOCALVERSION}.
