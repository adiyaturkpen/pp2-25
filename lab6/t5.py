import time
import math
def time_sqrt(n, t):
    time.sleep(t / 1000)
    a=math.sqrt(n)
    print(f"Square root of {n} after {t} milliseconds is {a}")
num=int(input())
sec=int(input())
time_sqrt(num,sec)
