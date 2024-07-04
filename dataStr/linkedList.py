class Node:
    ## NODE CONSTRUCTOR HERE ##
    def __init__(self, value):
        self.value = value
        self.next = None

    #                               #
    #                               #
    #                               #
    #################################
        
class LinkedList:
    ## CONSTRUCTORS HERE ##
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def appendLast(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
    
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node

        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop(self):
        if self.head is None:
            return None
        temp = self.head
        pre = self.head
        while(temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length-=1

        if self.length == 0:
            self.head = None
            self.tail = None

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length-=1
        if self.length == 0:
            self.tail = None
        return temp
        
    def get(self,index):
        if index < 0 or index >= self.length:
            return None

        temp = self.head
        for i in range(index):
            temp=temp.next
        return temp.value

    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self,index,value):
        new_node = Node(value)
        if index < 0 or index >= self.length+1:
            return False
        
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.appendLast(value)
        temp = self.head
        for i in range(index-1):
            temp = temp.next
        new_node.next = temp.next
        temp.next = new_node
        self.length+=1
        return True
        
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index ==0:
            return self.pop_first()
        if index == self.length-1:
            return self.pop()
        
        prev = self.get(index-1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        bfortemp = None
        afterTemp = temp.next
        for i in range(self.length):
            afterTemp = temp.next
            temp.next = bfortemp
            bfortemp = temp
            temp = afterTemp
    #                             #
    #                             #
    #                             #
    #                             #
    ###############################



 
my_linked_list = LinkedList(4)

for i in range(6):
    my_linked_list.appendLast(i)
