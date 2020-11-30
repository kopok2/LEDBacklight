f= open("output/output_"+str(int(open("expcount.txt", "r").read())+1)+".csv", "r").read().split("\n")

series_length = 50
output = open("output/series_"+str(int(open("expcount.txt", "r").read())+1)+".csv", "w")
for x in range(series_length):
    output.write("t_minus"+str(-(x-series_length))+", ")
output.write("avedif, change\n")
for x in range(f.__len__()-series_length):
    series = []
    sum = 0
    for y in range(series_length):
        series.append(int(f[x+y].split(",")[0]))
        sum+= int(f[x+y].split(",")[0])
    averaged = ((sum/series_length) - int(f[x+series_length-1].split(",")[0]))
    
    state = False
    for y in range(series_length-1):
        if (f[x+series_length-y-1].split(",")[1] != f[x+series_length-y-2].split(",")[1]):
            state = True
    
    #series.append(f[x+series_length-1].split(",")[1])
    output.write(str(series).replace("[", "]").replace("]", "").replace("'", ""))
    output.write(", ")
    output.write(str(abs(averaged))+", ")
    output.write(str(state))
    
    output.write("\n")