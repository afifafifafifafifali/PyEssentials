'''
The Listpy library
Copyright(c), Afif Ali Saadman
See the README.md file
'''
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class ListPy:
    def __init__(self):
        self.head = None

    def __len__(self):
        return self.get_length()

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data)+' --> ' if itr.next else str(itr.data)
            itr = itr.next
        print(llstr)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def append(self, data):  # alias of insert_at_end
        self.insert_at_end(data)

    def insert(self, index, data):  # alias of insert_at
        self.insert_at(index, data)

    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data)

    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise IndexError("Invalid Index")
        if index == 0:
            self.insert_at_begining(data)
            return
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = Node(data, itr.next)
                break
            itr = itr.next
            count += 1

    def pop(self, index=-1):
        length = self.get_length()
        if length == 0:
            raise IndexError("Pop from empty list")
        if index < -length or index >= length:
            raise IndexError("Index out of range")
        if index < 0:
            index += length
        if index == 0:
            popped = self.head.data
            self.head = self.head.next
            return popped
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                popped = itr.next.data
                itr.next = itr.next.next
                return popped
            itr = itr.next
            count += 1

    def remove(self, value):
        if self.head is None:
            raise ValueError("Value not in list")
        if self.head.data == value:
            self.head = self.head.next
            return
        itr = self.head
        while itr.next:
            if itr.next.data == value:
                itr.next = itr.next.next
                return
            itr = itr.next
        raise ValueError("Value not in list")

    def clear(self):
        self.head = None

    def index(self, value):
        count = 0
        itr = self.head
        while itr:
            if itr.data == value:
                return count
            itr = itr.next
            count += 1
        raise ValueError("Value not in list")

    def count(self, value):
        count = 0
        itr = self.head
        while itr:
            if itr.data == value:
                count += 1
            itr = itr.next
        return count

    def reverse(self):
        prev = None
        curr = self.head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        self.head = prev

    def sort(self):
        self.head = self._merge_sort(self.head)

    def _merge_sort(self, head):
        if head is None or head.next is None:
            return head
        mid = self._get_middle(head)
        right = mid.next
        mid.next = None
        return self._sorted_merge(self._merge_sort(head), self._merge_sort(right))

    def _get_middle(self, head):
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def _sorted_merge(self, a, b):
        if not a: return b
        if not b: return a
        if a.data < b.data:
            a.next = self._sorted_merge(a.next, b)
            return a
        else:
            b.next = self._sorted_merge(a, b.next)
            return b

    def get(self, index):  # like list[index]
        if index < 0 or index >= self.get_length():
            raise IndexError("Index out of range")
        itr = self.head
        count = 0
        while itr:
            if count == index:
                return itr.data
            itr = itr.next
            count += 1

    def set(self, index, value):  # like list[index] = value
        if index < 0 or index >= self.get_length():
            raise IndexError("Index out of range")
        itr = self.head
        count = 0
        while itr:
            if count == index:
                itr.data = value
                return
            itr = itr.next
            count += 1

    def insert_values(self, data_list):
        self.clear()
        for data in data_list:
            self.append(data)
