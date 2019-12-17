import datetime

on = False
outfile = open("outchange.txt", "w")
while True:
    if input() == "n":
        break
    on = not on
    if not on:
        print("Butelka poza podswietlaczem")
        open('switch.txt', 'w').write('b')
    else:
        print("Butelka na podswietlaczu")
        open('switch.txt', 'w').write('a')
    out = str(datetime.datetime.now())+" "+str(on)
    outfile.write(out+"\n")
    print(out)