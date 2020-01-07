def average(data, windowsize):
    s = 0
    for n in range(windowsize):
        s = s + data[n]['close']
    return (s/float(windowsize))
