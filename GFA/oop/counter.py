class Counter:

    def __init__(self, *counter):
        if len(counter) == 1:
            self.counter = counter[0]
            self.COUNTER = counter[0]
        else:
            self.COUNTER = 0
            self.counter = 0

    def add(self, *number):
        if number:
            self.counter += number[0]
        else:
            self.counter += 1

    def get(self):
        return self.counter

    def reset(self):
        self.counter = self.COUNTER


obj_no = Counter()
obj_with = Counter(2)

print(obj_no.counter)
print(obj_with.counter)
