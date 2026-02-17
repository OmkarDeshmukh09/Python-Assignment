import threading

# Shared variable
counter = 0

# Lock object
lock = threading.Lock()

def IncrementCounter():
    global counter
    
    for i in range(1000):   # Each thread increments 1000 times
        lock.acquire()
        counter += 1
        lock.release()

def main():

    threads = []

    # Create 5 threads
    for i in range(5):
        t = threading.Thread(target=IncrementCounter, name=f"Thread-{i+1}")
        threads.append(t)
        t.start()

    # Wait for all threads to complete
    for t in threads:
        t.join()

    print("Final value of counter is :", counter)


if __name__ == "__main__":
    main()
