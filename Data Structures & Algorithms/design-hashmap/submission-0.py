class ListNode:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.next = None

class MyHashMap:

    def __init__(self):
        self.data = [ListNode(0, -1) for i in range(10000)]        

    def put(self, key: int, value: int) -> None:
        index = key % len(self.data)
        
        cur = self.data[index] # point to the first ListNode at the specified index
        while cur.next: # go to the end of the LinkedList to insert new value
            if cur.next.key == key:
                cur.next.value = value # key was already added, so update the value
                return

            cur = cur.next
        
        cur.next = ListNode(key, value) # we are at the end of the LinkedList, add new value

    def get(self, key: int) -> int:
        index = key % len(self.data)
        cur = self.data[index]

        while cur.next:
            if cur.next.key == key:
                return cur.next.value
        
            cur = cur.next
        
        return -1

    def remove(self, key: int) -> None:
        index = key % len(self.data)
        cur = self.data[index]

        while cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            cur = cur.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)