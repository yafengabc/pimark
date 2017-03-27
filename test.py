#!/usr/bin/env python3

gcc="/usr/bin/gcc"
cpuinfo="/proc/cpuinfo"
import os
import time
import getpass
import socket
result={"CPU":"","HW":"","GCC":"","kernel":"","PIC":"","GMPI":"","MTGMPI":"","USER":""}
result["USER"]=getpass.getuser()+": "+socket.gethostname()
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
li3=[]
li4=[]
for i in rd:
    if i.find("model name")==0:
        li1=i.split(":")
        result["CPU"]=li1[1].strip()
    if i.find("Hardware")==0:
        li2=i.split(":")
        result["HW"]=li2[1].strip()
    if i.find("cpu model")==0:
        li3=i.split(":")
        if result["HW"]=="":
            result["HW"]==li3[1].strip()
    if i.find("Processor")==0:
        li4=i.split(":")
        if result["CPU"]=="":
            result["CPU"]==li4[1].strip()


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
#####======Benchmarking C===============
    print("::===Benchmarking C===")
    print("::Compling pi.c..")
    
    t=time.time()
    os.system("gcc -O2 pi.c -o pi -march=native")
    tc1=time.time()-t
    print("::>Complie time:{0}".format(tc1))

    t=time.time()
    os.system("./pi>pi.txt")
    t1=time.time()-t
    sizepi=os.path.getsize('pi.txt')
    print("::>Calc time:{0}".format(t1))
    os.system("rm pi pi.txt")
    result["PIC"]="{0:.3F}".format(t1)

    print("::Wait 10 seconds")
    time.sleep(10)
#####======Benchmarking GMPi===============
    print("::===Benchmarking GMP===")
    print("::Compling gmpi.cpp..")

    import multiprocessing
    t=time.time()
    os.system("g++ -O2 gmpi.cpp -o gmpi -march=native -lgmp -lgmpxx")
    tc2=time.time()-t
    print("::>Complie time:{0}".format(tc2))
    sizegmpi=os.path.getsize('gmpi')

    t=time.time()
    os.system("./gmpi>pi.txt")
    t2=time.time()-t
    print("::>Calc time:{0}".format(t2))
    sizegmpi=os.path.getsize('pi.txt')
    os.system("rm gmpi pi.txt")
    result["GMPI"]="{0:.3f}".format(t2)

    print("::Wait 10 seconds")
    time.sleep(10)
#####======Benchmarking mtGMPi===============
    print("::===Benchmarking mtGMPi Mutithread===")
    print("::Compling mtgmpi.c..")

    t=time.time()
    os.system("gcc -O2 mtgmpi.c -o mtgmpi -march=native -lgmp -lpthread")
    tc2=time.time()-t
    print("::>Complie time:{0}".format(tc2))
    t=time.time()
    os.system("./mtgmpi {0} >pi.txt".format(multiprocessing.cpu_count()))
    t2=time.time()-t
    print("::>Calc time:{0}".format(t2))
    sizemtgmpi=os.path.getsize('pi.txt')
    os.system("rm mtgmpi pi.txt")
    result["MTGMPI"]="{0:.3f}".format(t2)


####Commit the result to internel
import urllib
import urllib.parse
import urllib.request
url="http://pimark.win/send"
#url="http://pimark.applinzi.com/send"
if sizepi==100003 and sizegmpi==100012 and sizemtgmpi==40015:
    print("::File size is{0},{1},{2}..OK".format(sizepi,sizegmpi,sizemtgmpi))
    print("::Start to commit the result to internet...")
    #print(result)
    pst=urllib.request.urlopen(url,str(result).encode('utf-8'))
    print("::{0}".format(pst.readline().decode().strip()))
    print("::Visit:http://pimark.win")
else:
    print("!!! File size is not ok!")
