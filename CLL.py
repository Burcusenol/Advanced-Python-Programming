class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
               
        
class CLL:
    def __init__(self):
        self.head=None
        self.tail=None
        
    
    
#Insertion at Start of CLL
    def atStart(self,data):
        newNode=Node(data)
        if self.head==None:
            self.head=newNode
            self.tail=newNode
        else:
            self.tail.next=newNode
            newNode.next=self.head
            self.head=newNode
   
   
#Insertion at End of CLL
    def atEnd(self,data):
        newNode=Node(data)
        if self.head==None:
            self.head=newNode
            self.tail=newNode
        else:
            self.tail.next=newNode
            self.tail=newNode
            self.tail.next=self.head  
            #self.head.next=self.tail  SCLL difference CLL   
   
#Insertion at Between of CLL
    def inBetween(self, middle_node, newdata):
        if middle_node is None:
            print('The Mentioned Note does not exist')
            return

        NewNode = Node(newdata)
        NewNode.next = middle_node.next
        middle_node.next = NewNode

 
#Deletion in CLL
    def deleteNode(self,location):
        ptr=self.head
        ptr1=None
        if ptr.data==location:
            ptr=ptr.next
            self.tail.next=ptr
            self.head=ptr
        else:
            while ptr.next.data !=location:
                ptr=ptr.next
                ptr1=ptr.next.next
        if ptr.next.data==self.tail.data:
            self.tail=ptr
            self.tail.next=self.head
        else:
            ptr.next=ptr1
        
        
        
    def listPrint(self):
        ptr=self.head
        while True:
            if ptr.data==self.tail.data:
                print(ptr.data)
                return
            else:
                print(ptr.data)
                ptr=ptr.next
        
list1=CLL()
list1.atStart(3)
list1.atStart(2)
list1.atEnd(6)
list1.atEnd(8)
list1.inBetween(list1.head.next,15)
list1.inBetween(list1.head.next.next,20)
list1.inBetween(list1.head.next.next.next.next,40)
list1.deleteNode(20)
list1.listPrint()
