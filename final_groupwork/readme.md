Assumption1:The companies or organizations where developers work.

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
</snip>



Assumption3: Frequency of commit

We think timestamp is a good way to do this. Using timestamp, we can change it into local time in anywhere with python.
Because we want to submit the frequency, so subtract the adjacent timestamp to get the time interval. 
If it is in hours, it is divided by 3600; if it is in days, it is divided by 3600*24. 
To minimize the sample size, we just use first 100 git commit as example.

