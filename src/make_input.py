
outfile = open('../LED/bin/Debug/plain.txt', 'w')
for line in open("outraw.txt"):
    if ',' in line:
        outfile.write(line.split(',')[0] + '\n')
    