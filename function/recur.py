#!usr/bin/env python
# *_* encoding: utf-8 *_*
def fact(n):
    if n==1:
        return 1;
    return n*fact(n-1);

def mid(n):
    return fact_iter(1,1,n);
def fact_iter(product,count,max):
    if count>max:
        return product;
    return fact_iter(product*count,count+1,max);

print mid(10);
print fact(10);