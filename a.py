import re
ls = open("a","r").readlines()
for l in ls:
 if(l.startswith('shw ')):
     print l[4:]
 elif(l.startswith('vr ')):
     s = l[3:]
     r1 = re.search('(.*)=', s)
     r2 = re.search('=(.*)', s)
     a = str(r1.group(1))
     b = str(r2.group(1))
     print(a)
     print(b)
     print("vars saved")
     if a==b:
         print("is eql 1")
     else:
         print("is eql 0")
 elif(l.startswith('if ')):
     s = l[3:]
     r1 = re.search('(.*)=', s)
     r2 = re.search('=(.*);', s)
     r3 = re.search(';(.*)', s)
     a = str(r1.group(1))
     b = str(r2.group(1))
     print(a)
     print(b)
     print("vars saved")
     if a==b:
         print("is eql 1")
     else:
         print("is eql 0")
 else:
     print "invalid block"
