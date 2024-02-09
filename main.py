import time
import threading


# def small(a: str):
#     b = []
#     for i in a:
#         if i.islower():
#             b.append(i)
#     print(*b)


def timezone(a: int):
    for i in range(1, a + 1):
        time.sleep(1)
        print(f"The number: {i}")


def time_latter(a: str):
    for i in a:
        time.sleep(1)
        print(f"The latter: {i}")


Thread1 = threading.Thread(target=time_latter("Ahmadjon"))  # noqa
Thread2 = threading.Thread(target=timezone(5))

Thread1.start()
Thread2.start()

Thread1.join()
Thread2.join()

print("All threads are stop")
