#
# @lc app=leetcode.cn id=146 lang=python3
#
# [146] LRU 缓存机制
#

# @lc code=start



class doublelinknode:
    def __init__(self,key=0,value=0) -> None:
        self.key = key
        self.value = value
        self.pre = None
        self.next = None
class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        # 使用伪头部和伪尾部节点  
        self.head = doublelinknode()
        self.tail = doublelinknode()
        self.head.next=self.tail
        self.tail.pre = self.head
        self.capacity = capacity
        self.size = 0

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
         # 如果 key 存在，先通过哈希表定位，再移到头部
        node = self.cache[key]
        self.moveToHead(node)
        return node.value



    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            # 如果 key 不存在，创建一个新的节点
            node = doublelinknode(key,value)
            # 添加进哈希表
            self.cache[key] = node
            # 添加至双向链表的头部
            self.addToHead(node)
            self.size += 1
            if self.size>self.capacity:
                 # 如果超出容量，删除双向链表的尾部节点
                removed = self.removeTail()
                self.cache.pop(removed.key)
                self.size -= 1
        else:
            # 如果 key 存在，先通过哈希表定位，再修改 value，并移到头部
            node = self.cache[key]
            node.value = value
            self.moveToHead(node)

    def moveToHead(self,node):
        self.removeNode(node)
        self.addToHead(node)

    def removeTail(self):
        node = self.tail.pre
        self.tail.pre= node.pre
        node.pre.next = self.tail
        # self.removeNode(node)
        return node

    def addToHead(self,node):
        node.next=self.head.next
        self.head.next.pre=node
        self.head.next = node
        node.pre = self.head

    def removeNode(self,node):
        node.pre.next = node.next
        node.next.pre = node.pre




# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

