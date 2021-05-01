class Node:
    # Initializer to initilize class variables
    def __init__(self, data=None, next_node=None):
        self._data = data
        self.next_node = next_node

    def __str__(self):
        return f"{self._data}"

    # get data
    @property
    def data(self):
        return self._data

    # get next value
    def get_next(self):
        return self.next_node

    # set next data
    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def insert(self, data):
        """
        This insert method takes data, initializes a new node with the given data, and adds it to the list. Technically
        you can insert a node anywhere in the list, but the simplest way to do it is to place it at the head of the
        list and point the new node at the old head (sort of pushing the other nodes down the line).
        """
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    def __len__(self):
        """
        The size method is very simple, it basically counts nodes until it can’t find anymore, and returns how many
        nodes it found. The method starts at the head node, travels down the line of nodes until it reaches the end
        (the current will be None when it reaches the end) while keeping track of how many nodes it has seen.
        """
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next()
        return count

    def search(self, nodeData):
        """
        Search is actually very similar to size, but instead of traversing the whole list of nodes it checks at each 
        stop to see whether the current node has the requested data. If so, returns the node holding that data. If the 
        method goes through the entire list but still hasn’t found the data, it raises a value error and notifies the 
        user that the data is not in the list. 
        """
        current = self.head
        isPresent = False
        while current and isPresent is False:
            if current.data == nodeData:
                isPresent = True
            else:
                current = current.get_next()
                if current is None:
                    raise ValueError("Data not present in list")
        return current

    def delete(self, nodeData):
        """
        The delete method traverses the list in the same way that search does, but in addition to keeping track of the
        current node, the delete method also remembers the last node is visited. When delete finally arrives at the node
        it wants to delete. It simply removes that node from the chain by “leapfrogging” it.

        By this I mean that when the delete method reaches the node it wants to delete, it looks at the last node it
        visited (the ‘previous’ node) and resets that previous node’s pointer. Rather than pointing to the
        soon-to-be-deleted node.

        It will point to the next node in line. Since no nodes are pointing to the poor node that is being deleted, it
        is effectively removed from the list!
        """
        current = self.head
        previous = None
        isPresent = False
        while current and isPresent is False:
            if current.data == nodeData:
                isPresent = True
            else:
                previous = current
                current = current.get_next()
        if current is None:
            raise ValueError("Data not present in list")
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())
                
if __name__ == "__main__":

    nodes = (1,22,4,67,8,99,23,4,)

    ll = LinkedList()

    for n in nodes:
        ll.insert(n)

    found = ll.search(8)
    print(f"Found: {found}")
    # print(f"Size: {ll.__len__()}")
    print(f"Size: {len(ll)}")
    ll.delete(22)
    print(f"Size: {ll.__len__()}")
