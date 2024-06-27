
class BST():

    _default_node = object()

    def __init__(self, value = None):
        self.root = self.Node(value)
        pass

    class Node():

        def __init__(self, value, left = None, right = None):
            self.value = value
            self.left = left
            self.right = right
            pass

        def is_leaf(self):
            '''Verifica se é um nó folha, que não tem filhos.'''
            return self.left is None and self.right is None
        
        def get_value(self):
            try:
                return self.value
            except:
                return None

    def insert(self, value, node = None):

        if (self.root is None or self.root.value is None) and node is None:
            self.root = self.Node(value)
            return
        elif node is None:
            self.insert(value, self.root)
        
        if node is None:
            return
        
        new_node = self.Node(value)
        
        if value > node.value:
            if node.right is None:
                node.right = new_node
            else:
                self.insert(value, node.right)
        else:
            if node.left is None:
                node.left = new_node
            else:
                self.insert(value, node.left)

        pass

    def contains(self, value, node = _default_node):

        # Se não for passado valor e existe um valor raiz,
        # executa função recursivamente com valor raiz
        if node is self._default_node:
            if self.root.value is not None:
                return self.contains(value, self.root)
            else:
                node = None
        
        # Se Nó for vazio, retorna falso
        if node is None:
            return False
        
        # Se valor for igual ao valor do Nó, retorna verdadeiro
        elif value == node.value:
            return True
        
        # Se valor for menor ao valor do Nó, e nó da esquerda não for
        # vazio, chama recursivamente passando Nó da esquerda,
        # logicamente o menor valor.
        elif value < node.value:
            if node.left is not None:
                return self.contains(value, node.left)
        
        # Se não e Nó da direita não for vazio, chama recursivamente 
        # passando Nó da direita, logicamente o menor valor.
        else:
            if node.right is not None:
                return self.contains(value, node.right)
        
        return False

    def in_order(self, node = _default_node):
        '''
            E R D
            Esquerda / Raiz / Direita

            Percorre toda arvore, chegando ao valor mais a esquerda,
            voltando a raiz e depois a direita, assim buscando do menor
            ao maior valor
        '''

        # Se a chamada for sem um nó definido, ou seja,
        # primeira execução, faz chamada recursiva passando raiz
        if node is self._default_node:
            self.in_order(self.root)
            return

        # Se o nó passado tiver valor vazio, finaliza execução
        if node is None or node.value is None:
            return
        
        if node.left is not None:
            self.in_order(node.left) 
        else:
            self.in_order(self.Node(node.left))

        print(node.value)

        if node.right is not None:
            self.in_order(node.right) 
        else:
            self.in_order(self.Node(node.right))
        pass

    def min_value(self, current_node = _default_node):

        # Se não for passado um Nó, e a raiz não for vazia,
        # definimos a raiz como o no inicial
        if current_node is self._default_node:
            if self.root is not None:
                current_node = self.root

        # Caso o valor passado seja nulo, retorna nulo
        if current_node is None:
            return None

        # Percorre até o valor mais a esquerda, logicamente o valor menor
        while current_node.left is not None:
            current_node = current_node.left
        
        return current_node.value

    def delete_node(self, value, node = _default_node):

        if node is self._default_node:
            self.root = self.delete_node(value, self.root)
            return

        if node is None:
            return None
        
        if value < node.value:
            node.left = self.delete_node(value, node.left)
            return node
        elif value > node.value:
            node.right = self.delete_node(value, node.right)
            return node
        else:
            if node.is_leaf():
                return None
            elif node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                min_value = self.min_value(node.right)
                node.value = min_value
                node.right = self.delete_node(min_value, node.right)
                return node

    def get_value(self, node):
        if node is None:
            return None
        else:
            return node.get_value()

    def manual_check(self):
        '''Função a fim de uso para validação, verificando nivel a nivel. 4 niveis por padrão'''

        print(' ----- Nivel 1 --------')
        print('Raiz:', self.get_value(self.root))
        print(' ----- Nivel 2 --------')
        print('Esquerda da Raiz:', self.get_value(self.root.left))
        print('Direita da Raiz:', self.get_value(self.root.right))
        print(' ----- Nivel 3 --------')
        print('Esquerda da Esquerda da Raiz:', self.get_value(self.root.left.left))
        print('Direita da Esquerda da Raiz:', self.get_value(self.root.left.right))
        print('Esquerda da Direita da Raiz:', self.get_value(self.root.right.left))
        print('Direita da Direita da Raiz:', self.get_value(self.root.right.right))
        print(' ----- Nivel 4 --------')
        print('Esquerda da Esquerda da Esquerda da Raiz:', self.get_value(self.root.left.left.left))
        print('Direita da Esquerda da Esquerda da Raiz:', self.get_value(self.root.left.left.right))
        print('Esquerda da Direita da Esquerda da Raiz:', self.get_value(self.root.left.right.left))
        print('Direita da Direita da Esquerda da Raiz:', self.get_value(self.root.left.right.right))
        print('Esquerda da Esquerda da Direita da Raiz:', self.get_value(self.root.right.left.left))
        print('Direita da Esquerda da Direita da Raiz:', self.get_value(self.root.right.left.right))
        print('Esquerda da Direita da Direita da Raiz:', self.get_value(self.root.right.right.left))
        print('Direita da Direita da Direita da Raiz:', self.get_value(self.root.right.right.right))

    pass

if __name__ == '__main__':

    tree = BST()
    
    tree.insert(50)
    tree.insert(17)
    tree.insert(72)
    tree.insert(12)
    tree.insert(23)
    tree.insert(54)
    tree.insert(76)
    tree.insert(9)
    tree.insert(14)
    tree.insert(19)
    tree.insert(67)
    
    print('# ------------------ IN ORDER --------------- #')
    tree.in_order()

    print('# ------------------ CONTAINS --------------- #')
    value = 1
    print(f'valor {value}: {tree.contains(value)}')
    value = 23
    print(f'valor {value}: {tree.contains(value)}')
    value = 9
    print(f'valor {value}: {tree.contains(value)}')
    value = 71
    print(f'valor {value}: {tree.contains(value)}')
    value = 67
    print(f'valor {value}: {tree.contains(value)}')

    print('# ----------------- MIN VALUE --------------- #')
    print('Minimo valor:', tree.min_value())
    print('Minimo valor a partir da direita da Raiz:', tree.min_value(tree.root.right))

    print('# ----------- VERIFICAÇÃO MANUAL ------------ #')
    tree.manual_check()

    print('# ------------------- DELETE ---------------- #')
    tree.delete_node(50)

    print('# ------------------ IN ORDER --------------- #')
    tree.in_order()

    print('# ----------- VERIFICAÇÃO MANUAL ------------ #')
    tree.manual_check()
