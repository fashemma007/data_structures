class Node:
    # Node:data(value),next(next_value)
    def __init__(self,data=None,next=None):
        self.data = data ## the data value stored
        self.next = next ##value each it is pointing to next. If None, then it is end of list
class LinkedList:
    def __init__(self):
        self.head =None ## by default Head is none because the list is initially empty
    
    def insert_infront(self,data):
        """Inserts the given data at the begining of the linked list"""
        node = Node(data,self.head) ## placing the data in the node and giving it the attribute of Head
        self.head = node ## pointing Head attribute to the new node
    
    def show(self):
        if self.head is None: ## check if list is empty by checking if there is no head
            print("Linked list is empty")
            return
        iterator = self.head ## iterator to run thru the linked list
        string = ''  ## string where values in the list would be appended to
        while iterator: ## as far as the iterator isn't None...
            string +=str(iterator.data)+'=-->' ##append the data in iterator to the string and separate by =-->
            iterator = iterator.next ## do this again until there is no Next value
        print(string)
    
    def insert_end(self,data):
        """Inserts the given data to the end of the linked list"""
        if self.head is None: ## checks if list is empty
            self.head = Node(data,None) ## then make the new data the head with next val as None
            return
        iterator = self.head 
        while iterator.next: ## keeps on looking for the next Node iteratively
            iterator = iterator.next 
        iterator.next = Node(data,None) ## once you find the node without a Next, ie Next=None, stop
    
    def insert_vals(self,data_list):
        """Inserts the given lists into the linked list"""
        self.head = None
        for data in data_list:
            self.insert_end(data)
    
    def length(self):
        """Returns the length of the linked list"""
        count = 0
        iterator = self.head
        while iterator:
            count+=1
            iterator=iterator.next
        
        return count
        
    def remove_at(self,indx):
        if indx <0 or indx>=self.length():
            raise Exception("Invalid index")
        
        if indx == 0:
            self.head = self.head.next
            return
        count = 0
        iterator = self.head
        while iterator:
            if count == indx-1:
                iterator.next =iterator.next.next
                break
            iterator = iterator.next
            count +=1
    
    def insert_at(self,indx,data):
        if indx <0 or indx>=self.length():
            raise Exception("Invalid index")
        
        if indx == 0:
            self.insert_infront(data)
            
            return
        count = 0
        iterator = self.head
        while iterator:
            if count == indx-1:
                node = Node(data,iterator.next)
                iterator.next =node
                break
            
            iterator = iterator.next
            count +=1
    
    def insert_after_value(self, data_after, new):
        if self.head is None:
            return
        
        if self.head.data==data_after:
            self.head.next = Node(new,self.head.next)
            return

        iterator = self.head
        while iterator:
            if iterator.data == data_after:
                iterator.next = Node(new, iterator.next)
                break

            iterator = iterator.next
    
    
    def remove_by_value(self, data):
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        iterator = self.head
        while iterator.next:
            if iterator.next.data == data:
                iterator.next = iterator.next.next
                break
            iterator = iterator.next
        
    def check(self,data):
        """Checks if a given object is in the linked list"""
        lists = self.head
        while lists:
            if lists.data==data:
                return data+" is in Linked list"
            lists = lists.next
        return data+" is not in Linked list"
        
if __name__ == '__main__':
    fruit = LinkedList()
    fruit.insert_infront("Mango")
    fruit.insert_infront("Banana")
    fruit.insert_infront("Orange")
    fruit.insert_end("Cashew")
    fruit.insert_after_value("Mango","Soursop")
    fruit.show()
    # fruit.check("Guava")
    fruit.check("Soursop")
