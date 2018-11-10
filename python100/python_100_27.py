#！/usr/bin/env python3
print([10+5])
print([10 + i for i in range(10)])
ip_address=['192.168.1.%d' % ip for ip in range(1,255)]
print(ip_address[253])
