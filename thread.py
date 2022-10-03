import time
import multiprocessing


ret = []

def useless_function(queue, sec = 1):
    print(f'Sleeping for {sec} second(s)')
    time.sleep(sec)
    print(f'Done sleeping')
    
    ret = queue.get()
    ret.append(sec)
    queue.put(ret)
    
def main():
    start = time.perf_counter()
    
    queue = multiprocessing.Queue()
    queue.put(ret)

    process1 = multiprocessing.Process(target=useless_function, args=(queue, 2,))
    process2 = multiprocessing.Process(target=useless_function, args =(queue, 3))
    process1.start()
    process2.start()
    process1.join()
    process2.join()
    end = time.perf_counter()

    print(queue.get())  # Prints {"foo": True}

    print(f'Finished in {round(end-start, 2)} second(s)') 
if __name__ == "__main__":
    main()