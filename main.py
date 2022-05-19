#Here

import pyfirmata
import time
import threading


#board = pyfirmata.Arduino("/dev/cu.usbmodem14101")
#it = pyfirmata.util.Iterator(board)
#it.start()


class TL:
    def __init__(self, color):
        self.color = "green" #defaut
        self.carApr = False
        self.runn = True

    def printLight(self):
        if TL.color == "green":
           print("green, GO!")
        if TL.color == "yellow":
           print("green, SLOW!")
        if TL.color == "red":
           print("green, STOP!")


    def carAppr(self):
      if TL.carApr:
        return True
      else:
        return False

    def Print(self):
        return True

    def change(self):
      if TL.color == "green":
        TL.color = "yellow"
        time.sleep(3)
      if TL.color == "yellow":
        TL.color = "red"
        time.sleep(8)
      if TL.color == "red":
        TL.color = "green"
        time.sleep(8)
        
        
    def runF(self):
      while (TL.runn == True):       
        if TL.carAppr() == True:
          TL.color = "green"
        TL.change()
        
