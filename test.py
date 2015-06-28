#!/usr/bin/env python

gcc="/usr/bin/gcc"
cpuinfo="/proc/cpuinfo"
import os
import time
result={"CPU":"","HW":"","GCC":"","kernel":"","PIC":"","GMPI":""}

###Get the kernel version
fi=open("/proc/version")
rd=fi.read()
fi.close()
li=rd.split()
result["kernel"]=li[2]
###Get the cpuinfo###
fi=open(cpuinfo)
rd=fi.readlines()
fi.close()
li1=[]
li2=[]
for i in rd:
    if i.find("model name")==0:
        li1=i.split(":")
        result["CPU"]=li1[1].strip()
    if i.find("Hardware")==0:
        li2=i.split(":")
        result["HW"]=li2[1].strip()

print ("::Testing gcc installed")
if not os.path.exists(gcc):
    print("::>gcc not installed")
else:
    print("::>GCC installed")
    ##Get the GCC version##
    pip=os.popen("gcc -dumpversion")
    pip2=os.popen("gcc -dumpmachine")
    
    result["GCC"]=pip.read().strip()+":"+pip2.read().strip()
    pip.close()
    pip2.close()

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
    result["PIC"]="{0:.3F}".format(t1)

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
    result["GMPI"]="{0:.3f}".format(t2)

####Commit the result to internel
import urllib
import urllib.parse
import urllib.request
url="http://104.160.34.189:8080/send"
if os.path.exists(gcc):
    print("::Start to commit the result to internel...")
    pst=urllib.request.urlopen(url,str(result).encode('utf-8'))
    print("::{0}".format(pst.read().decode().strip()))
    print("::Visit:http://yafeng.linuxd.org/pimark.htm")
