#!/usr/bin/python
p = os.popen("curl ifconfig.me")
publicIP = p.read()
f=open('ip.txt','r+')
flist=f.readlines()
flist[20]="$CFG->wwwroot   = 'http://%s/moodle';\n"%(publicIP)
f=open('ip.txt','w+')
f.writelines(flist)
