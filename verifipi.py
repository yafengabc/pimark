import os
print("::Testing Pi.c....")
os.system("gcc pi.c -O2 -o pi")
os.system("g++ gmpi.cpp -O2 -o gmpi -lgmp -lgmpxx")
os.system("./pi>pic")
print("::Testing Pi.GMP....")
os.system("./gmpi>pigmp")
fi1=open("pic")
fi2=open("pigmp")
rd1=fi1.read()
print("::size of Pi.c {0}".format(len(rd1)))
rd2=fi2.read()
print("::size of Pi.GMP {0}".format(len(rd2)))
n=0
if len(rd1)>len(rd2):
    l=len(rd2)
else:
    l=len(rd1)
for i in range(l):
    if rd2[i]:
        if rd1[i]==rd2[i]:
            n+=1    
        else:
            break
if n>100000:
    print("::Test OK:{0}".format(n))
fi1.close()
fi2.close()
os.system("rm pi pigmp pic gmpi")
