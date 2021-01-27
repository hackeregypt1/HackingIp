import os
import time
os.system("clear")
pkg install cowsay -y

print ("\033[1;91m██╗██████╗░")
print ("\033[1;91m██║██╔══██╗")
print ("\033[1;91m██║██████╔╝")
print ("\033[1;91m██║██╔═══╝░")
print ("\033[1;91m██║██║░░░░░")

print ("\033[1;91m[01]DDOS")
print ("\033[1;91m[02]Ping Phone")
cow Hello
a = input ("\033[0;32mWhat U Need: ")
if a == "01" :
  os.system("clear")
  ae = input ("\033[0;32m Type Ip: ")
  ping ae
if a == "02" :
  ad = input ("\033[0;32mType Ip: ")
  print ("start ping" +ad)
  time.sleep(6)
  ping ad
