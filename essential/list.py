#!usr/bin/env python
# _*_ encoding: utf-8 _*_
t = ('comeon','man',['hello','world']);
print t;
t[2][0] = 'xiaoyang';
#t[2][1] = '怕了吧';
t[2][1] = (1,);
print t;

d = {'hello':'world','comeon':'man'};
d.pop('hello');
print d.get('0','not have');

s = set([1,3,8,'ceshi']);
s1 = set([3,6,9]);
print(s);
s1.add(7)
s.remove(8)
print s | s1;
