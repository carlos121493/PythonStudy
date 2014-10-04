#!usr/bin/env python
# *_* encoding:utf-8 *_*

def func(a,b,c=0,*arg,**kw):
    print "a is",a;
    print "b is",b;
    print "c is",c;
    if not isinstance(c,(int,float)):
        raise TypeError("wo ca c not number");
        return;
    sub = 0;
    for i in arg:
        if(isinstance(i,(int,float))):
            sub += i;
        else:
            print i
    print sub;
    for k in kw:
        print kw[k];

#func(1,3,4);
#func(*(2,4,5,6,7,8));
#func(*(2,4,"dd",6,7,8));
#func(*(2,4,9,6,7,8,"bushiba"),city="heeee",comeon="man");
#func(*(2,4,9,6,7,8,"bushiba"),**{"city":"shanghai","comeon":"man"});
#func(2,7,8,'ddd',9,3,7,**{"city":"shanghai","comeon":"man"});
func(*range(30),**{"city":"shanghai","comeon":"man"});