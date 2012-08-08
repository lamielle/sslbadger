from ctypes import *
user32 = windll.user32

# START SENDINPUT TYPE DECLARATIONS
PUL = POINTER(c_ulong)
class KeyBdInput(Structure):
    _fields_ = [("wVk", c_ushort),
             ("wScan", c_ushort),
             ("dwFlags", c_ulong),
             ("time", c_ulong),
             ("dwExtraInfo", PUL)]

class HardwareInput(Structure):
    _fields_ = [("uMsg", c_ulong),
             ("wParamL", c_short),
             ("wParamH", c_ushort)]

class MouseInput(Structure):
    _fields_ = [("dx", c_long),
             ("dy", c_long),
             ("mouseData", c_ulong),
             ("dwFlags", c_ulong),
             ("time",c_ulong),
             ("dwExtraInfo", PUL)]

class Input_I(Union):
    _fields_ = [("ki", KeyBdInput),
              ("mi", MouseInput),
              ("hi", HardwareInput)]

class Input(Structure):
    _fields_ = [("type", c_ulong),
             ("ii", Input_I)]

# END SENDINPUT TYPE DECLARATIONS
##
##FInputs = Input * 2
##extra = c_ulong(0)
##
##click = Input_I()
##click.mi = MouseInput(0, 0, 0, 2, 0, pointer(extra))
##release = Input_I()
##release.mi = MouseInput(0, 0, 0, 4, 0, pointer(extra))
##
##x = FInputs( (0, click), (0, release) )
##import time
##time.sleep(3)
##print "Clicking!"
##print user32.SendInput(2, pointer(x), sizeof(x[0]))
##
##Keypresses = Input * 2
##keydown = Input_I()
##keydown.type = 0x1
##keydown.ki = KeyBdInput(0x41, 0, 0, 0, pointer(extra))
##keyup = Input_I()
##keyup.type = 0x1
##keyup.ki = KeyBdInput(0x41, 0, 0x0002, 0, pointer(extra))
##y = Keypresses((0,keydown), (0, keyup))
##print "Keypress!"
##print user32.SendInput(2, pointer(y), sizeof(y[0]))

import time
for i in xrange(1,11):
    time.sleep(1)
    print i
FInputs = Input * 1
extra = c_ulong(0)
ii_ = Input_I()
ii_.ki = KeyBdInput( 0x9, 0x48, 0, 0, pointer(extra) )
x = FInputs( ( 1, ii_ ) )
print sizeof(x[0])
print windll.user32.SendInput(1, pointer(x), sizeof(x[0]))
print "err",windll.kernel32.GetLastError()

FInputs = Input * 1
extra = c_ulong(0)
ii_ = Input_I()
ii_.ki = KeyBdInput( 0xD, 0x48, 0, 0, pointer(extra) )
x = FInputs( ( 1, ii_ ) )
print sizeof(x[0])
print windll.user32.SendInput(1, pointer(x), sizeof(x[0]))
print "err",windll.kernel32.GetLastError()

#"wVk"
#"wScan"
#"dwFlags"
#"time"
#"dwExtraInfo"
#
#   INPUT input;
#   input.type = INPUT_KEYBOARD;
#   input.ki.wScan = KEYEVENTF_SCANCODE;
#   input.ki.dwExtraInfo = GetMessageExtraInfo();
#   input.ki.wVk = vk;
#   input.ki.dwFlags = 0;
#   if (keyUp) {
#      input.ki.dwFlags = KEYEVENTF_KEYUP;
#   }
#   input.ki.wVk = vk;
