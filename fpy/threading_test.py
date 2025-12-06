from threading import Thread


def task():
    print("线程1运行")


thread_one = Thread(target=task)

thread_one.run()


class MyThread(Thread):
    def __init__(self, num):
        super().__init__()
        self.name = "线程" + str(num)

    def run(self):
        message = self.name + "运行"
        print(message)


thread_two = MyThread(2)
thread_two.start()
