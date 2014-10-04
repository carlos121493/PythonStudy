#!usr/bin/env python
# _*_ encoding: utf-8 _*_

ret = u'中国人是好样的'
reta = ret.encode('utf-8')
print(reta);
print(reta.decode('utf-8'));
print('%s 是对的' % (reta))