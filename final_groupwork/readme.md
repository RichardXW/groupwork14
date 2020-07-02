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
<snip>



