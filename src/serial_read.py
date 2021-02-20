import serial
import datetime

j = 0
last = ''
def state_char(t):
    global j
    global last
    if j:
        j -= 1
    last = '0' if not t and not j else ('1' if t == 'a' or last == '1' else '2')
    return last


ser = serial.Serial()
ser.port = 'COM3'
try:
    ser.open()
except:
    ser.close()
    print("NO")
    ser.open()
ser.baudrate = 512000
outfile = open("outraw.txt", "w")
outfile.write('val,target\n')
print("COM Port successfully opened")
while not open("killme.txt", "r").read() == "killme":
    t = open('switch.txt', 'r').read()
    out = str(ser.readline().strip()).replace("'", "").replace("b", "") + ", " + state_char(t)
    #print(out, t)
    
    
    if t:
        j = 30
        ser.write(bytes(t, encoding='utf-8'))
        open('switch.txt', 'w').write('')
    #print(out)
    outfile.write(out+"\n")