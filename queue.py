
class Queue:

    def __init__(self, value = None):
        new_node = None if value is None else self.Node(value)
        self.first = new_node
        self.last = new_node
        self.lenght = 0 if value is None else 1
        pass

    class Node():

        def __init__(self, value, next = None):
            self.value = value
            self.next = next
            pass
        
    def get_first(self):
        if self.first is not None:
            print(f'First: {self.first.value}')
        else:
            print('Fila vazia!')

    def get_last(self):
        if self.last is not None:
            print(f'Last: {self.last.value}')
        else:
            print('Fila Vazia!')

    def get_length(self):
        print(f'Length: {self.lenght}')

    def print(self):
        current_node = self.first
        if current_node is None:
            print('Fila vazia!')
        else:
            while current_node is not None:
                print(current_node.value)
                current_node = current_node.next

    def enqueue(self, value):
        new_node = self.Node(value)
        if self.lenght == 0:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.lenght += 1
        pass

    def dequeue(self):

        if self.lenght == 0:
            return None
        temp = self.first

        if self.lenght == 1:
            self.first = None
            self.last = None
        else:       
            self.first = temp.next
            temp.next = None
        self.lenght -= 1
        return temp

if __name__ == '__main__':
    print('################################')
    queue = Queue(1)
    queue.get_first()
    queue.get_last()
    queue.get_length()
    queue.print()

    print('################################')
    queue.enqueue(3)
    queue.get_first()
    queue.get_last()
    queue.get_length()
    queue.print()

    print('################################')
    queue.enqueue(13)
    queue.get_first()
    queue.get_last()
    queue.get_length()
    queue.print()

    print('################################')
    queue.dequeue()
    queue.get_first()
    queue.get_last()
    queue.get_length()
    queue.print()
