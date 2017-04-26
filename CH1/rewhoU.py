#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    > File Name: rewho.py
    > Author: Hughe
    > Mail:1044829783@qq.com 
    > Created Time: 2017年04月20日 星期四 21时43分04秒
"""
"""
py2和py3都可运行的列出所有登录当前系统的用户信息
"""

import os
import re
from distutils.log import warn as printf

with os.popen('who','r') as f:
    for eachLine in f:
        printf(re.split(r'\s\s+|\t',eachLine.strip()))

