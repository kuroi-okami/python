from src.data_structures.dllist.dlllist_node import DlListNode


class DllList():
    def __init__(self):
        self.head = None

    def insert(self, value: int) -> None:
        tail = self.head
        while tail is not None:
            tail = tail.next

        new_head = DlListNode(value)
        new_head.next = self.head
        if self.head is not None:
            new_head.prev = None

        self.head = new_head

    def display(self):
        tmp = self.head
        while (tmp is not None):
            print(tmp.value)
            tmp = tmp.next


if __name__ == '__main__':
    list = DllList()
    list.insert(2)
    list.insert(5)
    list.insert(3)
    list.insert(4)
    list.insert(8)
    list.insert(9)
    list.insert(1)

    list.display()
