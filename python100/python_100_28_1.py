#!/usr/bin/env python3
with open('/root/1.txt','w+') as f:
    f.tell()
    f.seek(0,0)
    data=['line1\n','line2\n','line3\n','line4\n','line5\n']
    f.writelines(data)
    f.write('line10\n')
    te=f.tell()
    f.seek(0)
    file=f.read()
print(te)
print(file)

