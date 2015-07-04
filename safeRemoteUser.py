#!/usr/bin/python
import sys
from subprocess import call, check_output

args = sys.argv[1:]
if len(args) is not 2:
  sys.exit('usage: safeRemoteUser.py [user] [safe_remote1,safe_remote2]')

tUser = args[0]
safeRemotes = args[1].split(',')

users = check_output(['/usr/bin/who'])
for line in users.split('\n'):
  line = line.split()
  
  if len(line) is not 5:
    continue
  
  user = line[0]
  pts = line[1]
  rAddr = line[4].strip('()')
  
  if user != tUser:
    continue
  
  if rAddr in safeRemotes:
    continue
  
  psPids = check_output(['/bin/ps', '-h', '-o', 'pid', '-t', pts])
  psPidsList = psPids.split('\n')
  
  for pid in psPidsList:
    if pid != '':
      call(['kill', '-9', pid])
