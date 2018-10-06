# coding:utf-8
from sys import argv
script, fn = argv

print "We are going to erase thie file '%s'." % fn
print "If you don't want to erase,you can hit Ctrl\+C."
print "If you want,Please hit the RETURN."

print "Opening the file .. .."
files=open(fn,"w")
raw_input("?")
print "Truncating the file. Goodbye!"
files.truncate()

print "Now,Please input three details for this file:"
l1=raw_input("line1:")
l2=raw_input("line2:")
l3=raw_input("line3:")

print "Data writing .. .."
iles.write(l1+'\n'+l2+'\n'+l3+'\n') #可以用一个write 打印多行
print "And finally,we close it."

files.close()
