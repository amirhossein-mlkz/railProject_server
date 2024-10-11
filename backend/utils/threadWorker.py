import threading

class threadWorkers:

    def __init__(self, worker, thread):
        self.thread:threading.Thread = worker
        self.thread = thread
    
    def is_alive(self, ) -> bool:
        if self.thread is None:
            return False
        if self.thread.is_alive():
            return True
        return False
    
    def start(self,):
        self.thread.start()
