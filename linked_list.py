class SinglyNode:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class DoublyNode:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None


def menu():
    print("\n1. Singly Linked List \n2. Doubly Linked List \n3. Circular Linked List \n4. Exit")
    choice = int(input("Choose an option: "))
    return choice


def singly_linked_list():
    print("\n*** Singly Linked List ***")
    choice = 1
    head = None
    temp = None
    while choice == 1:
        data = int(input("\nEnter node data: "))
        new_node = SinglyNode(data)
        if head is None:
            head = temp = new_node
        else:
            temp.next = new_node
            temp = new_node
        choice = int(input("\nTo insert a new node press 1 else any other integer: "))
    
    print("\nThe elements in the Singly Linked list are...")
    temp = head
    while temp:
        print(temp.data)
        temp = temp.next


def doubly_linked_list():
    print("\n*** Doubly Linked List ***")
    choice = 1
    head = None
    temp = None
    while choice == 1:
        data = int(input("\nEnter node data: "))
        new_node = DoublyNode(data)
        if head is None:
            head = temp = new_node
        else:
            temp.next = new_node
            new_node.prev = temp
            temp = new_node
        choice = int(input("\nTo insert a new node press 1 else any other integer: "))
    
    print("\nThe elements in the Doubly Linked list are...")
    temp = head
    while temp:
        print(temp.data)
        temp = temp.next


def circular_linked_list():
    print("\n*** Circular Linked List ***")
    # This is a simple demonstration of circular linked list
    elements = [10, 20, 30]
    head = None
    temp = None
    for data in elements:
        new_node = SinglyNode(data)
        if head is None:
            head = temp = new_node
        else:
            temp.next = new_node
            temp = new_node
    # Making the list circular
    temp.next = head
    
    print("\nThe elements in the Circular Linked list are...")
    temp = head
    while True:
        print(temp.data)
        temp = temp.next
        if temp == head:
            break


def main():
    while True:
        choice = menu()
        if choice == 1:
            singly_linked_list()
        elif choice == 2:
            doubly_linked_list()
        elif choice == 3:
            circular_linked_list()
        elif choice == 4:
            break
        else:
            print("\nInvalid Option")


if __name__ == "__main__":
    main()
