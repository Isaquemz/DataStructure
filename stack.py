
class Stack():

    def __init__(self, value = None, top = None):
        self.top = None if value is None else self.Node(value)
        self.height = 0 if value is None else 1
        pass

    class Node():
        
        def __init__(self, value, next = None):
            self.value = value
            self.next = next
            pass

    def get_top(self):
        if self.top is None:
            print('Pilha vazia!')
        else:
            print(f'Top: {self.top.value}')
    
    def get_height(self):
        print(f'Height: {self.height}')

    def print(self):
        current_node = self.top
        while current_node is not None:
            print(current_node.value)
            current_node = current_node.next
        pass

    def push(self, value):
        new_node = self.Node(value)
        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1
        pass

    def pop(self):

        if self.height == 0:
            return None
        
        temp = self.top
        self.top = temp.next
        temp.next = None
        self.height -= 1

        return temp

if __name__ == '__main__':
    stack = Stack()

    print("############################")
    stack.get_top()
    stack.get_height()
    stack.print()

    print("############################")
    stack.push(1)
    stack.get_top()
    stack.get_height()
    stack.print()

    print("############################")
    stack.push(10)
    stack.get_top()
    stack.get_height()
    stack.print()

    print("############################")
    stack.pop()
    stack.get_top()
    stack.get_height()
    stack.print()
