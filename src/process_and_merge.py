with open('merged.csv', 'w') as outfile:
    from os import listdir
    from os.path import isfile, join
    mypath = 'output/'
    onlyfiles = [mypath + f for f in listdir(mypath) if isfile(join(mypath, f)) if 'series' in f]
    print(onlyfiles)
    state = False
    writen = False
    j = 0
    for file in onlyfiles:
        for line in open(file).readlines()[j:]:
            if 'False' in line and state and writen:
                state = False
                writen = False
                outfile.write(line.replace('False', '0'))
            elif 'False' in line:
                outfile.write(line.replace('False', '0'))
            elif 'True' in line and not state and not writen:
                state = True
                writen = True
                outfile.write(line.replace('True', '1'))
            else:
                outfile.write(line.replace('True', '1'))
        j = 1