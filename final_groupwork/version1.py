#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd
import subprocess

__author__ = "Zunye Tang, Xiangwen Qiao, Wenyao Chen, Bofei Zhang Data Scicence, LZU University "
__copyright__ = "Copyright © 2020, Group 14, Zunye Tang"
__version__ = 0.1


class Full_infor:
    def __init__(self,version='v4.4'):
        self.version = version
        self.repo = "C:\\Users\\17301\\Desktop\\linux-stable\\"
        self.csv = "C:\\Users\\17301\\Desktop\\数据科学编程\\name.csv"
        self.name_set = set()

    def infor(self,set_name):
        ls = []
        cmd1 = 'git log --pretty=format:"%an,%cd,% ae" --author="'
        cmd2 = '" -1 --date=short'
        for i in set_name:
            cmd = cmd1 + i + cmd2
            get_name_infor = self.get_developer_name(cmd)
            get_name_infor = get_name_infor.communicate()[0].decode("utf-8").split(",")
            ls.append(get_name_infor)
            df = pd.DataFrame(ls,columns=["name", "commit_time", "email"])
        print(df)


    def get_developer_name(self,cmd):
        """
        cmd command find developers uniq name
        :param cmd:
        :return: developer name
        """
        return subprocess.Popen(cmd, cwd=self.repo, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL,
                         shell=True)

    def run(self):
        rev1 = self.version
        cmd = " git log --pretty=format:'%cn' v4.4 --follow kernel/sched/core.c "
        git_name_list = self.get_developer_name(cmd)
        raw_counts = git_name_list.communicate()[0]
        for name in raw_counts.decode("utf-8").split("\n"):
            name = name.strip("'")
            self.name_set.add(name)
        self.infor(self.name_set)


infor = Full_infor().run()
