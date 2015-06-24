#!/usr/bin/env python

gcc="/usr/bin/gcc"
clang="/usr/bin/clang"

import os
import time

print ("::test gcc and clang installed")
if not os.path.exists(gcc):
    print("::>gcc not installed")
else:
    print("::>GCC installed")

if not os.path.exists(clang):
    print("::>clang not installed")
else:
    print("::>clang installed")

if  os.path.exists(gcc):
    print("::===Testing GCC benchmark===")

    t=time.time()
    os.system("gcc -O2 pi.c -o pi")
    tc1=time.time()-t
    print("::>Complie time:{0}".format(tc1))

    t=time.time()
    os.system("./pi>/dev/null")
    t1=time.time()-t
    print("::>Calc time:{0}".format(t1))
    os.system("rm pi")
print("::===Testing Clang benchmark===")

if os.path.exists(clang):
    t=time.time()
    os.system("clang -O2 pi.c -o pi")
    tc2=time.time()-t
    print("::>Complie time:{0}".format(tc2))

    t=time.time()
    os.system("./pi>/dev/null")
    t2=time.time()-t
    print("::>Calc time:{0}".format(t2))
    os.system("rm pi")

if os.path.exists(clang) and os.path.exists(gcc):
    print("::>clang complie time is {0:.2f}% to GCC".format(100*tc2/tc1))
    print("::>clang calc time is {0:.2f}% to GCC".format(100*t2/t1))
