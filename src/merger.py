# coding=utf-8
"""Merge experiment files."""

from collections import deque
import statistics


DATA_PATH = 'outraw.txt'
CHANGED_PATH_1 = 'outraw1.csv'
CHANGED_PATH_2 = 'outraw2.csv'
BACK_RANGE = 15


if __name__ == '__main__':
    vals = open(DATA_PATH).readlines()
    frame = deque()
    outfile = open(CHANGED_PATH_1, 'w')
    outfile.write(",".join(['f_{0}'.format(x) for x in range(BACK_RANGE)]) + ",diff,diff2,std,target\n")
    for v in vals:
        frame.append(v.split(',')[0])
        if len(frame) > BACK_RANGE:
            frame.popleft()
            outfile.write(",".join([str(int(x)) for x in frame]) + "," + str((int(frame[-1]) - int(frame[0]))) + "," + str((int(frame[-1]) - int(frame[7]))) + "," +str(statistics.stdev([int(x) for x in list(frame)]))+ "," + str(1 if int(v.split(',')[1].strip()) == 1 else 0) + '\n')
    vals = open(DATA_PATH).readlines()
    frame = deque()
    outfile = open(CHANGED_PATH_2, 'w')
    outfile.write(",".join(['f_{0}'.format(x) for x in range(BACK_RANGE)]) + ",diff,diff2,std,target\n")
    for v in vals:
        frame.append(v.split(',')[0])
        if len(frame) > BACK_RANGE:
            frame.popleft()
            outfile.write(",".join([str(int(x)) for x in frame]) + "," + str((int(frame[-1]) - int(frame[0]))) + "," + str((int(frame[-1]) - int(frame[7]))) + "," +str(statistics.stdev([int(x) for x in list(frame)]))+ "," + str(int(v.split(',')[1].strip()) // 2) + '\n')
