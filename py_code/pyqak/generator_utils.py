from statistics import mean


def clip(stream, clip_low=0, clip_high=200):
    for val in stream:
        if val < clip_low:
            clipped = clip_low
        elif val > clip_high:
            clipped = clip_high
        else:
            clipped = val
        yield clipped


def avg_window(stream, window_size=4):
    buff = []
    for val in stream:
        if len(buff) == window_size:
            mu = mean(buff)
            buff = []
            yield mu
        else:
            buff.append(val)
