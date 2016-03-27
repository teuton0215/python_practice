#/use/env/python 3
#-*- encoding:utf-8 -*-

import subprocess
#use cmd  nslookup www.python.org
print('$ nslookup www.python.org')
r = subprocess.call(['nslookup', 'www.python.org'])
#The  end
print('Exit code:', r)