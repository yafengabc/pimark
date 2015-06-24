#include <iostream>
#include <gmpxx.h>

using namespace std;
int main()
{
    int L=100000;
    int N=L/4+1;
    int M=332200;
    int n=(int)(L/1.39793+1);
    mpf_class s("0",M);
    mpf_class w("80",M);
    mpf_class v("956",M);
    mpf_class q("0",M);

    mpf_class i25("25",M);
    mpf_class i239("57121",M);
    mpf_class K21("0",M);
    mp_exp_t exp;

    for(int k=1;k<=n;++k)
    {
        K21=2*k-1;
        w=w/i25;
        v=v/i239;
        q=w-v;
        q=q/K21;
        if(k%2)
            s=s+q;
        else
            s=s-q;
    }

    string str=s.get_str(exp);
    str.insert(exp,".");
    cout<<str<<endl;
}
