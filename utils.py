import time

def meassure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()

        print("Time taken {} seconds".format(end_time - start_time))
        return result

    return wrapper