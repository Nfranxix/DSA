class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    
    def __str__(self):
        return f"{self.data}:{self.next}"


class linked_list:
    def __init__(self):
        self.head = None


    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print("List is Empty")
            return
        
        itr = self.head
        llstr = ""  
        while itr:
            llstr += str(itr.data) + "-->"
            itr = itr.next

        print(llstr)

    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data,None)
            return


        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data,None)
        

        
        

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def get_lenght(self):
        count =0
        itr = self.head
        while itr:
            count +=1
            itr = itr.next
        return count
        

    def remove_at(self, index):
        if index < 0 or index>= self.get_lenght():
            raise Exception("Invalid index")
        
        if index == 0:
            self.head = self.head.next

        count =0
        itr = self.head
        while itr:
            if count == index -1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count+=1


    def insert_at(self,index,data):
         if index < 0 or index>= self.get_lenght():
            raise Exception("Invalid index")
         
         if index==0:
             self.insert_at_begining(data)
             return
         count=0
         itr =self.head
         while itr:
            if count ==index -1:
                 node = Node(data, itr.next)
                 itr.next = node
                 break
            itr =itr.next
            count+=1
 
            
    def insert_after_value(self, data_after, data_to_insert):
        if self.head is None:
            return

        if self.head.data==data_after:
            self.head.next = Node(data_to_insert,self.head.next)
            return

        itr = self.head
        while itr:
            if itr.data == data_after:
                itr.next = Node(data_to_insert, itr.next)
                break

            itr = itr.next

    def remove_by_value(self, data):
        if self.head == data:
            return
        
        if self.head.data == data:
            self.head = self.head.next
            return
        
        itr = self.head
        while itr:
            if itr.next.data == data:
                itr.next = itr.next.next
                break
            itr = itr.next 
                



list = linked_list()
list.insert_values([1,45,78,300,23,400])
list.print()
list.insert_after_value(78,100)
list.print()
list.remove_by_value(300)

# list.insert_at_begining(56)
# list.insert_at_end(44)
# list.insert_at_begining(57)
# list.insert_at_begining(50)
# list.print()
# list.remove_at(2)
# list.print()
# list.insert_at(1,100)
# print(list.get_lenght())
list.print()

