#Okay so currently I'm just going through each line of buttons in order, once one finishes we go to the next and loop again
#Which is fine for rev 1, rev 2 will try and get them all looping together with better colours
#This is all a bit long in the tooth but hell, I'm learning and it's great fun!

import display, time

#We need our colours in here don't we
rgbTable1 = [0xD0021B,0xFF7F00,0xF8B700,0x7ED321,0x50E3C2,0x4A90E2,0x0551AA,0x9013FE,0xBD10E0,0xE010C0]
rgbTable2 = [0xFF7F00,0xF8B700,0x7ED321,0x50E3C2,0x4A90E2,0x0551AA,0x9013FE,0xBD10E0,0xE010C0,0xD0021B]
rgbTable3 = [0xF8B700,0x7ED321,0x50E3C2,0x4A90E2,0x0551AA,0x9013FE,0xBD10E0,0xE010C0,0xD0021B,0xFF7F00]
rgbTable4 = [0x7ED321,0x50E3C2,0x4A90E2,0x0551AA,0x9013FE,0xBD10E0,0xE010C0,0xD0021B,0xFF7F00,0xF8B700]

def line1():
    for i in rgbTable1: #We want to go between the colours in order so loop through the table.
        display.drawPixel(0,0,(i)) 
        display.drawPixel(0,1,(i))  
        display.drawPixel(0,2,(i))  
        display.drawPixel(0,3,(i))
        display.flush() 
        time.sleep_ms(400)

def line2():
    for p in rgbTable2:
        display.drawPixel(1,0,(p))  
        display.drawPixel(1,1,(p))  
        display.drawPixel(1,2,(p))  
        display.drawPixel(1,3,(p))
        display.flush()
        time.sleep_ms(400)
        
def line3():
    for x in rgbTable3:
        display.drawPixel(2,0,(x))  
        display.drawPixel(2,1,(x))  
        display.drawPixel(2,2,(x))  
        display.drawPixel(2,3,(x))
        display.flush()
        time.sleep_ms(400)
        
def line4():
    for y in rgbTable4:
        display.drawPixel(3,0,(y))  
        display.drawPixel(3,1,(y))  
        display.drawPixel(3,2,(y))  
        display.drawPixel(3,3,(y))
        display.flush()
        time.sleep_ms(400)

while True:#Loop forever & ever & ever & ever
    line1()
    line2()
    line3()
    line4()