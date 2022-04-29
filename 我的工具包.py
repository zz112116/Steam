#!/usr/bin/env python
# -*- coding:utf-8 -*-

def 复制内容(内容):

    import win32clipboard as wcb
    import win32con as wc
    # 打开复制粘贴板
    wcb.OpenClipboard()
    # 我们之前可能已经Ctrl+C了，这里是清空目前Ctrl+C复制的内容。但是经过测试，这一步即使没有也无所谓
    # wcb.EmptyClipboard()
    # 将内容写入复制粘贴板,第一个参数win32con.CF_TEXT不用管，我也不知道它是干什么的
    # 关键第二个参数，就是我们要复制的内容，一定要传入字节
    wcb.SetClipboardData(wc.CF_TEXT, 内容.encode("gbk"))
    # 关闭复制粘贴板
    wcb.CloseClipboard()

if __name__ == "__main__":
    pass