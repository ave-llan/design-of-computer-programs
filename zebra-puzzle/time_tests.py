import time

def timedcall(fn, *args):
    t0 = time.clock()
    result = fn(*args)
    t1 = time.clock()
    return t1-t0, result


def timedcalls(n, fn, *args):
    "Call function n times wtih args; return the min, avg, and max time."
    times = [timedcall(fn, *args)[0] for _ in range(n)]
    return min(times), average(times), max(times)

def average(numbers):
    "Return the average (arithmetic mean) of a sequence of numbers."
    return sum(numbers) / float(len(numbers))

