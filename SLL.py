class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class SLL:
    def __init__(self):
        self.head = None

# Insertion at End of SLL
    def atEnd(self, newdata):
        NewNode = Node(newdata)
        if self.head is None:
            self.head = NewNode
            return

        tail = self.head
        while(tail.next):
            tail = tail.next
        tail.next = NewNode

# Insertion at Start of SLL
    def atStart(self, newdata):
        NewNode = Node(newdata)
        NewNode.next = self.head
        self.head = NewNode


# Insertion at Between of SLL
    def inBetween(self, middle_node, newdata):
        if middle_node is None:
            print('The Mentioned Note does not exist')
            return

        NewNode = Node(newdata)
        NewNode.next = middle_node.next
        middle_node.next = NewNode


# Deletion in SLL
    def deleteNode(self, removeData):
        Headval = self.head
        if(Headval is not None):
            if(Headval.data == removeData):
                self.head = Headval.next
                Headval = None
                return
        while(Headval is not None):
            if(Headval.data == removeData):
                break

            prev = Headval
            Headval = Headval.next

        if(Headval == None):
            return
        prev.next = Headval.next
        Headval = None


# Count No of Elements in SLL

    def getCount(self):
        tmp = self.head
        count = 0

        while(tmp):
            count += 1
            tmp = tmp.next
        return count

# Removing Duplicates from Unsorted SLL
    def remove_duplicates(self):
        ptr1 = None
        ptr2 = None
        dup = None
        ptr1 = self.head

        while(ptr1 != None and ptr1.next != None):
            ptr2 = ptr1
            while(ptr2.next != None):
                if(ptr1.data == ptr2.next.data):
                    dup = ptr2.next
                    ptr2.next = ptr2.next.next
                else:
                    ptr2 = ptr2.next
            ptr1 = ptr1.next

# Removing Duplicates from Sorted SLL
    def remove_from_sorted(self):
        temp = self.head
        if temp is None:
            return
        while temp.next is not None:
            if(temp.data == temp.next.data):
                new = temp.next.next
                temp.next = new
            else:
                temp = temp.next
        return self.head



# Removing Duplicates from Sorted SLL
    def remove_from_sorted2(self):
        if(self.head==None and self.head.next==None):
            return
        current=self.head
        while(current.next):
            if(current.data==current.next.data):
                current.next=current.next.next
            else:
                current=current.next
        return            
      
      
 #Swap Nodes in SLL
    def swapNodes(self,x,y):
        if x==y:
            return
        prevX=None
        currX=self.head
        while (currX !=None and currX.data!= x):
            prevX=currX
            currX=currX.next
        prevY=None
        currY=self.head
        while(currY!=None and currY.data!=y):
            prevY=currY
            currY=currY.next
        if currX==None or currY==None:
            return
        if prevX!=None:
            prevX.next=currY
        else:
            self.head=currY
        if prevY!=None:
            prevY.next=currX
        else:
            self.head=currX
            
            
        temp=currX.next
        currX.next=currY.next
        currY.next=temp      
      
                
    def listprint(self):
        output = self.head
        while output is not None:
            print(output.data)
            output = output.next





list1 = SLL()
list1.head = Node('Thurs')
e2 = Node('Mon')
e3 = Node('Mon')

list1.head.next = e2
e2.next = e3

list1.atEnd('Thurs')
list1.atEnd('Mon')
list1.atEnd('Thurs')
list1.atEnd("Fri")
list1.atEnd("Thurs")
list1.atStart('Sat')

list1.inBetween(list1.head, 'Sun')
list1.inBetween(list1.head.next, 'Sun')
list1.inBetween(list1.head.next.next, 'Sun')
list1.deleteNode('Sat')

#  count=list1.getCount()
#  print('Count Before Removing Duplicates=' , count)

#  list1.remove_duplicates()
#  count=list1.getCount()
#  print('Count After Removing Duplicates=' , count)


# list1.listprint()


list2 = SLL()
list2.head = Node(10)
e2 = Node(20)
e3 = Node(30)

list2.head.next = e2
e2.next = e3

#list2.atEnd(30)
list2.atEnd(40)
#list2.atEnd(40)
#list2.atEnd(50)
list2.atEnd(50)
list2.atEnd(60)


# list2.inBetween(list2.head,40)
# list2.inBetween(list2.head.next,50)
# list2.inBetween(list2.head.next.next,50)

# count = list2.getCount()
# print('Count Before Removing Duplicates=', count)

#list2.remove_duplicates()
#list2.remove_from_sorted()

#list2.remove_from_sorted2()
# count = list2.getCount()
# print('Count After Removing Duplicates=', count)

print('The SLL Before Swapping Nodes')
list2.listprint()
print('The SLL After Swapping Nodes')
list2.swapNodes(10,20)
list2.listprint()
