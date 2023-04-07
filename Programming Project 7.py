#Jack Krejci

#Singly linked list class
class ListEmpty(Exception):
    pass

#Exception for to small of a list
class ToSmall(Exception):
    pass

#Singly List
class SinglyList:
    class _Node:
        def __init__(self, e, next):
            self._element = e
            self._next = next

    def __init__(self):
        self._head = self._tail = None
        self._size = 0

        self._current = None #needed to provide iterator support

    def is_empty(self):
        return self._size == 0

    def add_head(self, element):
        if self.is_empty():
            new_node = self._Node(element, None)
            self._head = self._tail = self._current = new_node
        else:
            new_node = self._Node(element, self._head)
            self._head = new_node

        self._size += 1

    def add_tail(self, element):
        if self.is_empty():
            self.add_head(element)
        else:
            new_node = self._Node(element, None)
            self._tail._next = new_node
            self._tail = new_node
            self._size += 1

    def delete_tail(self):
        if self.is_empty():
            raise ListEmpty()

        p = self._head
        while p._next is not self._tail:
            p = p._next

        self._tail = p
        self._tail._next = None

        self._size -= 1
        
    def delete_head(self):
        if self.is_empty():
            raise ListEmpty()

        p = self._head
        self._head = p._next
        p._next = None

        self._size -= 1
        
    #Function that finds the third to last element in the list
    def find_3rd_to_last(self):
        #Can't get third to last if there's less than 3 elements
        if self._size < 3:
            raise ToSmall()

        #Do your algorithm to find the third to last element
        counter = 0
        list_len = self._size
        for i in self:
            counter += 1
            if counter == (list_len - 2):
                return i
        
    #Function that reverses the list
    def reverse(self):

        if self.is_empty():
            raise ListEmpty()
        
        #Add every element to the head to put it in reverse and take note of orignal size
        size_orig = len(self)
        for e in self:
            self.add_head(e)

        #While the size of the new list is greater than the old delete the tail
        #which deletes all the old elements which were pushed to the back of the list
        while len(self) > size_orig:
            self.delete_tail()             

    
    def __len__(self):
        return self._size


    def __iter__(self):
        """needed to provide iterator support"""
        return self

    def __next__(self):
        """needed to provide iterator support,
        there are several other cases that needs
        to be handled when delete_head, delete_tail
        are interleaved with iterator, one classical
        way of overcomming this is to lock modification
        while iterator is in progress (e.g.: raise
        concurrent modification exception as in java).
        Handling these cases is beyond scope of this
        simple implementation"""

        if self.is_empty():
            raise StopIteration()

        if self._current == None:
            # as a rough solution, start iterator over
            self._current = self._head
            raise StopIteration()

        e = self._current._element
        self._current = self._current._next
        return e


#Main Code BELOW IS JUST CHECK CODE; NEED TO ADJUST THIS AS YOU GO
l = SinglyList()

#Adds 0-9 in proper order by making each new element the last eventually making 9 last where it should be
for i in range(10):
    l.add_tail(i)

#Used to print what the elements are in the list in the correct order above
print("Original List:")
for e in l:
    print(e)
    
print()

#Call the reverse function and check if the list was indeed reveresed
l.reverse()
print("Below is the reversed list:")
for e in l:
    print(e)

#Print the third to last element
third_last = l.find_3rd_to_last()
print("The third to last element:", third_last)
