
#-*-coding:utf8-*-
import time

t1 = time.process_time()
a = [i for i in range(10000000)]
t2 = time.process_time()
b = (i for i in range(10000000))
t3 = time.process_time()
c = {i for i in range(10000000)}
t4 = time.process_time()
d = {i:i for i in range(10000000)}
t5 = time.process_time()
print(t2-t1, t3-t2, t4 - t3, t5-t4)