"""

All of this is configured to run at 1280x1024 resolution, playing at
http://notdoppler.com/burritobison.php

Also on chrome. It'll mess up if browser is a different size as it uses
very fragil and poorly designed getpixel() calls to check for things.. 

"""

import ImageGrab, ImageOps
import Image
import sys, os
import win32api, win32con
import time
from random import random
from random import randrange
from multiprocessing import Process

##GLOBALS
shopping = True
playing = True

def mousePos(x=(0,0)):
    win32api.SetCursorPos(x)
    #Temporary position. Eventually this will receive arguments based on
    #game logic
    tmp = (156, 335)

def isSpinning():
    mousePos((475,620))
    expectedVal = (255, 225, 13)
    box = (473,377,530,432)
    
    im = ImageGrab.grab()
    
    inVal = im.getpixel((500, 390))
    ##print inVal
    ##print expectedVal
    im.save(os.getcwd() + '\\' + 'Spinning.png', "PNG")
    if inVal == expectedVal:
        print 'Spinning = True'
        return True
    else:
        print 'Not spinning'
        return False
    ##im.save(os.getcwd() + '\\' + 'text_002.png', "PNG")

def launcher():
    
    expectedVal= (250, 152, 135)
    im = ImageGrab.grab((455, 435, 501, 467))
    inVal =  im.getpixel((41,24))
##    print inVal
##    im.save(os.getcwd() + '\\' + 'launcher.png', "PNG")
##    im.putpixel((32,28), (0,0,0))
##    print inVal
    if inVal != expectedVal:
        leftClick()
        im.save(os.getcwd() + '\\' + 'launcher.png', "PNG")
        print 'Launch!'
        return 1
    else:
        print 'missed'
        launcher()

def leftClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
##    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    print "MOUSE CLICK!!"
    time.sleep(.05)
    

def runFinished():
    expectedVal = (42,181,240)
    eVal2 = (17,31,75)
    box = (181,362,850,452)
    
    im = ImageGrab.grab(box)
    
    inVal = im.getpixel((591, 30))
    inVal2 = im.getpixel((35, 49))
    
    if inVal == expectedVal and inVal2 == eVal2:
        return True


def fuzzCheck(im):
    coppa = (99,104,137)
    if im.getpixel((randrange(263,290),(randrange(196,223)))) == coppa:
        print 'A cop!'
        return True
    if im.getpixel((randrange(295,320),(randrange(196,223)))) == coppa:
        print 'A cop!'
        return True



def bubbleCheck(im):
    bubble = (252,114,186)
    if im.getpixel((randrange(298,325),randrange(100,120))) == bubble:
        print 'A Bubble!'
        return True
    if im.getpixel((randrange(325,350),randrange(80,200))) == bubble:
        print 'A Bubble!'

    

def specialChecker(im):
    special = (255,250,240)
    if im.getpixel((624,130)) == special:
        return(True)

def spinCheck(im):
    launchGuy = (255,242,252)
    if im.getpixel((546,90)) == launchGuy:
        return True
    
def multiClick():
    for i in range(14):
        leftClick()
        
def eventFinder():
    
    box = (200,500,884,750)
    im = ImageGrab.grab(box)

    if specialChecker(im):
        print 'Special spotted!\n'
        p = Process(target= multiClick())
        p.start()
        p.join()
        

    if bubbleCheck(im):
        print "A bubble has appeared!\n"
        leftClick()

##    if specialChecker(im):
##        print 'Special spotted!\n'
##        for i in range(15):
##            leftClick()

    if fuzzCheck(im):
        leftClick()

    if specialChecker(im):
        print 'Special spotted!\n'
        

    if spinCheck(im):
        if isSpinning():
            launcher()
            
    print 'searching...'
        
        


def canShop():
    im = ImageGrab.grab()
    
    expectedVal = (242,227,110)
    inVal = im.getpixel((695,385))
    if expectedVal == inVal:
        return True

def exitShop():
    mousePos((840,785))
    leftClick()

