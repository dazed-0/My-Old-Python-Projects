class Node:
    def __init__(self, ND):
        self.__NodeData = ND #Storing Node Data
        self.__LeftNode = None
        self.__RightNode = None
    
    def GetData(self):
        return self.__NodeData
    
    def GetLeft(self):
        return self.__LeftNode
    
    def GetRight(self):
        return self.__RightNode
    
    def SetLeft(self, L):
        self.__LeftNode = L
    
    def SetRight(self, R):
        self.__RightNode = R

Node1 = Node(10)
Node2 = Node(20)
Node3 = Node(5)
Node4 = Node(15)
Node5 = Node(7)

class Tree:

    def __init__(self, FN):
        self.__FirstNode = FN #Stores the First Node

    def GetRootNode(self):
        return self.__FirstNode
    
    def Insert(self, IN):
        flag = False
        self.__InsertNode = IN
        CurrentNode = self.__FirstNode
        while flag == False:
            if CurrentNode.GetData() > self.__InsertNode.GetData():
                if CurrentNode.GetLeft() != None:
                    CurrentNode = CurrentNode.GetLeft()
                else:
                    CurrentNode.SetLeft(self.__InsertNode)
                    flag = True

            else:
                if CurrentNode.GetRight() != None:
                    CurrentNode = CurrentNode.GetRight()
                else:
                    CurrentNode.SetRight(self.__InsertNode)
                    flag = True

Tree1 = Tree(Node1)

Tree1.Insert(Node2)
Tree1.Insert(Node3)
Tree1.Insert(Node4)
Tree1.Insert(Node5)

def OutputInOrder(N):
    Node = N
    if Node.GetLeft() != None:
        OutputInOrder(Node.GetLeft())
    
    print(Node.GetData())
    
    if Node.GetRight() != None:
        OutputInOrder(Node.GetRight())

OutputInOrder(Node1)