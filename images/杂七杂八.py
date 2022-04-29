#!/usr/bin/env python
# -*- coding:utf-8 -*-
import time


def 日志写入(a):
    时间 = a + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + '\n'
    with open('日志.txt', 'a', encoding='utf-8') as f:
        f.write(时间)
    print(时间)
if __name__ == "__main__":
    日志写入('开始：')