def checkSales():
    im = ImageGrab.grab()

    
    if im.getpixel((275,440))[2] < 150:
        print 'Elastic for sale\n'
        mousePos((275,525))
        leftClick()
        time.sleep(.05)
        return True
    
    elif im.getpixel((370,435))[2] < 150:
        print 'slip for sale\n'
        mousePos((370,435))
        leftClick()
        time.sleep(.05)
        return True
    
    elif im.getpixel((465,439))[2] < 150:
        print 'Pickpocket for sale\n'
        mousePos((465,439))
        leftClick()
        time.sleep(.05)
        return True
    
    elif im.getpixel((458,532))[2] < 150:
        print 'Resistance for sale\n'
        mousePos((458,532))
        leftClick()
        time.sleep(.05)
        return True
    
    elif im.getpixel((365,530))[2] < 150:
        print 'rocket for sale\n'
        mousePos((365,530))
        leftClick()
        time.sleep(.05)
        return True
    
    elif im.getpixel((270,530))[2] < 150:
        print 'Bouncies for sale\n'
        mousePos((270,530))
        leftClick()
        time.sleep(.1)
        return True
    
    elif im.getpixel((272, 635))[2] < 150:
        print 'BubbleGum for sale\n'
        mousePos((272, 635))
        leftClick()
        time.sleep(.1)
        return True
    
    elif im.getpixel((367,635))[2] < 150:
        print 'Glider for sale\n'
        mousePos((367,635))
        leftClick()
        time.sleep(.1)
        return True
    
    elif im.getpixel((460,635))[2] < 130:
        print 'Rocket for sale\n'
        mousePos((460,635))
        leftClick()
        time.sleep(.1)
        return True
    
    elif im.getpixel((270,725))[2] < 150:
        print 'Pogo for sale\n'
        mousePos((270,725))
        leftClick()
        time.sleep(.1)
        return True
    
    elif im.getpixel((370,725))[2] < 150:
        print 'Pepper for sale\n'
        mousePos((370,725))
        leftClick()
        time.sleep(.1)
        return True
    
    elif im.getpixel((463,725))[2] < 150:
        print 'general for sale\n'
        mousePos((463,725))
        leftClick()
        time.sleep(.1)
        return True
    
    else:
        return False


def buy():
    mousePos((745,535))
    leftClick()
  
def retry():
    mousePos((780,415))
    leftClick()

def clickInfo():
    mousePos((195,424))
    leftClick()

def infoBoxLeft():
    expectedVal = (46,195,251)
    eVal2 = (251,223,114)
    box = (160,339,460,652)
    
    im = ImageGrab.grab(box)
    
    inVal2 = im.getpixel((92,84))
    inVal = im.getpixel((24,82))

    if inVal == expectedVal and inVal2 == eVal2:
        print "an InfoBox is on screen"
        return True

def infoBoxMid():
    expectedVal = (28,184,250)
    eVal2 = (251,223,114)
    box = (160,339,460,652)
    
    im = ImageGrab.grab(box)
    
    inVal2 = im.getpixel((230,164))
    inVal = im.getpixel((178,166))

    if inVal == expectedVal and inVal2 == eVal2:
        print "mis-screen InfoBox showing"
        return True

def infoExplosive():
    box = (160,339,460,652)
    im = ImageGrab.grab()
    
    expectedVal = (33,175,235)
    inVal = im.getpixel((389,442))

    eVal2 = (241,216,117)
    inVal2 = im.getpixel((445,440))    

    if inVal == expectedVal and inVal2 == eVal2:
        print "InfoExplosion Dialog On screen"
        return True

def infoBubble():
    im = ImageGrab.grab()

    inPix = (59,195,246)
    if im.getpixel((385,440)) == inPix:
        return True
    
    


boxes = [1,1,1,1,1,1]
def play():    
    shopping = False
    count =0
    
    while True:
        if shopping == False:
            if infoBoxLeft() == True:
                clickInfo()
                boxes[0]=0
                               
            elif infoBoxMid() == True:
                mousePos((345,505))
                leftClick()

            elif infoExplosive() == True:
                mousePos((395,440))
                leftClick()
            if infoBubble():
                mousePos((385,440))
                leftClick()
                                   
            else:
                eventFinder()
                count +=1
                print count
                if count >15:
                    leftClick()
                    count=0
                eventFinder()
                
            if runFinished() == True:
                if canShop() == True:
                    mousePos((695,385))
                    leftClick()
                    shopping = True
                else:               
                    retry()
                    time.sleep(2)



        else:
            
            while checkSales() == True:
                buy()
            exitShop()
            time.sleep(2)
            play()

                

def main():
##    pass  
    time.sleep(2)
    play()
        
if __name__ == '__main__':
    main()
            

    
            
