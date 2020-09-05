class Node:
    def __init__(self, data, nextNode):
        self.data = data
        self.pnext = nextNode


class List:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node_next(self, data):
        if self.head is None and self.tail is None:
            node = Node(data, None)
            self.head = node
            self.tail = node
            return
        # Remember about pointer in C++
        node = Node(data, None)
        self.tail.pnext = node
        self.tail = node

    def insert_node_pre(self, data):
        if self.head is None and self.tail is None:
            node = Node(data, None)
            self.head = node
            self.tail = node
            return

        node = Node(data, self.head)
        self.head = node

    def printlist(self):
        if self.head is None and self.tail is None:
            print 'List is empty'
            return

        while(self.head != self.tail):
            print self.head.data
            self.head = self.head.pnext

            if self.head.pnext is None:
                print self.head.data


linklist = List()

for i in range(5):
    print 'i', i
    linklist.insert_node_next(10*i)

linklist.insert_node_pre(100)

linklist.printlist()
