class ListNode:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return f"<ListNode: {self.data}>"


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
           
            
            
          
        
   

        
             
                


            






sll = SinglyLinkedList()
sll.append("5")
sll.append("6")
sll.append("7")
sll.append("8")
sll.remove(0)

print(sll)
    
   
