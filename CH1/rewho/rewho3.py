"""
    > File Name: rewho.py
    > Author: Hughe
    > Mail:1044829783@qq.com 
    > Created Time: 2017年04月20日 星期四 21时43分04秒
"""

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re

with os.popen('who','r') as f:
    for eachLine in f:
        print(re.split(r'\s\s+|\t',eachLine.strip()))

