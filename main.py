import keyboard as keyb
import time as t 
from random import *
zd = 0
print("Welcome to Zd coins miner!")
t.sleep(1.5)
print("Click to F7 for start mining")
keyb.wait('F7')
t.sleep(2.2)
print("Preparations in progress... ")
t.sleep(3.5)
print("Mining has started")
t.sleep(1.5)
while True:  
    zd=zd+uniform(0,0.5)
    print("Zd Coins = " + str(zd))
    t.sleep(uniform(3,10))    