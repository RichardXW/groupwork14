'''
__author__ = 'Xiyuan Chang, group14, LZU University '
__copyright__ = 'Copyright © 2020, Group 14, Xiyuan Chang'
__email__='xychang2018@lzu.edu.cn'
__license__ = "GPL V2"
__version__ = 0.2

This code is to get the names, emails, start working time and recent submit time in Linux kernel of submitters who contibute code to kernel/sched/core.c.
We want to use the eamil addresses to get their companies.
The start working time and recent submit time are used to know how long they have been contributing codes to Linux kernel.

We select v4.4 as range. The results are output to a txt file.


'''
from subprocess import Popen, PIPE, check_output,DEVNULL
import re


def name_email(fileName,repo):
    namel = set()
    naem = dict()
    cmd = ["git","log", "--pretty=format:'%cn %ce'", "v4.4", fileName]
    p = Popen(cmd, cwd=repo, stdout=PIPE, shell = True)
    data, res = p.communicate()
    
    for line in data.decode("iso8859-1").split("\n"):
        namel.add(line)#avoid the repeat names  (the results in this set:{name email})
        
    emailformat = re.compile('[a-zA-Z0-9.-_+%]+@[^\s]*[.a-zA-Z0-9]+')#find email
    name = re.compile('[A-Za-z]+ [A-Za-z]+')#find the names of submitters
    for i in l:
        emails = re.findall(emailformat,i)
        names = re.findall(name,i)
        cem = emails[0]#Get strings for the email address
        cna = names[0]
        naem[cna]=cem
    return naem #return a dict :{name:email}
       


def worktime(repo):#start working time and the lastest submit time in Linux kernel of the one who contribute codes to kernel/sched/core.c
    lasttime={} 
    statime = {}
    dic = name_email("kernel/sched/core.c", "D:/linux kernel/linux")
    authors = dic.keys()
    i = list(authors)
    
    
    for i in list(authors):
        cmd = 'git log --pretty=format:"%cd"' + ' ' + '--author="%s"'%(i) + " " + "-1 --date=short"  #the lastest time
        p = Popen(cmd,cwd = repo, stdout=PIPE, stderr=DEVNULL, shell=True)
        data, res = p.communicate()
        cmd2 = 'git log -1 --pretty=format:"%cd"' + ' ' + '--author="%s"'%(i) + " " + "--reverse --date=short"  #the first time of submitting (start time)
        p2 = Popen(cmd,cwd = repo, stdout=PIPE, stderr=DEVNULL, shell=True)
        data2,res2 = p2.communicate()
        for line in data.decode("utf-8").split("\n"):
            lasttime[i]=line
        for start in data2.decode("utf-8").split("\n"):
            statime[i]=start2
        with open('out.txt', 'w') as f:
            for k in lasttime.keys():# results are in txt file:  name lastest time     start time   emails
                print(k,lasttime[k],statime[k],dic[k], file=f)

                


if __name__ == '__main__':
    name_email("kernel/sched/core.c", "D:/linux kernel/linux")
    worktime("D:/linux kernel/linux")
