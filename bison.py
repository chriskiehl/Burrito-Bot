"""
A bot to automatically play Burrito Bison. 

This was my first big project that I tackled in Python. It has been 
one year since I wrote it, and it still gets forked every now and 
again. So, high time for a refactoring session! 

The original bison.py will remain. It's like a time capsule now. 
"""

import os
import csv
import sys
import time
import Image
import offset
import win32api
import win32con
import ImageOps
import ImageGrab
from ctypes import *
from random import random
from random import randrange
from multiprocessing import Process
from desktop_magic import getMonitorCoordinates 
from desktop_magic import getScreenAsImage as grab

def get_play_area(monitor):
	'''
	Snaps an image of the chosen monitor (zero indexed). 
	Loops through the RGB pixels looking for the value 
	(244,222,176), which corresponds to the top left 
	most pixel of the game.

	It returns the coordinates of the playarea. 
	'''
	
	TOP_LEFT_PIXELS = (204,204,204)
	GREY_BORDER = (204,204,204)
	SCREEN_WIDTH = 719
	SCREEN_HEIGH = 479

	monitor_coords = getMonitorCoordinates(0) #set to whatever monitor you have the game screen on
	im = grab(monitor_coords)
	imageWidth, imHeight = im.size
	imageArray = im.getdata()

	for index, pixel in enumerate(imageArray):
		if pixel == TOP_LEFT_PIXELS:
			# getdata returns a flat array, so the below figures out
			# the 2d coords based on the index position.
			top = (index / imageWidth)
			left = (index % imageWidth)
			if (im.getpixel((left + 1, top + 1)) == GREY_BORDER and
				im.getpixel((left + 2, top + 2)) == GREY_BORDER):
				top += 5
				left += 5
				
				return (left, top, left + SCREEN_WIDTH, top + SCREEN_HEIGH) 

	raise Exception("Play area not in view." 
			"Make sure the game is visible on screen!")	


def _getLocationOffsetAndPixel():
	playArea = get_play_area()
	offset.x = playArea[0]
	offset.y = playArea[1]

	snapshot = ImageGrab.grab(playArea)

	pos = list(win32api.GetCursorPos())
	pos[0] = pos[0] - offset.x
	pos[1] = pos[1] - offset.y
	pixelAtMousePos = getPixel(pos[0], pos[1])

	print pos, pixelAtMousePos

def _dumpDataToExcel(data):
	'''
	dump frequency and bin information to a csv
	file for Histogram creation. 
	'''
	data.sort()
	bins = _createBins(data)
	with open('histogram.csv', 'wb') as csvfile:
		writer = csv.writer(csvfile, delimiter=',')
		writer.writerow(['Frequency', 'Bins'])
		for i in range(len(data)):
			if i < len(bins):
				writer.writerow([data[i], bins[i]])
			else:
				writer.writerow([data[i]])

def _createBins(data, binNum=15):
	'''
	Generates equally sized bins for 
	histogram output
	'''
	minVal = data[0]
	maxVal = data[-1]
	dataRange = maxVal - minVal
	binRange = dataRange/binNum
	bins = []
	for i in range(binNum):
		bins.append(minVal)
		minVal += binRange
	return bins


def getPixel(x,y):
	offset.x
	offset.y
	

	gdi= windll.gdi32
	RGBInt = gdi.GetPixel(windll.user32.GetDC(0),
				offset.x + x, offset.y + y)

	red = RGBInt & 255
	green = (RGBInt >> 8) & 255
	blue = (RGBInt >> 16) & 255
	return (red, green, blue)

def check_pixel(location, color):
	pixel = getPixel(location[0], location[1])
	print 'input color:      ', color
	print 'check pixel color:', pixel 
	if pixel in [color]:
		return True
	return False	

def is_spinner_screen():
	STAR_LOCATION = (339, 47)
	GOLD_STAR_COLOR = (255, 225, 13)
	
	return check_pixel(STAR_LOCATION, GOLD_STAR_COLOR)

def wait_for_needle():
	NEEDLE_CENTER = (327, 121)
	BOARD_COLOR = (250,114,95)

	s = time.time()
	hit_count = 0
	while time.time() - s < 15: #If STILL not found after 15 sec. Prob on wrong screen
		if not check_pixel(NEEDLE_CENTER, BOARD_COLOR):
			hit_count += 1 
			if hit_count > 30:
				return True


def set_mouse_pos(pos=(0,0)):
	x,y = pos
	x = x + offset.x
	y = y + offset.y
	win32api.SetCursorPos((x,y))

def launcher():
    
    expectedVal= (250, 152, 135)
    im = ImageGrab.grab((455, 435, 501, 467))
    inVal =  im.getpixel((41,24))
