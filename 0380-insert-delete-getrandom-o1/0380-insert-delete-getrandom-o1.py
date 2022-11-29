import random

class RandomizedSet:

    def __init__(self):
        self.set_ = set()

    def insert(self, val: int) -> bool:
        bool_ = False if val in self.set_ else True
        self.set_.add(val)
        return bool_

    def remove(self, val: int) -> bool:
        bool_ = True if val in self.set_ else False
        if bool_:
            self.set_.remove(val)
        return bool_

    def getRandom(self) -> int:
        return random.choice(list(self.set_))


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()