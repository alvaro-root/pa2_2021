import queue
import array as arr

# ============================================
# Array
# ============================================
a = arr.array('d', [1.1, 2.1, 3.1])
a.append(3.4)
a.extend([4.5, 6.3, 6.8])
a.insert(2, 3.8)

b = arr.array('d', [3.7, 8.6])
c = arr.array('d')
c = a + b

print(a.pop())
print(a.pop(3))
a.remove(1.1)


# ============================================
# Stack
# ============================================
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, data):
        self.items.append(data)

    def pop(self):
        return self.items.pop()


s = Stack()

while True:
    print('push <value>')
    print('pop')
    print('quit')
    do = input('What would you like to do?').split()

    operation = do[0].strip().lower()
    if operation == 'push':
        s.push(int(do[1]))
    elif operation == 'pop':
        if s.is_empty():
            print('Stack is empty')
        else:
            print('Popped value:', s.pop())
    elif operation == 'quit':
        break


# ============================================
# Queue
#
# Can also use the 'queue' library.
# The queue module implements multi-producer, multi-consumer queues. It is especially useful in threaded programming
# when information must be exchanged safely between multiple threads. The Queue class in this module implements all the
# required locking semantics.
#
# The module implements three types of queue, which differ only in the order in which the entries are retrieved. In a
# FIFO queue, the first tasks added are the first retrieved. In a LIFO queue, the most recently added entry is the first
# retrieved (operating like a stack). With a priority queue, the entries are kept sorted (using the heapq module) and
# the lowest valued entry is retrieved first.
# ============================================
class Queue:
    def __init__(self, max_size):
        self.__max_size = max_size
        self.__elements = [None] * self.__max_size
        self.__rear = -1
        self.__front = 0

    # returns max_size of queue
    def get_max_size(self):
        return self.__max_size

    # returns bool value whether queue is full or not, True if full and False otherwise
    def is_full(self):
        return self.__rear == self.__max_size - 1

    # inserts/enqueue data to the queue if it is not full
    def enqueue(self, data):
        if (self.is_full()):
            print("Queue is full. No enqueue possible")
        else:
            self.__rear += 1
            self.__elements[self.__rear] = data

    # display all the content of the queue
    # def display(self):
    #     for i in range(0, self.__rear + 1):
    #         print(self.__elements[i])

    # You can use the below __str__() to print the elements of the DS object while debugging
    def __str__(self):
        msg = []
        index = self.__front
        while (index <= self.__rear):
            msg.append((str)(self.__elements[index]))
            index += 1
        msg = " ".join(msg)
        msg = "Queue data(Front to Rear): " + msg
        return msg

    # function to check if queue is empty or not
    def is_empty(self):
        if (self.__rear == -1 or self.__front == self.__max_size):
            return True
        else:
            return False

    # function to deque an element and return it
    def dequeue(self):
        if (self.is_empty()):
            print("queue is already empty")
        else:
            data = self.__elements[self.__front]
            self.__front += 1
            return data

    # function to display elements from front to rear if queue is not empty
    def display(self):
        if (not self.is_empty()):
            for i in range(self.__front, self.__rear + 1):
                print(self.__elements[i])
        else:
            print("empty queue")


queue1 = Queue(5)

# Enqueue all the required element(s)
queue1.enqueue("A")
queue1.enqueue("B")
queue1.enqueue("C")
queue1.enqueue("D")
queue1.enqueue("E")
print(queue1)

# Dequeue all the required element(s)
print("Dequeued: ", queue1.dequeue())
print("Dequeued: ", queue1.dequeue())
print("Dequeued: ", queue1.dequeue())
print("Dequeued: ", queue1.dequeue())
print("Dequeued: ", queue1.dequeue())
print("Dequeued: ", queue1.dequeue())

# ============================================
# Heap
# Heap is a special tree structure in which each parent node is less than or equal to its child node. Then it is called
# a Min Heap. If each parent node is greater than or equal to its child node then it is called a max heap. It is very
# useful is implementing priority queues where the queue item with higher weightage is given more priority in processing.
#
# Create a Heap
# A heap is created by using python’s inbuilt library named heapq. This library has the relevant functions to carry out
# various operations on heap data structure. Below is a list of these functions.
#
# heapify - This function converts a regular list to a heap. In the resulting heap the smallest element gets pushed to
# the index position 0. But rest of the data elements are not necessarily sorted.
# heappush – This function adds an element to the heap without altering the current heap.
# heappop - This function returns the smallest data element from the heap.
# heapreplace – This function replaces the smallest data element with a new value supplied in the function.
# ============================================
import heapq

H = [21,1,45,78,3,5]
# Use heapify to rearrange the elements
heapq.heapify(H)
print(H)
# Add element
heapq.heappush(H,8)
print(H)
# Remove element from the heap
heapq.heappop(H)
# Replace an element
heapq.heapreplace(H,6)
print(H)

# initializing list
li = [5, 7, 9, 1, 3]

# using heapify to convert list into heap
heapq.heapify(li)

# printing created heap
print("The created heap is : ", end="")
print(list(li))

# using heappush() to push elements into heap
# pushes 4
heapq.heappush(li, 4)

# printing modified heap
print("The modified heap after push is : ", end="")
print(list(li))

# using heappop() to pop smallest element
print("The popped and smallest element is : ", end="")
print(heapq.heappop(li))

# initializing list 1
li1 = [5, 7, 9, 4, 3]

# initializing list 2
li2 = [5, 7, 9, 4, 3]

# using heapify() to convert list into heap
heapq.heapify(li1)
heapq.heapify(li2)

# using heappushpop() to push and pop items simultaneously
# pops 2
print("The popped item using heappushpop() is : ", end="")
print(heapq.heappushpop(li1, 2))

# using heapreplace() to push and pop items simultaneously
# pops 3
print("The popped item using heapreplace() is : ", end="")
print(heapq.heapreplace(li2, 2))

# initializing list
li1 = [6, 7, 9, 4, 3, 5, 8, 10, 1]

# using heapify() to convert list into heap
heapq.heapify(li1)

# using nlargest to print 3 largest numbers
# prints 10, 9 and 8
print("The 3 largest numbers in list are : ", end="")
print(heapq.nlargest(3, li1))

# using nsmallest to print 3 smallest numbers
# prints 1, 3 and 4
print("The 3 smallest numbers in list are : ", end="")
print(heapq.nsmallest(3, li1))

pass