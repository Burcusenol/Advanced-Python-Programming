class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DLL:
    def __init__(self):
        self.head = None


# Appending to a DLL
    def append(self, newVal):
        newNode = Node(newVal)
        newNode.next = None
        if (self.head is None):
            newNode.prev = None
            return
        last=self.head
        while(last.next is not None):
            last=last.next
        last.next=newNode
        newNode.prev=last
        return
                
#Insertion at Start of DLL  
    def atStart(self,newVal):
        NewNode=Node(newVal)
        NewNode.next=self.head
        if self.head is not None:
            self.head.prev=Node
        self.head=NewNode   
            

#Insertion at Between of DLL  
    def inBetween(self,newVal,location):
        newNode=Node(newVal)
        ptr1=self.head
        ptr2=None
        while True:
            if ptr1.data==location:
                ptr2=ptr1.next
                ptr1.next=newNode
                newNode.prev=ptr1
                newNode.next=ptr2
                ptr2.prev=newNode
                return
            else:
                ptr1=ptr1.next
            
#Deletion from End of DLL
    def delEnd(self):
        ptr=self.head
        while ptr is not None:
            if ptr.next is None:
                ptr=ptr.prev
                ptr.next=None
                return
            else:
                ptr=ptr.next


#Deletion from Start of DLL
    def delStart(self):
        ptr=self.head
        ptr=ptr.next
        ptr.prev=None
        self.head=self.head.next   

#Deletion from Middle of DLL
    def delBetween(self,location):
        ptr1=self.head
        ptr2=None
        while True:
            if ptr1.next.data==location:
                ptr2=ptr1.next.next
                ptr1.next=ptr2
                ptr2.prev=ptr1
                return
            else:
                ptr1=ptr1.next
        
    
    def listprint(self):
        node=self.head
        while(node is not None):
            print(node.data)
            node=node.next
        
        
list1=DLL()
list1.atStart(10)
list1.atStart(15)
list1.append(23)
list1.append(40)
list1.append(50)
list1.inBetween(35,23)
list1.inBetween(12,15)
list1.delBetween(23)
list1.delEnd()
list1.delEnd()
list1.delStart()
list1.listprint()