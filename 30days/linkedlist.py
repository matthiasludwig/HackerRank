class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def insert(self,head,data): 
        #Complete this method
        last = head

        while last:
            if last.next != None:
                last = last.next
            else:
                break

        T = Node(data)
        if last != None:
            last.next = T
            #print(head)
            return head
        else:
            #print(T.data)
            return T

mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
mylist.display(head); 	  