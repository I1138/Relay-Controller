//import modules
import Relay-Controller as relay
import time

// setup relay
relay.relay-setup(1,2,3,4,5,6,7,8)

// loop to cycle ch3 every second
while true:
  ch3_ON()
  print(relay_state(ch3))
  time.sleep(1)
  ch3_OFF()
  print(relay_state(ch3))
  time.sleep(1)

