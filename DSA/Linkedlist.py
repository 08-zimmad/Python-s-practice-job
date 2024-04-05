class Node:
    def __init__(self,var):
        self.val=var
        self.next=None


class LinkedList:
    def __init__(self) -> None:
        self.head=None

    def InsertAtStart(self,val):
        if self.head==None:
            self.head=Node(val)
            return self.head
        else:
            return None

    def insertAtMid(self,val,pos):
        if self.head==None:
            return self.InsertAtStart(val)
        if pos<0:
            print("Invalid Position")
            return
        cur_node=self.head
        prev_node=cur_node
        for i in range(0, pos-1):
            if cur_node==None:
                print("Position Out of bound")
                return
            prev_node=cur_node
            cur_node=cur_node.next

        if cur_node==None:
            print("Position Out of bound1")
            return

        new_node=Node(val)
        prev_node.next=new_node
        new_node.next=cur_node
        return new_node
    
    def insertAtEnd(self, val):
        if self.head is None:

            self.head = Node(val)
            return

        alt_head = self.head
        while alt_head.next is not None:
            alt_head = alt_head.next

        new_node = Node(val)
        alt_head.next = new_node

    def print_list(self):
        alt_head=self.head
        while alt_head is not None:
            print(alt_head.val)
            alt_head=alt_head.next



if "__main__":
    list=LinkedList()
    list.InsertAtStart(1)
    list.insertAtEnd(2)
    list.insertAtEnd(3)
    list.insertAtEnd(4)
    list.insertAtEnd(5)
    list.insertAtMid(6,4)

    list.print_list()



