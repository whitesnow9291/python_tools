import time
import multiprocessing


ret = []

def funtion1(queue, sec = 1):
    time.sleep(sec)
    ret = queue.get()
    ret.append(sec)
    queue.put(ret)

def funtion2(id = 1):
    time.sleep(1)
    return id
    
def use_process():
    start = time.perf_counter()
    
    processes = []
    queue = multiprocessing.Queue()
    queue.put([3])
    for i in range(0, 10):
        p = multiprocessing.Process(target=funtion1, args=(queue, 1,))
        p.start()
        processes.append(p) 
    for p in processes:
        p.join()
    end = time.perf_counter()

    print(queue.get())  # Prints {"foo": True}

    print(f'Finished in {round(end-start, 2)} second(s)') 
    
def use_pool():
    start = time.perf_counter()
    p = multiprocessing.Pool(multiprocessing.cpu_count())
    result = p.map(funtion2, range(10))
    end = time.perf_counter()

    print(result)  # Prints {"foo": True}

    print(f'Finished in {round(end-start, 2)} second(s)') 
if __name__ == "__main__":
    params = [(keyword, 'location_name', 'language_code', 'domain') for keyword in ['1','2']]
    print(params)

    # use_pool()