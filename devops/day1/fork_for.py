#!/usr/bin/env python3
import os
pid=os.fork()
if not pid:
    print('hello')

pid=os.fork()
if not pid:
    print('hello')

pid=os.fork()
if not pid:
    print('hello')

