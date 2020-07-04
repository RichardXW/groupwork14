#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd
import subprocess

__author__ = "Zunye Tang, Xiangwen Qiao, Wenyao Chen, Bofei Zhang Data Scicence, LZU University "
__copyright__ = "Copyright © 2020, Group 14, Zunye Tang"
__version__ = 0.2


class Infor:
    def __init__(self,version='v4.4'):
        self.version = version
        self.repo = "C:\\Users\\17301\\Desktop\\linux-stable\\"
        self.dev = "C:\\Users\\17301\\Desktop\\数据科学编程\\out.csv"
        self.name_set = set()


    def infor_(self,set_name):
        ls = []
        cmd1 = 'git log --pretty=format:"%an,%cd,% ae" --author="'
        cmd2 = '" -1 --date=short'
        for i in set_name:
            cmd = cmd1 + i + cmd2
            get_name_infor = self.get_developer_name(cmd)
            get_name_infor = get_name_infor.communicate()[0].decode("utf-8").split(",")
            ls.append(get_name_infor)
            df = pd.DataFrame(ls,columns=["name", "commit_time", "email"])
        return df


    def get_developer_name(self,cmd):
        """
        cmd command find developers uniq name
        :param cmd:
        :return: developer name
        """
        return subprocess.Popen(cmd, cwd=self.repo, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL,
                         shell=True)

    def get_time(self,dataframe):
        for i in self.name_set:
            cmd = 'git log --pretty=format:"%cd" --author="%s"' % (
                i) + " -1 --date=short"
            p = subprocess.Popen(cmd, cwd=self.repo, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, shell=True)
            last = p.communicate()[0]
            cmd2 = 'git log -1 --pretty=format:"%cd" --author="%s"' % (
                i) + " --reverse --date=short"
            p2 = subprocess.Popen(cmd, cwd=self.repo, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, shell=True)
            start = p.communicate()[0]
            dataframe = pd.concat([dataframe,last,start],axis=1,ignore_index=True)
        return dataframe


    def run(self):
        rev1 = self.version
        cmd = " git log --pretty=format:'%cn' "+rev1+" --follow kernel/sched/core.c "
        git_name_list = self.get_developer_name(cmd)
        raw_counts = git_name_list.communicate()[0]
        for name in raw_counts.decode("utf-8").split("\n"):
            name = name.strip("'")
            self.name_set.add(name)
        df = self.infor_(self.name_set)
        df2 = self.get_time(df)
        return df2


infor = Infor().run()
print(infor)
