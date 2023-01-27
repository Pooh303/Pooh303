
class DataNode:
    def __init__(self, name):
        self.name = name
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.count = 0
        self.head = None

    def traverse(self):
        if self.head is None:
            print("This is an empty list.")
        else:
            pos = self.head
            while pos is not None:
                print("->", pos.name, end='')
                pos = pos.next
            print("")
        return
    
    def insertFront(self, data):
        pNew = DataNode(data)
        if self.head is None: #empty
            self.head = pNew
        else:
            pNew.next = self.head
            self.head = pNew
        self.count += 1
        return
    
    def insertLast(self, data):
        pNew = DataNode(data)
        if self.head is None:
            self.head = pNew
        else:
            start = self.head
            while start.next != None:
                start = start.next
            start.next = pNew
        return
        
    
    def insertBefore(self, node, data):
        if not self.head:
            print("This is an empty list.")
            return
        new_node = DataNode(data)
        current = self.head

        if current.name == node:
            new_node.next = current
            self.head = new_node
            return
        while current.next:
            if current.next.name == node:
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
        print("Cannot insert, {} does not exist.".format(node))
        return

    def delete(self, data):
        if not self.head:
            print("This is an empty list.")
        if self.head.name == data:
            self.head = self.head.next
            return
        start = self.head
        while start.next:
            if start.next.name == data:
                start.next = start.next.next
                return
            start = start.next
        print("Cannot delete, {} does not exist.".format(data))
        return


mylist = SinglyLinkedList() #Object
pNew = DataNode("John")
mylist.head = pNew
print(mylist.head.name)
pNew = DataNode("Tony")
mylist.head.next = pNew
print(mylist.head.next.name)
mylist.traverse()
mylist.insertFront("Bill")
mylist.traverse()
mylist.insertLast("Ben")
mylist.traverse()
mylist.delete("Ben")






