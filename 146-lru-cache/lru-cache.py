class Node:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self,node):
        node.prev.next = node.next
        node.next.prev = node.prev
        return
    
    def insert(self,node):
        node.next = self.head.next
        node.prev = self.head

        self.head.next.prev = node
        self.head.next = node
        return
        

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.value
        return -1


    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.remove(node)
            self.insert(node)
            return 
        elif len(self.cache)>=self.cap:
            lru = self.tail.prev
            self.remove(lru)
            del self.cache[lru.key]
            node = Node(key,value)
            self.insert(node)
            self.cache[key] = node
        else:
            node = Node(key,value)
            self.insert(node)
            self.cache[key] = node
        return


        




        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)