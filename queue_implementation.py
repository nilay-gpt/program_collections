"""
Queue functioning as Stack.
"""

class QueueFunction():

    def __init__(self):
        self.enque_list = list()


    def enque(self, item):
        # inserts in the starting postion
        self.enque_list = [item] + self.enque_list

    def deque(self):
        # pops from the starting postion
        if self.enque_list:
            self.enque_list.pop(0)
        else:
            print "Empty list, nothing to deque."


if __name__ == "__main__":
    obj = QueueFunction()

    while True:
        user_input = int(raw_input("Chose one option: 1>Enque \n 2>Deque \n 3>Stop\n"))
        if user_input == 1:
            _input = raw_input("Enter the value:")
            obj.enque(_input)
            print obj.enque_list
        elif user_input == 2:
            obj.deque()
            print obj.enque_list
        elif user_input == 3:
            print  "The Final output is:", obj.enque_list
            exit()
        else:
            print "Chose a valid option"
