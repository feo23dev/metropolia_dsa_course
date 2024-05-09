class ListNode:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

    def __repr__(self):
        return f"<ListNode: {self.data}>"

class DoublyLinkedList:
    def __init__(self):
        self._head = self._tail = None;
        self._size = 0
    
    def __repr__(self):
        current_node = self._head
        values = ''
        while current_node:
            values += f', {current_node.data}'
            current_node = current_node.next
        plural = '' if self._size == 1 else 's'
        return f'<DoublyLinkedList ({self._size} element{plural}): [{values.lstrip(", ")}]>'
    
    def __len__(self):
        return self._size
    

    def insert(self,index,value):
        if index < 0 or index > self._size:
            raise ValueError("Index must be in bounds")
        
        current_node = self._head

        if index == 0:
            

            new_node = ListNode(value)
            self._head = new_node
            new_node.next = current_node
        elif index == self._size:
          
            current_node = self._tail
            new_node = ListNode(value)
            current_node.next = new_node
            new_node.prev = current_node
            
        else:
            for _ in range(index):
            
                current_node = current_node.next

            new_node = ListNode(value)
        
            prev_node = current_node.prev
            prev_node.next = new_node
            new_node.prev = prev_node
            new_node.next = current_node
            current_node.prev = new_node

        self._size +=1
        
       





        print(current_node)

    def remove(self,index):
        if index < 0 or index > self._size-1:
            
            raise(ValueError("Out of bounds!"))
           
        

        current_node = self._head
        if index == 0:
            next_node = current_node.next
            self._head = next_node
            
            self._size -= 1
            return current_node

        if index == self._size-1:
            
            current_node = self._tail
            prev = current_node.prev
            prev.next= None
            self._tail = prev
            self._size -= 1
            return current_node

        
        for _ in range(index):

            current_node= current_node.next
            
        
        prev = current_node.prev
        next = current_node.next
        prev.next = next
        next.prev = prev
        self._size -= 1
       
        return current_node



    def append(self,value):

        newNode = ListNode(value,next=None,prev=self._tail)

        if self._head is None:
            self._head = self._tail = newNode
        else:
            self._tail.next = newNode
            self._tail = newNode
        self._size +=1
            
    def pop(self):

        if not self._size:
            return None
        
        node_to_remove = self._tail
        previous_node = node_to_remove.prev
       
        if node_to_remove == self._head:
            self._head = None    
        else:
            previous_node.next = None

        self._tail = previous_node

        self._size -= 1

        value = node_to_remove.data
        del(node_to_remove)
        return value

class ListBasedQueue(DoublyLinkedList):
    def __init__(self):
        super().__init__()
    def __repr__(self):
        plural = '' if self._size == 1 else 's'
        values = ','.join([c for c in self])
        return f'<ListBasedQueue ({self._size} element{plural}): [{values}]'
    
    
    def enqueue(self, data):
        self.insert(0, data)



    def dequeue(self):
        return self.pop()




class SinglyLinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __repr__(self):
        current_node = self._head
        values = ''
        while current_node:
            values += f', {current_node.data}'
            current_node = current_node.next
        plural = '' if self._size == 1 else 's'
        return f'<SinglyLinkedList ({self._size} element{plural}): [{values.lstrip(", ")}]>'
    
    def __len__(self):
        return self._size;

    def append(self, value):
        """Append a value to the end of the list"""
        """ Returns none """

        node = ListNode(value)

        if self._head is None:
            self._head =self._tail= node

        else:
            """ Start from the head, and go to the last item so that we can append the node to the end of the list"""
            """ We need to start from the head, because we can move forward only by pointers """
            
            self._tail.next = node
            self._tail = node
        self._size += 1

    def pop(self):
        """ This methods removes the last element of the List """
        """ Case 1) The list is empty """
        """ Case 2) List only has 1 item """
        """ Case 3) List has items more than 1 """

        """To be able to remove an element, we need to go to previous element, and set it's pointer to none"""
        
        previous = None
        current_node = self._head
       

        if current_node is None:
            return None
        elif current_node.next is None:
            self._head = None
            self._size -= 1
            return current_node.data
        else:
            while current_node.next:
                previous=current_node
                current_node = current_node.next
            
            self._tail = previous
            previous.next=None
            self._size -= 1
            return current_node.data
        
    def remove(self,index):
        print("REMOVE WILL RUN  THIS IS LENGTH",self._size)
        if index < 0 or index > self._size:
            raise(ValueError("Index out of bounds"))
        
        previous_node = None
        current_node = self._head
        next_node = current_node.next

        if index == 0:
            temp = self._head
            self._head = temp.next
            self._size -=1
            return temp.data



     
        print("INDEX",index)
        for _ in range(index):

            print("for _ ",_)
                
               
            previous_node = current_node
            current_node = next_node
            next_node = current_node.next
             
                # next_node = current_node.next
            print("Previous",previous_node)
            print("Current",current_node)
            print("Next",next_node)

       
        self._size -=1
        previous_node.next = next_node
        toRemove = current_node
        return toRemove.data
                
                
            # previous_node.next = next_node
           
            
            
          
        
   

        
             
                


            






dll = DoublyLinkedList()
dll.append(10)
dll.append(20)
dll.append(30)
dll.append(40)
dll.append(50)
dll.remove(4)


print(dll)
    
   