##    print inVal
##    im.save(os.getcwd() + '\\' + 'launcher.png', "PNG")
##    im.putpixel((32,28), (0,0,0))
##    print inVal
    if inVal != expectedVal:
        left_click()
        im.save(os.getcwd() + '\\' + 'launcher.png', "PNG")
        print 'Launch!'
        return 1
    else:
        print 'missed'
        launcher()


    

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
        left_click()
        
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
        left_click()

##    if specialChecker(im):
##        print 'Special spotted!\n'
##        for i in range(15):
##            left_click()

    if fuzzCheck(im):
        left_click()

    if specialChecker(im):
        print 'Special spotted!\n'
        

    if spinCheck(im):
        if isSpinning():
            launcher()
            
    print 'searching...'
        
        


def can_shop():
	SHOP_BUTTON = (497, 55)
	BUTTON_COLOR = (39, 178, 237)

	if not check_pixel(SHOP_BUTTON, BUTTON_COLOR):
		return True
	return False

def enter_shop():
	SHOP_BUTTON = (497, 55)
	set_mouse_pos(SHOP_BUTTON)
	left_click()

def exitShop():
    set_mouse_pos((685, 446))
    left_click()

def check_sales_and_purcahse():
	shop_items = {
		'elastic_cables': [(116, 99), (236, 138, 207)],
		'slippery_lotion': [(209, 104), (228, 132, 200)],
		'pickpocket': [(304, 101), (234, 136, 205)],
		'bounciness': [(112, 191), (235, 136, 206)],
		'rocket_slam': [(207, 188), (234, 136, 205)],
		'resistance': [(303, 191), (237, 138, 208)],
		'bubble_gummies': [(115, 293), (232, 133, 203)],
		'glider_gummies': [(206, 296), (235, 136, 206)],
		'rocket_gummies': [(303, 295), (227, 131, 199)],
		'pogostick': [(111, 381), (235, 136, 206)],
		'pepper_gummies': [(210, 383), (234, 136, 205)],
		'general_goods': [(306, 380), (233, 134, 204)]
	}

	while True:
		item_available = get_available_items(shop_items)
		if item_available is None:
			break
		purchase_item(item_available)
	print 'Done shopping'

def get_available_items(shop_items):
	for k, v in shop_items.iteritems():
		item_location = v[0]
		item_color = v[1]	
		print 'checking:', k

		if not check_pixel(item_location, item_color):
			print 'purchasing item:', k
			return item_location
	return None

def purchase_item(item_location):
	set_mouse_pos(item_location)
	left_click()

	BUY_BUTTON = (582, 193)
	set_mouse_pos(BUY_BUTTON)
	left_click()
	time.sleep(1)

def on_retry_screen():
	RETRY_LOC, RETRY_COLOR = [(637, 56), (35, 175, 243)]
	if check_pixel(RETRY_LOC, RETRY_COLOR):
		return True
	return False

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
                set_mouse_pos((345,505))
                left_click()

            elif infoExplosive() == True:
                set_mouse_pos((395,440))
                left_click()
            if infoBubble():
                set_mouse_pos((385,440))
                left_click()
                                   
            else:
                eventFinder()
                count +=1
                print count
                if count >15:
                    left_click()
                    count=0
                eventFinder()
                
            if runFinished() == True:
                if canShop() == True:
                    set_mouse_pos((695,385))
                    left_click()
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

def left_click():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    print "MOUSE CLICK!!"
    time.sleep(.05)

def main():
	play_area = get_play_area(0)
	# print play_area
	offset.save_to_json((play_area[0], play_area[1]))
	reload(offset)
	# print offset.x, offset.y

	im = grab(play_area)
	im.save('adfsadsf.png', 'png')
	# # print is_spinner_screen()
	# # set_mouse_pos((720, 270))
	# # wait_for_needle()
	# # left_click()

	# if can_shop():
	# 	enter_shop()

	# time.sleep(3)

	# for i in range(12):
	# 	time.sleep(3)
	pos = win32api.GetCursorPos()
	x = pos[0] - offset.x
	y = pos[1] - offset.y
	print '[(%d, %d), %s]' % (x,y, str(getPixel(x,y)))
	print 

	print on_retry_screen()
	# print on_retry_screen()
	# check_sales_and_purcahse()
	# print getPixel(631, 54)
	
bot_logo = '''



		 ____                      _  _          
		|  _ \                    (_)| |         
		| |_) | _   _  _ __  _ __  _ | |_   ___  
		|  _ < | | | || '__|| '__|| || __| / _ \ 
		| |_) || |_| || |   | |   | || |_ | (_) |
		|____/  \__,_||_|   |_|   |_| \__| \___/ 
				 ____          _   
				|  _ \        | |  
				| |_) |  ___  | |_ 
				|  _ <  / _ \ | __|
				| |_) || (_) || |_ 
				|____/  \___/  \__|



		1. Start Bot
		2. Quit
'''

if __name__ == '__main__':
    print bot_logo
    c = input('Select an option:')
            

    
            
