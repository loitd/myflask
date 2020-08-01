import time

def exetime_decor(input_func):
    def inner(*args, **kwargs): #args or instance
        _startime = time.time() #Return the time in seconds
        _ret = input_func(*args, **kwargs) #do the things declared in the original func
        _endtime = time.time()
        print("[{0}] - {1} - {2} - Execution time: {3:.2f} secs".format(input_func.__name__, args, kwargs, _endtime-_startime)) #do additional things
        return _ret
    return inner

@exetime_decor
def hehe(name, age):
    print(name, age)
    pass