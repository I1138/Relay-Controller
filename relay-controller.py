#!/usr/bin/python
#    <--8ch Relay Controller-->
#8-channel-relay control program/library V. 0.80 (Alpha rewrite). implemented in python.
#Created by Ian Bolin 12/19/15
#Updated by Ian Bolin 12/22/16
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
    #V. 0.80 (alpha rewrite)
#coming soon:
#   Relay on for time function
#   may include a near complete rewrite of the relay on/off functions
#   may eventually support relays with other configurations (num channels)



#Start of library code

#importing dependencies
import RPi.GPIO as GPIO

    """library designed to control an 8-channel-relay."""
    def __init__(self, arg):
        super(8-channel-relay, self).__init__()
        self.arg = arg
        GPIO.setmode(bcm)
        self.relay_setup()


    #IMPORTANT! relay_setup MUST BE CALLED FIRST, WITH A SET OF 8 VALUES, OTHERWISE THE PROGRAM WILL FAIL!!!

    # relay channels (gpio pins)
    def relay_setup(pins = [1,2,3,4,5,6,7,8]):
        pins = Channels
        #setup relay channels
        GPIO.setup(channels, GPIO.OUT, 1)
        #unpack channels
        channel1, channel2, channel3, channel4, channel5, channel6, channel7, channel8 = Channels

    # class variables
    channel1_state = False
    channel2_state = False
    channel3_state = False
    channel4_state = False
    channel5_state = False
    channel6_state = False
    channel7_state = False
    channel8_state = False
    #library functions

    #get relay state
    def channel_state(channel):
        if channel = 1:
            return channel1_state

        if channel = 2:
            return channel2_state

        if channel = 3:
            return channel3_state

        if channel = 4:
            return channel4_state

        if channel = 5:
            return channel5_state

        if channel = 6:
            return channel6_state

        if channel = 7:
            return channel7_state

        if channel = 8:
            return channel8_state

        else:
            print ("invalid argument for 'channel_state()' try 1,2, etc.")


    #user control on/off
    def ch_ctrl(ch):
        if ch = 1:
            GPIO.OUT(channel1, 0)
            channel1_state = True
            input(press enter to stop)
            GPIO.OUT(channel1, 1)
            channel1_state = False

        if ch = 2:
        	GPIO.OUT(channel2, 0)
            channel2_state = True
            input(press enter to stop)
            GPIO.OUT(channel2, 1)
            channel2_state = False

        if ch = 3:
        	GPIO.OUT(channel3, 0)
            channel3_state = True
            input(press enter to stop)
            GPIO.OUT(channel3, 1)
            channel3_state = False

        if ch = 4:
            GPIO.OUT(channel4, 0)
            channel4_state = True
            input(press enter to stop)
            GPIO.OUT(channel4, 1)
            channel4_state = False

        if ch = 5:
            GPIO.OUT(channel5, 0)
            channel5_state = True
            input(press enter to stop)
            GPIO.OUT(channel5, 1)
            channel5_state = False

        if ch = 6:
            GPIO.OUT(channel6, 0)
            channel6_state = True
            input(press enter to stop)
            GPIO.OUT(channel6, 1)
            channel6_state = False

        if ch = 7:
            GPIO.OUT(channel7, 0)
            channel7_state = True
            input(press enter to stop)
            GPIO.OUT(channel7, 1)
            channel7_state = False

        if ch = 8:
            GPIO.OUT(channel8, 0)
            channel8_state = True
            input(press enter to stop)
            GPIO.OUT(channel8, 1)
            channel8_state = False

        else:


        #turn off relays
    def ch_OFF(ch)
        if ch = 1:
            GPIO.OUT(channel1, 1)
            channel1_state = False

        if ch = 2:
            GPIO.OUT(channel2, 1)
            channel2_state = False

        if ch = 3:
            GPIO.OUT(channel3, 1)
            channel3_state = False

        if ch = 4:
            GPIO.OUT(channel4, 1)
            channel4_state = False

        if ch = 5:
            GPIO.OUT(channel5, 1)
            channel5_state = False

        if ch = 6:
            GPIO.OUT(channel6, 1)
            channel6_state = False

        if ch = 7:
            GPIO.OUT(channel7, 1)
            channel7_state = False

        if ch = 8:
            GPIO.OUT(channel8, 1)
            channel8_state = False

        else:

    #turn on relays
    def ch_ON(ch):
        if ch = 1:
            GPIO.OUT(channel1, 0)
            channel1_state = True

        if ch = 2:
            GPIO.OUT(channel2, 0)
            channel2_state = True

        if ch = 3:
            GPIO.OUT(channel3, 0)
            channel3_state = True

        if ch = 4:
            GPIO.OUT(channel4, 0)
            channel4_state = True

        if ch = 5:
            GPIO.OUT(channel5, 0)
            channel5_state = True

        if ch = 6:
            GPIO.OUT(channel6, 0)
            channel6_state = True

        if ch = 7:
            GPIO.OUT(channel7, 0)
            channel7_state = True

        if ch = 8:
            GPIO.OUT(channel8, 0)
            channel8_state = True

        else:
#End of library.
#This library designed and created by Ian Bolin on 12/19/15.
#V. 0.8 on 12/22/15
#V. 0.80 on 12/22/16
