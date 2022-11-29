from time import time

class KeyMemory:
    def __init__(self):
        self.key = None
        self.prekey = None
        self.time = None
        self.pretime = None
    def add_key_and_time(self,key,time):
        self.prekey = self.key
        self.key = key
        self.pretime = self.time
        self.time = time
    def get_time_gap(self):
        if self.pretime :
            return self.time - self.pretime
    def is_same_key(self):
        if self.prekey:
            if self.key == self.prekey:
                return True
            else:
                return False
