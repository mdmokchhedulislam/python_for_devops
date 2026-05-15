# class BrowserHistory:
#     def __init__(self):
#         self.history = []

#     def visit_page(self, url):
#         print(f"Visiting: {url}")
#         self.history.append(url)

#     def back_button(self):
#         if len(self.history) > 1:
#             last_page = self.history.pop()
#             print(f"Moving back from: {last_page}")
#             print(f"Now at: {self.history[-1]}")
#         else:
#             print("No more pages in history!")


# browser = BrowserHistory()
# browser.visit_page("google.com")
# browser.visit_page("facebook.com")
# browser.visit_page("github.com")

# browser.back_button() 
# browser.back_button() 




# numbers = [1,2,3,4,5,6,7,8,9,10]
# odd = []
# for i in numbers:
#     if(i%2!=0):
#         odd.append(i)
#         print(f"{i} is odd number")

# print(odd)


# linkedlist

class Node:
    def __init__(self, data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
    
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def append(self, data):
        new_node=Node(data)
        if not self.head:
            self.head=new_node
            return
        last = self.head
        while last.next:
            last=last.next
        last.next=new_node


    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

mylist = LinkedList()
mylist.append(10)
mylist.append(20)
mylist.append(30)
mylist.append(40)
mylist.append(50)



mylist.display()