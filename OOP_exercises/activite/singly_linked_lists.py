class Node:
    def __init__(self, value, next=None):
        self.data = value
        self.next = next


class SLL:
    def __init__(self):
        self.head = None

    def insertion(self):
        try:
            v = int(input('enter an integer: '))
            new = Node(v)

            if self.head is None:
                self.head = new
            else:
                last = self.head
                while last.next is not None:
                    last = last.next
                last.next = new
        except ValueError:
            print("you must enter an integer!!!")

    def __str__(self):
        try:
            last = self.head
            values = []
            while last.next is not None:
                values.append(last.data)
                last = last.next
            values.append(last.data)
            values.sort(reverse=True)
            for x in range(len(values)):
                print(values[x], end=" _|_ " if x != (len(values) - 1) else " |")
            return ""
        except AttributeError:
            pass

    def insertions(self):
        while True:
            self.insertion()
            q = input("are you done?\n==> Y / N: ")
            q = q.upper()
            if q == "Y":
                break
