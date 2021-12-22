class HashTable:
    def __init__(self):
        self.Max = 100
        self.list = [[] for i in range(self.Max)]

    def gen_hash(self,key):
        hash = 0
        for character in key:
            hash+=ord(character)
        return hash % self.Max
    
    def __setitem__(self,key,val):
        """This allows us use the self['key'] = value
        to set the items"""
        hash = self.gen_hash(key)
        found=False
        for indx,element in enumerate(self.list[hash]):
            if len(element)==2 and element[0]==key:
                self.list[hash][indx]=(key,val)
                found=True
                break
        if not found:
            self.list[hash].append((key,val))
        
    
    def __getitem__(self,key):
        """This allows us use the self['key'] to get the items"""
        hash = self.gen_hash(key)
        for element in self.list[hash]:
            if element[0]==key:
                return element[1]
            
    
    def __delitem__(self,key):
        hash = self.gen_hash(key)
        iterable = self.list[hash]
        for element in self.list[hash]:
            if element[0]==key:
                iterable.pop(iterable.index(element))
        return

fruit_prices = HashTable()
fruit_prices['Guava']=200
fruit_prices['Mango']=150
fruit_prices['Cashew']=250
fruit_prices['Sug']=50
print(fruit_prices.list)
print("__________Running `del fruit_prices['Sug']`__________ ")
del fruit_prices['Sug']
print(fruit_prices.list)