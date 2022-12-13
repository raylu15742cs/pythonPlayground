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

    


if __name__ == '__main__':
    ll = LinkedList()
    ll.print()