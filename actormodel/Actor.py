import queue, time
from abc import ABC, abstractmethod
from threading import Thread


class Actor(Thread):
    def __init__(self):
        self.mailbox = queue.Queue()
        self.address = lambda message: self.mailbox.put(message)
        super(Actor, self).__init__()
        self.start()
    
    def getAddress(self):
        return lambda message: self.mailbox.put(message)
    
    def run(self):
        while (True):
            message = self.mailbox.get()
            if message != None:
                self.handleMessage(message)
                if message.messageType == "kill":
                    break
            else:
                time.sleep(0.01)
    
    @abstractmethod
    def handleMessage(self, message):
        pass