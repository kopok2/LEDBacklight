# coding=utf-8
"""LED ML Model running pipeline."""
import statistics
import serial
from collections import deque
from joblib import load
import numpy as np

state = False
BACK_RANGE = 15
j = 0
dec = 0
ser = serial.Serial()
ser.port = 'COM3'
try:
    ser.open()
except:
    ser.close()
    ser.open()
ser.baudrate = 512000


if __name__ == '__main__':
    clf_on = load('model1.joblib')
    clf_off = load('model2.joblib')
    clf = [clf_on, clf_off]
    decisions = deque()
    frame = deque()
    while True:
        val = int(str(ser.readline().strip()).replace("'", "").replace("b", ""))
        frame.append(val)
        print(decisions, j, sum(list(decisions)))
        if len(frame) > BACK_RANGE:
            frame.popleft()
            frames = list(frame) + [(frame[-1] - frame[0])] + [(frame[-1] - frame[7])] + [statistics.stdev(list(frame))]
            dec = clf[int(state)].predict_proba(np.array(frames).reshape(1, -1))[0][1]
            print(dec)
            if dec > [0.25, 0.35][int(state)]:
                print(1)
                decisions.append(1)
                if not j:
                    
                    
                    if not state:
                        print('TURNING ON')
                        j = 75
                        ser.write(bytes('a', encoding='utf-8'))
                        dec = 0
                        state = not state
                    elif state and sum(list(decisions)) > 0:
                        print('TURNING OFF')
                        j = 75
                        ser.write(bytes('b', encoding='utf-8'))
                        dec = 0
                        state = not state
            else:
                print(0)
                decisions.append(0)
            if j:
                j -= 1
            if len(decisions) > 30:
                decisions.popleft()