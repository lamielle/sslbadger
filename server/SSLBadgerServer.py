import SimpleHTTPServer
import SocketServer

from ctypes import *
import time

##################################################
# ctypes type declarations for using SendInput
#
PtrULong = POINTER(c_ulong)
class KeyboardInput(Structure):
    _fields_ = [("wVk", c_ushort),
                ("wScan", c_ushort),
                ("dwFlags", c_ulong),
                ("time", c_ulong),
                ("dwExtraInfo", PtrULong)]

class HardwareInput(Structure):
    _fields_ = [("uMsg", c_ulong),
                ("wParamL", c_short),
                ("wParamH", c_ushort)]

class MouseInput(Structure):
    _fields_ = [("dx", c_long),
                ("dy", c_long),
                ("mouseData", c_ulong),
                ("dwFlags", c_ulong),
                ("time", c_ulong),
                ("dwExtraInfo", PtrULong)]

class InputUnion(Union):
    _fields_ = [("ki", KeyboardInput),
                ("mi", MouseInput),
                ("hi", HardwareInput)]

class Input(Structure):
    _fields_ = [("type", c_ulong),
                ("ii", InputUnion)]
#
##################################################

# Use SendInput to send a input event with the given keycode
def SendKey(key):
   InputsArray1 = Input * 1
   nullULong = c_ulong(0)
   keyInput = InputUnion()
   keyInput.ki = KeyboardInput(key, 0x48, 0, 0, pointer(nullULong))

   # One input instance in the array of type 1 (keyboard)
   inputsArray = InputsArray1((1,keyInput))
   numSent = windll.user32.SendInput(1, # 1 input event
                                     pointer(inputsArray),
                                     sizeof(inputsArray[0]))
   if numSent != 1:
      print "SendInput result:", numSent
      print "SentInput error:", windll.kernel32.GetLastError()

class SSLBadgerServer(SimpleHTTPServer.SimpleHTTPRequestHandler):
   def do_GET(self):
      if self.path=='/sendTabEnter':
         self.send_response(200)
         self.end_headers()
         self.wfile.write("OK") #call sample function here
         time.sleep(5)
         # Send tab then enter
         SendKey(0x9)
         SendKey(0xD)
      else:
         self.send_response(404)
         self.end_headers()
         self.wfile.write("Not Found")

if __name__ == '__main__':
   PORT = 9999
   httpd = SocketServer.TCPServer(("", PORT), SSLBadgerServer)

   print "serving at port", PORT
   httpd.serve_forever()
