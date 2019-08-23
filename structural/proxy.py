import time


class Producer:
    """Very costly object"""

    def __init__(self, *args, **kwargs):
        time.sleep(2)
        print("producer initiated")

    def do_heavy_lifting(self):
        time.sleep(2)
        print("done heavy lifting")


class Proxy:
    def __init__(self):
        self.available = True
        self.producer = None

    def execute(self):
        if self.available:
            self.producer = Producer()
            self.producer.do_heavy_lifting()
        else:
            print("producer busy, try again later")


proxy = Proxy()

proxy.execute()

proxy.available = False

proxy.execute()
