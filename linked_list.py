
class LinkedList():

    def __init__(self, data = None):
        '''Construtor do objeto de lista linkada'''
        new_node = None if data is None else self.Node(data)
        self.head = new_node
        self.tail = new_node
        self.length = 0 if data is None else 1
        pass

    class Node():

        def __init__(self, data = None, next = None):
            '''Construtor do Nó'''
            self.data = data
            self.next = next
            pass
    
    def get_head(self):
        if self.head is None or self.head.data is None:
            print('Lista vazia!')
        else:
            print('Head:', self.head.data)
        pass

    def get_tail(self):
        if self.tail is None or self.tail.data is None:
            print('Lista vazia!')
        else:
            print('Tail:', self.tail.data)
        pass

    def get_lenght(self):
        print('Lenght:', self.length)
        pass

    def print(self):
        '''Percorre a lista, demostrando todos, enquanto existir informação.'''
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next
        pass

    def get(self, index):
        '''Percorre a lista a fim de retornar um index selecionado.'''
        
        # Se o index recebido esta fora do intervalo, retorna vazio.
        if index < 0 or index >= self.length:
            return None
        
        # Percorre a lista ate o index solicitado.
        current_node = self.head
        for i in range(0, index):
            current_node = current_node.next

        return current_node

    def append(self, data):
        '''Adiciona um elemento no fim da lista.'''

        new_node = self.Node(data)
        # Se lista estiver vazia, novo Nó assume Cabeça e Calda
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        # Se não, vincula o antigo nó calda, ao novo nó,
        # e o define como nó calda
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        pass

    def prepend(self, data):
        ''' Adiciona um elemento no inicio da lista.'''

        new_node = self.Node(data)
        # Se lista estiver vazia, novo Nó assume Cabeça e Calda
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        # Se não, vincula o antigo nó cabeça, ao novo nó,
        # e o define como nó cabeça
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        pass

    def insert(self, index, data):
        '''Insere registro no index recebido.'''

        if index < 0 or index > self.length:
            return False
        if index == 0:
            self.prepend(data)
            return True
        if index == self.length:
            self.append(data)
            return True
        
        new_node = self.Node(data)
        temp = self.get(index-1)

        new_node.next = temp.next
        temp.next = new_node
        self.length += 1

        return True

    def set(self, index, data):
        '''Atualiza valor do Nó com base no index.'''

        temp = self.get(index)
        if temp != None:
            temp.data = data
            return True
        else:
            return False

    def remove_first(self):
        '''Remove o primeiro item da lista.'''

        # Se lista esta vazia, retorna vazio
        if self.length == 0:
            return None
        
        # Puxa o valor após ao nó cabeça para substituir
        # o nó cabeça atual, salvando-o antes para retorno
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1

        # Se após remoção, lista ficou vazia, define 
        # nó cabeça e nó calda como vazio
        if self.length == 0:
            self.head = None
            self.tail = None

        return temp

    def remove_last(self):
        '''
            Percorre a lista até encontrar o Nó anterior a calda,
            define esse Nó como calda e retorna o nó removido.
        '''

        # Se a lista é vazia, retorna None
        if self.length == 0:
            return None
        # Se existe apenas um registro, a lista ficará vazia,
        # define nó cabeça e Nó calda como vazio, evitando
        # percorrer toda lista
        elif self.length == 1:
            temp = self.head
            self.head = None
            self.tail = None
            return temp
        
        # A partir do nó cabeça, percorre a lista para encontrar o nó
        # anterior a calda
        pre_tail = self.head
        while pre_tail.next != self.tail:
            pre_tail = pre_tail.next

        # Salva o nó calda atual em uma variavel para retorno,
        # define o nó anterior a calda, como calda, e retira o
        # vinculo com o nó que foi removido
        temp = self.tail
        self.tail = pre_tail
        self.tail.next = None
        self.length -= 1

        return temp

    def remove(self, index):
        '''Remove um nó de acordo com index.'''

        # Se o index passado esta fora do intervalo, retorna vazio
        if index < 0 or index >= self.length:
            return None
        # Se esta no começo ou no fim da lista, utiliza as funções ja criadas
        if index == 0:
            return self.remove_first()
        if index == self.length-1:
            return self.remove_last()
        
        # Busca o Nó anterior ao que sera removido, e guarda o que sera,
        # a fim de retorno. Vincula o Nó anterior com o proximo, removendo
        # o vinculo com o solicitado.
        pre_remove = self.get(index-1)
        temp = pre_remove.next
        pre_remove.next = temp.next
        temp.next = None
        self.length -= 1

        return temp

if __name__ == '__main__':
    print('################################')
    list = LinkedList('elemento 1')
    list.get_head()
    list.get_tail()
    list.get_lenght()
    list.print()

    print('################################')
    list.append('elemento 2')
    list.get_head()
    list.get_tail()
    list.get_lenght()
    list.print()

    print('################################')
    list.append('elemento 3')
    list.get_head()
    list.get_tail()
    list.get_lenght()
    list.print()

    print('################################')
    print(list.remove_last().data)
    list.get_head()
    list.get_tail()
    list.get_lenght()
    list.print()

    print('################################')
    list.prepend('elemento 0')
    list.get_head()
    list.get_tail()
    list.get_lenght()
    list.print()

    print('################################')
    print(list.remove_first().data)
    list.get_head()
    list.get_tail()
    list.get_lenght()
    list.print()

    print('################################')
    print(list.get(1))

    print('################################')
    print(list.insert(2, 'elemento 2.5'))
    list.get_head()
    list.get_tail()
    list.get_lenght()
    list.print()

    print('################################')
    print(list.set(0, 'elemento 0.5'))
    list.get_head()
    list.get_tail()
    list.get_lenght()
    list.print()

    print('################################')
    print(list.remove(2))
    list.get_head()
    list.get_tail()
    list.get_lenght()
    list.print()
