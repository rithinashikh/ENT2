class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.height = 0

    def print_stack(self):
        if self.top is None:
            print('empty stack')
        else:
            temp = self.top
            while temp is not None:
                print(temp.value)
                temp = temp.next

    def push(self, value):
        new_node = Node(value)
        if self.top is None:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1

    def pop(self):
        if self.height == 0:
            return None
        temp = self.top
        self.top = self.top.next
        temp.next = None
        self.height -= 1
        return temp


my_stack = Stack()

my_stack.push(5)
my_stack.push(6)
my_stack.push(8)
print('Original stack:')
my_stack.print_stack()
print('Height: ', my_stack.height)

print('\nAfter pop: ')
my_stack.pop()
my_stack.print_stack()
print('Height: ', my_stack.height)


