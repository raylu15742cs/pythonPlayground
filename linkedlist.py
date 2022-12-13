class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
class LinkedList:
    def __init__(self):
            self.head = None
    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        llstr = ""
        while itr:
            if itr.next :
                llstr += str(itr.data) + " --> "
            else:
                llstr += str(itr.data)
            itr = itr.next
        print(llstr)
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def insert_at_begining(self,data):
        node = Node(data, self.head)
        self.head = node
    
    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data,None)
            return
        itr = self.head

        while itr.next:
            itr = itr.next
        
        itr.next = Node(data, None)
    
    def insert_at(self, index, data):
        if index<0 or index > self.get_length():
            raise Exception("Invalid Index")
        if index == 0:
            self.insert_at_begining(data)
            return
        

    


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_begining(2)
    ll.insert_at_end(3)
    ll.print()