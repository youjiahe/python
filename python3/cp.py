# -*- coding=utf-8 -*-
#!/usr/bin/env python3
fil_src=open('/bin/ls','rb')
data=fil_src.read()
fil_dest=open('/root/ls','wb')
fil_dest.write(data)
fil_src.close()
fil_dest.close()