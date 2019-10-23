

#implementing STACK DS with lists 

class Stack:
     def __init__(self):
         self.st = []

     def isEmpty(self):
         return self.st == []

     def push(self, item):
         self.st.append(item)

     def pop(self):
         return self.st.pop()

     def peek(self):
         return self.st[len(self.st)-1]

     def size(self):
         return len(self.st)

#implement STACK using linked lists
class Node:
    def __init__(self, data):
       self.data = data
       self.next = None
 
class stack:     #with lower s 
    def __init__(self):
        self.head = None
 
    def push(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
 
    def pop(self):
        if self.head is None:
            return None
        else:
            popped = self.head.data
            self.head = self.head.next
            return popped
#-----------------------------------------

#implementing queue using lists
class Queue:
    def __init__(self):
        self.qu = []

    def isEmpty(self):
        return self.qu == []

    def enqueue(self, item):
        self.qu.insert(0,item)

    def dequeue(self):
        return self.qu.pop()

    def size(self):
        return len(self.qu)

#implementing queue using linked list used the class pre-defined above
 
class queue:
    def __init__(self):
        self.head = None
        self.last = None
 
    def enqueue(self, data):
        if self.last is None:
            self.head = Node(data)
            self.last = self.head
        else:
            self.last.next = Node(data)
            self.last = self.last.next
 
    def dequeue(self):
        if self.head is None:
            return None
        else:
            to_return = self.head.data
            self.head = self.head.next
            return to_return
#------------------------------------------
#implementing a tree in most basic way

class node(object):  
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, obj):
        self.children.append(obj)
'''intercation with above class
n = node(5)
p = node(6)
q = node(7)
n.add_child(p)
n.add_child(q)
print(n.data)
for c in n.children:
    print(c.data)'''
#implementing graph with dicts 

class Graph:

    def __init__(self):
        self.graph_dict={}

    def addEdge(self,node,neighbour):  
        if node not in self.graph_dict:
            self.graph_dict[node]=[neighbour]
        else:
            self.graph_dict[node].append(neighbour)
            
    def show_edges(self):
        for node in self.graph_dict:
            for neighbour in self.graph_dict[node]:
                print("(",node,", ",neighbour,")")
'''adding nodes 
g= Graph()
g.addEdge('1', '2')
g.addEdge('1', '3')
g.addEdge('2', '3')
g.addEdge('2', '1')
g.addEdge('3', '1')
g.addEdge('3', '2')
g.show_edges()'''
#---------------------
#implementing DFS using recursion

def dfs(self, tree):
    if tree.root is None:
        return []
    visited, stack = [], [tree.root]
    while stack:
        node = stack.pop()
        visited.append(node)
        stack.extend(filter(None, [node.r, node.l]))  
        # append right first, so left will be popped first
    return visited
#-----------the END------------