#!/usr/bin/env python3
import os
import tarfile
tar=tarfile.open('/opt/test/systemd.tar.gz','w:gz')
tar.add('/usr/lib/systemd/system')
tar.close()

tar=tarfile.open('/opt/test/systemd.tar.gz','r:gz')
os.mkdir('/opt/test/system')
os.chdir('/opt/test/system')
tar.extractall()
tar.close()