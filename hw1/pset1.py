#!/user/bin/bash/env/Python

import urllib
import csv
import matplotlib.pyplot as plt
import numpy as np

def homework1_problem1():

    def mean(lst):
        return float(sum(lst)) / len(lst)

    path = "https://www.dartmouth.edu/~chance/teaching_aids/data/golf.txt"

    data = {}

    f = urllib.urlopen(path)
    titles = f.readline().split()
    for line in f:
        new = line.split()
        for i in range(4):
            data[titles[i]] = data.get(titles[i], []) + [new[i]]
    f.close()

    data[titles[2]] = map(float, data[titles[2]])
    data[titles[3]] = map(int, data[titles[3]])

    print data[titles[2]]
    print data[titles[3]]

    avgGOLFHANDI = mean (data[titles[2]])
    avgSTOCKRATE = mean (data[titles[3]])

    print "average golf handicap is ", avgGOLFHANDI
    print "average stock rate is ", avgSTOCKRATE

    # references
    # https://stackoverflow.com/questions/1393324/in-python-given-a-url-to-a-text-file-what-is-the-simplest-way-to-read-the-cont
    # https://stackoverflow.com/questions/30627937/traceback-attributeerroraddinfourl-instance-has-no-attribute-exit/30628128
    # https://stackoverflow.com/questions/7368789/convert-all-strings-in-a-list-to-int

def homework1_problem2():

    def readCSVColumn(name, column):
        with open(name, 'rb') as f:
            reader = csv.reader(f)
            titles = reader.next()
            index = 0
            for i in range(len(titles)):
                if titles[i] == column:
                    index = i
            data = []
            try:
                for row in reader:
                    data.append(float(row[index]))
            except csv.Error as e:
                sys.exit('file %s, line %d: %s' % (filename, reader.line_num, e))

            f.close()
            return data

    def hist(data):
        _ = plt.hist(data, bins=range(-4,24,2), range=(-4,24), normed=1)
        _ = plt.xlabel('duration of birth (hours)')
        _ = plt.ylabel('density (fraction of births)')
        _ = plt.title('STAT111 Q1: Density of Child Birth Durations')
        plt.show()

    data = readCSVColumn("births.csv", "time")
    hist(data)

    # references
    # https://docs.python.org/2/library/csv.
    # https://stackoverflow.com/questions/9141732/how-does-numpy-histogram-work

def main():
    homework1_problem1()
    homework1_problem2()

if __name__ == "__main__":
    main()
