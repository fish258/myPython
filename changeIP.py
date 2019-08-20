#!/usr/bin/python
p = os.popen("curl ifconfig.me")
publicIP = p.read()
f=open('ip.txt','r+')
flist=f.readlines()
flist[3]='%s\n'%(publicIP)
f=open('ip.txt','w+')
f.writelines(flist)
