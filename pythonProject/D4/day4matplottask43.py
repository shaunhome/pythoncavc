from matplotlib import pyplot as plt

infile = open("excell-datasets/gdp_info_this.csv")

for line in infile:
    print(line)

for line in infile:
    linevalues = line.rstrip().split(",")
    linelbl = linevalues[0]
    linevalues.pop(0)
    linevalues.reverse()
    for i in range(0, len(linevalues)):
        linevalues[i] = int(linevalues[i])
    print(linevalues)

infile.close()
# from pg 226 carry on