class HashTable:
    def __init__(self):
        self.Max = 100
        self.list = ["Empty" for i in range(self.Max)]

    def gen_hash(self,key):
        hash = 0
        for character in key:
            hash+=ord(character)
        return hash % self.Max
    
    def __setitem__(self,key,val):
        """This allows us use the self['key'] = value
        to set the items"""
        hash = self.gen_hash(key)
        self.list[hash]=val
    
    def __getitem__(self,key):
        """This allows us use the self['key'] to get the items"""
        hash = self.gen_hash(key)
        return self.list[hash]
    
    def __delitem__(self,key):
        hash = self.gen_hash(key)
        self.list[hash] = "Empty"
        return

fruit_prices = HashTable()
fruit_prices['Guava']=200
fruit_prices['Mango']=150
fruit_prices['Sug']=50
print(fruit_prices.list)
print("__________Running `del fruit_prices['Sug']`__________ ")
del fruit_prices['Sug']
print(fruit_prices.list)