#!/usr/bin/env python
"""
temp.py - Phenny Ping Module based on
ping.py - Phenny Ping Module
Author: F. Tricas
Author: Sean B. Palmer, inamidst.com
About: http://inamidst.com/phenny/
"""


import subprocess

def temp(phenny, input): 
   arg='sudo /home/pi/usr/src/pruebas/temperatura' 
   p=subprocess.Popen(arg,shell=True,stdout=subprocess.PIPE)
   data = p.communicate()
   split_data = data[0].split()
   tempC = split_data[0]
   my_ip = 'La temperatura es %s' %  tempC

   phenny.say(input.nick + '!' + ' ' + my_ip)
temp.priority = 'high'
temp.commands = ['temp']

def ip(phenny, input):
  arg='ip route list'
  p=subprocess.Popen(arg,shell=True,stdout=subprocess.PIPE)
  data = p.communicate()
  split_data = data[0].split()
  ipaddr = split_data[split_data.index('src')+1]
  my_ip = 'La ip de la raspberry es %s' %  ipaddr

  phenny.say(input.nick + '!' + ' ' + my_ip)
ip.priority = 'high'
ip.commands = ['ip']

import os

def ls(phenny, input):   
  lista=os.listdir('.')
  for filename in lista:
     phenny.say(input.nick + '!' + ' ' + filename)

ls.priority = 'high'
ls.commands = ['ls']


if __name__ == '__main__': 
   print __doc__.strip()
