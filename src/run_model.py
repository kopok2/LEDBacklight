# coding=utf-8
"""LED ML Model running pipeline."""
import statistics
import serial
import math
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


def log_response_1(values):
    val = -1.50597366
    coefs = [-0.41624938,  0.41212599, -0.04200694, -0.15245494,  0.19430454,  0.22582816,
   0.56097061,  0.0815576,   0.01920004,  0.49723097, -0.37569262,  0.12507564,
  -0.21171196, -0.87159269, -0.05628933,  0.35996005, -0.13784693, -0.5079509 ]
    for i, v in enumerate(values):
        val += coefs[i] * v
    return 1 / (1 + math.exp(-val))


def log_response_2(values):
    val = -4.16206442
    coefs = [-0.1676783976042788, -0.07490376386931438, 0.1679468741641528, 0.20543775361618735,
             0.17936835589663927, -0.4774662932996938, -0.6803555471988786, -0.13736468551300987, 0.3642389901822257,
             0.12545928823219152, -0.3393245258375251, 0.22316485676210265,
             0.48307983581723346, 0.258810779369491, -0.1365470275428234, 0.031131370067844766, 0.0008176580329774881, -1.043453152345807]
    for i, v in enumerate(values):
        val += coefs[i] * v
    return 1 / (1 + math.exp(-val))


log_response = [log_response_1, log_response_2]

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
            dec2 = log_response[int(state)](frames)
            print(dec, dec2, abs(dec - dec2))
            if dec > [0.5, 0.5][int(state)]:
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