from queue import Queue
from queue import LifoQueue

queue_object = Queue(10)
for i in range(4):
    queue_object.put(i)

while not queue_object.empty():
    print(queue_object.get())


life_queue = LifoQueue()
for i in range(4):
    life_queue.put(i)

while not life_queue.empty():
    print(life_queue.get())


from queue import PriorityQueue


class Job:
    def __init__(self, level, description):
        self.level = level
        self.description = description
        return

    def __lt__(self, other):
        return self.level < other.level


priority_queue = PriorityQueue()
priority_queue.put(Job(5, "中级别工作"))
priority_queue.put(Job(10, "低级别工作"))
priority_queue.put(Job(1, "重要工作"))
while not priority_queue.empty():
    next_job = priority_queue.get()
    print("开始工作：", next_job.description)
