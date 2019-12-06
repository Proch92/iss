from collections import deque
from statistics import stdev, mean
from math import fabs


def drop_outliers(stream, window_size=10, stdev_clipping=1.5):
    fifo_buffer = deque(maxlen=window_size)
    for val in stream:
        if len(fifo_buffer) == window_size:
            std = stdev(fifo_buffer)
            mu = mean(fifo_buffer)
            if fabs(mu - val) <= (std * stdev_clipping):
                fifo_buffer.append(val)
                yield val
        else:
            fifo_buffer.append(val)


def avg_window(stream, window_size=4):
    buff = []
    for val in stream:
        if len(buff) == window_size:
            mu = mean(buff)
            buff = []
            yield mu
        else:
            buff.append(val)
