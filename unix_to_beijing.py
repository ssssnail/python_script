import numpy
import datetime

def test():
    arr_unix_time = numpy.loadtxt(open("unix.csv", "rb"), delimiter=",", skiprows=0)
    for i in range(len(arr_unix_time)):
        unix_time = arr_unix_time[i]
        time = datetime.datetime.fromtimestamp(unix_time)
        print(time)
test()

