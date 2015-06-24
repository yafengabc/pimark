#!/usr/bin/env python

gcc="/usr/bin/gcc"

import os
import time

print ("::Testing gcc installed")
if not os.path.exists(gcc):
    print("::>gcc not installed")
else:
    print("::>GCC installed")

if  os.path.exists(gcc):
    print("::===Benchmarking C===")
    print("::Compling pi.c..")
    
    t=time.time()
    os.system("gcc -O2 pi.c -o pi -march=native")
    tc1=time.time()-t
    print("::>Complie time:{0}".format(tc1))

    t=time.time()
    os.system("./pi>/dev/null")
    t1=time.time()-t
    print("::>Calc time:{0}".format(t1))
    os.system("rm pi")

    print("::Wait 10 seconds")
    time.sleep(10)
    print("::===Benchmarking GMP===")
    print("::Compling gmpi.cpp..")

    t=time.time()
    os.system("g++ -O2 gmpi.cpp -o gmpi -march=native -lgmp -lgmpxx")
    tc2=time.time()-t
    print("::>Complie time:{0}".format(tc2))

    t=time.time()
    os.system("./gmpi>/dev/null")
    t2=time.time()-t
    print("::>Calc time:{0}".format(t2))
    os.system("rm gmpi")

