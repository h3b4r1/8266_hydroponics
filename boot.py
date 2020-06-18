# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
import uos, machine
#uos.dupterm(None, 1) # disable REPL on UART(0)
import gc
#import webrepl
#webrepl.start()
gc.collect()
import network
from config import *

sta_if = network.WLAN(network.STA_IF)
sta_if.active(apstate)
sta_if.connect('apbssid','appass')
