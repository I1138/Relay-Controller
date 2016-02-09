#!/usr/bin/python
#    <--8ch Relay Controller-->
#8-channel-relay control program/library V. 0.8 (Alpha). implemented in python. 
#Created by Ian Bolin 12/19/15
#DEPENDENCIES:
    #RPi.GPIO V. 1.0+

#supported functions:
    
    #relay_setup(pins)
        #sets up the GPIO pins as relay channels

    #relay_state(ch[channel number])
        #returns the state of a relay
    
    #ch[relay channel number]_ctrl()
        #turns the selected relay on until user input
    
    #ch[relay channel number]_ON()
        #turns a relay on indefinitely
        
    #ch[relay channel number]_OFF()
        #turns a relay off indefinitely

#change log:
    #V. 0.7 (pre-Alpha)
        #base library code
    #V. 0.8 (Alpha)
        #added documentation
        #added change log
        
#Next Up:
#   testing on Raspberry Pi (V. 0.9)
#   final Review before release (V. 1.0)



#coming soon:
#   *Relay on for time function (V. 2.0)
#   *V. 3.0 may include a near complete rewrite of the relay on/off functions
#   *may eventually support relays with other configurations



#Start of library code

#importing dependencies
import RPi.GPIO as GPIO

#set GPIO mode
GPIO.setmode(bcm)

#IMPORTANT! relay_setup MUST BE CALLED FIRST, WITH A SET OF 8 VALUES, OTHERWISE THE PROGRAM WILL FAIL!!!

# relay channels (gpio pins)
def relay_setup(pins):
    pins = Channels 
    #setup relay channels
    GPIO.setup(channels, GPIO.OUT, 1)
    #unpack channels
    channel1, channel2, channel3, channel4, channel5, channel6, channel7, channel8 = Channels

# variables
channel1_state = "undefined"
channel2_state = "undefined"
channel3_state = "undefined"
channel4_state = "undefined"
channel5_state = "undefined"
channel6_state = "undefined"
channel7_state = "undefined"
channel8_state = "undefined"
#library functions

#get relay state
def channel_state(channel):
    if channel = ch1:
        return channel1_state
        
    if channel = ch2:
        return channel2_state
        
    if channel = ch3:
        return channel3_state
        
    if channel = ch4:
        return channel4_state
        
    if channel = ch5:
        return channel5_state
        
    if channel = ch6:
        return channel6_state
        
    if channel = ch7:
        return channel7_state
        
    if channel = ch8:
        return channel8_state
        
    else:
        print ("invalid argument for 'channel_state()' try ch1 ch2 etc.")
        
        
#user control on/off
def ch1_ctrl():
    GPIO.OUT(channel1, 0)
    channel1_state = True
    input(press enter to stop)
    GPIO.OUT(channel1, 1)
    channel1_state = False
 
def ch2_ctrl():
	GPIO.OUT(channel2, 0)
    channel2_state = True
    input(press enter to stop)
    GPIO.OUT(channel2, 1)
    channel2_state = False
    
def ch3_ctrl():
	GPIO.OUT(channel3, 0)
    channel3_state = True
    input(press enter to stop)
    GPIO.OUT(channel3, 1)
    channel3_state = False

def ch4_ctrl():
    GPIO.OUT(channel4, 0)
    channel4_state = True
    input(press enter to stop)
    GPIO.OUT(channel4, 1)
    channel4_state = False
    
def ch5_ctrl():
    GPIO.OUT(channel5, 0)
    channel5_state = True
    input(press enter to stop)
    GPIO.OUT(channel5, 1)
    channel5_state = False
    
def ch6_ctrl():
    GPIO.OUT(channel6, 0)
    channel6_state = True
    input(press enter to stop)
    GPIO.OUT(channel6, 1)
    channel6_state = False
    
def ch7_ctrl():
    GPIO.OUT(channel7, 0)
    channel7_state = True
    input(press enter to stop)
    GPIO.OUT(channel7, 1)
    channel7_state = False
    
def ch8_ctrl():
    GPIO.OUT(channel8, 0)
    channel8_state = True
    input(press enter to stop)
    GPIO.OUT(channel8, 1)
    channel8_state = False


#turn off relays
def ch1_OFF():
    GPIO.OUT(channel1, 1)
    channel1_state = False
    
def ch2_OFF():
    GPIO.OUT(channel2, 1)
    channel2_state = False
    
def ch3_OFF():
    GPIO.OUT(channel3, 1)
    channel3_state = False
    
def ch4_OFF():
    GPIO.OUT(channel4, 1)
    channel4_state = False
    
def ch5_OFF():
    GPIO.OUT(channel5, 1)
    channel5_state = False
    
def ch6_OFF():
    GPIO.OUT(channel6, 1)
    channel6_state = False
    
def ch7_OFF():
    GPIO.OUT(channel7, 1)
    channel7_state = False
    
def ch8_OFF():
    GPIO.OUT(channel8, 1)
    channel8_state = False
    
    
#turn on relays
def ch1_ON():
    GPIO.OUT(channel1, 0)
    channel1_state = True
    
def ch2_ON():
    GPIO.OUT(channel2, 0)
    channel2_state = True
    
def ch3_ON():
    GPIO.OUT(channel3, 0)
    channel3_state = True
    
def ch4_ON():
    GPIO.OUT(channel4, 0)
    channel4_state = True
    
def ch5_ON():
    GPIO.OUT(channel5, 0)
    channel5_state = True
    
def ch6_ON():
    GPIO.OUT(channel6, 0)
    channel6_state = True
    
def ch7_ON():
    GPIO.OUT(channel7, 0)
    channel7_state = True
    
def ch8_ON():
    GPIO.OUT(channel8, 0)
    channel8_state = True
    
#End of library.
#This library designed and created by Ian Bolin on 12/19/15.
#V. 0.8 on 12/22/15
