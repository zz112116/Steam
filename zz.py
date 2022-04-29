import time

时间 = '开始：'+ time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + '\n'
with open('日志.txt','a',encoding='utf-8') as f:
    f.write(时间)