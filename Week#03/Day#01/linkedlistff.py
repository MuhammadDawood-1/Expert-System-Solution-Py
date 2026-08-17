class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    
        
class linkedlist:
    head=None
    tail=None
    #initialize
    def __init__(self,n1):
        self.head=n1
        self.tail=n1
    
    def insert_head(self,n1):
        n1.next=self.head
        self.head=n1
        
    def insert_tail(self,m1):
        self.tail.next=m1
        self.tail=m1
    def display(self):
        temp=self.head
        while temp:
            print(temp.data)
            temp=temp.next
    # def insert_after(self, i, n2):
    #     temp=self.head
    #     while temp:
    #         temp=temp.next
    #         if temp.data == i:
    #             temp.
                
        
        
        
d=Node(10)
c=Node(20)
v=Node(30)

l=linkedlist(d)
# l.display()
l.insert_head(v)
# l.display()
l.insert_tail(c)
l.display()        