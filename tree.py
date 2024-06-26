
class Tree():

    def __init__(self, value = None):
        '''Construtor do objeto nó'''
        self.root = self.Node(value)
        pass

    class Node():

        def __init__(self, value, left = None, right = None):
            '''Construtor do objeto Node'''
            self.value = value
            self.left = left
            self.right = right

        def is_leaf(self):
            '''Verifica se é um nó folha, que não tem filhos.'''
            return self.left is None and self.right is None
    
        pass

    def insert(self, value):
        '''
            Função responsavel por inserir o Nó no lugar devido,
            de acordo com regra definida:

            Raiz / Esquerda / Direta

              - Se raiz esta vazia, adiciona na raiz;
              - Se esquerda esta vazia, adiciona na esquerda;
              - Se direita esta vazia, adiciona na direita.
        '''
        
        # Se a raiz esta vazia, adiciona o nó na raiz
        if self.root.value is None:
            self.root = self.Node(value)

        else:
            # Cria o objeto nó a ser inserido
            new_node = self.Node(value)
            
            # Insere valor da raiz na fila para ser
            # verificado segundo estrutura de arvore
            queue = []
            queue.append(self.root)

            # Percorre arvore para identificar local a ser inserido
            while len(queue) > 0:
                
                # Pega o proximo valor da fila, a ser verificado
                current_node = queue.pop(0)

                # Se lado esquerdo estiver vazio, aloco no lado esquerdo,
                # se não, adiciono a fila para ser verificado novamente
                if current_node.left is None:
                    current_node.left = new_node
                    break
                else:
                    queue.append(current_node.left)

                # Se lado direito estiver vazio, aloco no lado direito,
                # se não, adiciono a fila para ser verificado novamente
                if current_node.right is None:
                    current_node.right = new_node
                    break
                else:
                    queue.append(current_node.right)

                pass
        
        pass

    def pre_order(self, node = None):
        '''
            R E D
            Raiz / Esquerda / Direita

            Percorre a arvore demonstrando o valor raiz e percorrendo os proximos
            de acordo com a regra, esquerda enquanto houver, e posteriormente a direita.
        '''

        # Se a chamada for sem um nó definido, ou seja,
        # primeira execução, faz chamada recursiva passando raiz
        if node is None:
            self.pre_order(self.root)
            return

        # Se o nó passado tiver valor vazio, finaliza execução
        if node.value is None:
            return
        
        print(node.value)

        if node.left is not None:
            self.pre_order(node.left) 
        else:
            self.pre_order(self.Node(node.left))

        if node.right is not None:
            self.pre_order(node.right) 
        else:
            self.pre_order(self.Node(node.right))

    def in_order(self, node = None):
        '''
            E R D
            Esquerda / Raiz / Direita

            Percorre toda arvore, chegando ao valor mais a esquerda,
            voltando a raiz e depois a direita.
        '''

        # Se a chamada for sem um nó definido, ou seja,
        # primeira execução, faz chamada recursiva passando raiz
        if node is None:
            self.in_order(self.root)
            return

        # Se o nó passado tiver valor vazio, finaliza execução
        if node.value is None:
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

    def pos_order(self, node = None):
        '''
            E D R
            Esquerda / Direita / Raiz

            Percorre toda arvore, chegando ao valor mais a esquerda,
            indo para a direita e voltando para a raiz.
        '''

        # Se a chamada for sem um nó definido, ou seja,
        # primeira execução, faz chamada recursiva passando raiz
        if node is None:
            self.pos_order(self.root)
            return

        # Se o nó passado tiver valor vazio, finaliza execução
        if node.value is None:
            return
        
        if node.left is not None:
            self.pos_order(node.left) 
        else:
            self.pos_order(self.Node(node.left))

        if node.right is not None:
            self.pos_order(node.right) 
        else:
            self.pos_order(self.Node(node.right))

        print(node.value)

        pass

    def bfs(self):
        '''
            Percorre a arvore seguindo por niveis, demonstrando a mesma ordem de inserção.
        '''

        # Se o valor do nó raiz é None, significa que é uma arvore vazia
        if self.root.value is None:
            return
        
        # Adiciona valor raiz na lista para verificação
        queue = []
        queue.append(self.root)

        while len(queue) > 0:
            # Busca proximo valor para verificação
            node_current = queue.pop(0)

            # Se nó da esquerda tiver valor, adiciona na lista para verificar
            if node_current.left is not None:
                queue.append(node_current.left)

            # Se nó da direita tiver valor, adiciona na lista para verificar
            if node_current.right is not None:
                queue.append(node_current.right)

            # Printa valor atual
            print(node_current.value)

            pass

        pass

    pass

if __name__ == '__main__':

    tree = Tree()
    
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

    print('# ----------------- PRE ORDER --------------- #')
    tree.pre_order()
    print('# ------------------ IN ORDER --------------- #')
    tree.in_order()
    print('# ------------------ POS ORDER ---------------- #')
    tree.pos_order()
    print('# -------------------- BFS ------------------ #')
    tree.bfs()

    print('# ----------- VERIFICAÇÃO MANUAL ------------ #')
    print(' ----- Nivel 1 --------')
    print('Raiz: ', tree.root.value)
    print(' ----- Nivel 2 --------')
    print('Esquerda da Raiz: ', tree.root.left.value)
    print('Direita da Raiz: ', tree.root.right.value)
    print(' ----- Nivel 3 --------')
    print('Esquerda da Esquerda da Raiz: ', tree.root.left.left.value)
    print('Direita da Esquerda da Raiz: ', tree.root.left.right.value)
    print('Esquerda da Direita da Raiz: ', tree.root.right.left.value)
    print('Direita da Direita da Raiz: ', tree.root.right.right.value)
    print(' ----- Nivel 4 --------')
    print('Esquerda da Esquerda da Esquerda da Raiz: ', tree.root.left.left.left.value)
    print('Direita da Esquerda da Esquerda da Raiz: ', tree.root.left.left.right.value)
    print('Esquerda da Direita da Esquerda da Raiz: ', tree.root.left.right.left.value)
    print('Direita da Direita da Esquerda da Raiz: ', tree.root.left.right.right.value)
    print('Esquerda da Esquerda da Direita da Raiz: ', tree.root.right.left.left)
    print('Direita da Esquerda da Direita da Raiz: ', tree.root.right.left.right)
    print('Esquerda da Direita da Direita da Raiz: ', tree.root.right.right.left)
    print('Direita da Direita da Direita da Raiz: ', tree.root.right.right.right)
