class Hash_Table:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self,key):
        h =0
        for char in key:
            h += ord(char)
            return h % self.MAX
        
       
    def __getitem__(self, key):
        arr_index = self.get_hash(key)
        for kv in self.arr[arr_index]:
            if kv[0] == key:
                return kv[1]
            
    def __setitem__(self, key, val):
        h = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element)==2 and element[0] == key:
                self.arr[h][idx] = (key,val)
                found = True
        if not found:
            self.arr[h].append((key,val))
        
    def __delitem__(self, key):
        arr_index = self.get_hash(key)
        for index, kv in enumerate(self.arr[arr_index]):
            if kv[0] == key:
                print("del",index)
                del self.arr[arr_index][index]

ht = Hash_Table()
ht["may 9"] = 300
# print(ht.arr)
ht["may 6"] = 30000
ht["april 11"] = 200
ht["may 6"] = 100
ht["jan 3"] =700
ht["july 14"] =1000
ht["jan 20"] =800
print(ht.arr)
print(ht["july 14"])
print(ht["may 6"])
        


