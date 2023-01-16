import queue

queue = queue.Queue()

queue.put(12)
queue.put(52)
queue.put(44)

print(queue.get())
print(queue.qsize())
print(queue.get())
print(queue.qsize())
print(queue.get())
print(queue.qsize())