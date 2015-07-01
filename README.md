# pimark

This is a pi benchmark to calc 100,000 pi  
这是一个计算10万位圆周率的测试程序，

you should install gcc python and gmp to test  
测试前需要安装好gcc、python、gmp，   

if you use debian,unbuntu,please install gcc g++  
 python3 and libgmp-dev   
如果使用的是ubuntu、debian等deb系统，请安装gcc   
g++ python3 libgmp-dev   

the test result is in：   
测试结果在：   

Order by C：<http://yafeng.linuxd.org/pimark.htm>   
Order by GMP：<http://yafeng.linuxd.org/gmpimark.htm>   

if you want to compare gcc and clang,please install clang.  
如果想比较GCC、clang的效率，请安装clang。
顺便说一句，gmp算法应该比不出啥来，因为算法本身依赖gmp  
而系统gmp一般是gcc编译的，等于gcc自己跟自己比了，除非  
重新用clang编译gmp。

##安装（install）：

`git clone https://github.com/yafengabc/pimark.git`

Or download the zip file：
或者下载zip文件：

` wget https://github.com/yafengabc/pimark/archive/master.zip`

##执行（test）：
run `./test.py` to run the banchmark  
运行`./test.py`来测试

##pi.c:
Calc the pi using the C language  
用C写的计算圆周率的程序，网上抄的，经典的J.Marchin公式.

##gmpi.cpp

Calc the pi using the C++ language and gmp library  
用GMP库自己改写的，算法跟上边的一样，效率完爆C版

##verifipi.py

compare the result with pi.c and gmpi.cpp  
比较C版与GMP版的结果。两者当然应该是一样的。
