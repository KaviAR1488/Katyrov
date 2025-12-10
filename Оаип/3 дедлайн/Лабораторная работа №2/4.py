def my_range(start,end,step):
    current=start
    while current<end:
        yield current
        current+=step