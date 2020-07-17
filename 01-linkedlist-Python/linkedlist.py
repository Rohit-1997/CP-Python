"""The LinkedList code from before is provided below.
Add three functions to the LinkedList.
"get_position" returns the element at a certain position.
The "insert" function will add an element to a particular
spot in the list.
"delete" will delete the first element with that
particular value.
Then, use "Test Run" and "Submit" to run the test cases
at the bottom."""

class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        
    def append(self, new_element):
        if not self.head:
            self.head = new_element
            return
        current = self.head
        while current.next != None:
            current = current.next
        current.next = new_element
            
    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        if not self.head:
            return None
        counter = 1
        current = self.head

        while counter != position:
            current = current.next
            counter += 1
        return current.value
    
    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        # Your code goes here
        if not self.head:
            self.head = new_element
            return
        
        # first position
        if position == 1:
            new_element.next = self.head
            self.head = new_element
            return

        counter = 1
        current = self.head
        while counter < position:
            current = current.next
            counter += 1
        
        
    
    
    def delete(self, value):
        """Delete the first node with a given value."""
        # Your code goes here
        pass
