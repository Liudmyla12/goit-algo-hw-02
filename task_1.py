from queue import Queue
import itertools
import random
import time
queue = Queue()
counter = itertools.count(1)


def generate_request():
    request_id = next(counter)
    queue.put(request_id)
    print(f"Заявка #{request_id} додана до черги")


def process_request():
    if not queue.empty():
        request = queue.get()
        print(f"Обробляється заявка #{request}")
        time.sleep(0.3)
        print(f"Заявка #{request} оброблена")
    else:
        print("Черга порожня")


if __name__ == "__main__":
    try:
        while True:
            generate_request()
            process_request()
            time.sleep(1)
            print("-" * 30)
    except KeyboardInterrupt:
        print("Роботу завершено")

