class Node:
    def __init__(self, coeff, power):
        self.coeff = coeff
        self.power = power
        self.next = None


def insert(head, coeff, power):
    new_node = Node(coeff, power)

    if head is None:
        return new_node

    temp = head
    while temp.next:
        temp = temp.next
    temp.next = new_node
    return head


def add_poly(p1, p2):
    result = None

    while p1 and p2:
        if p1.power == p2.power:
            result = insert(result, p1.coeff + p2.coeff, p1.power)
            p1 = p1.next
            p2 = p2.next

        elif p1.power > p2.power:
            result = insert(result, p1.coeff, p1.power)
            p1 = p1.next

        else:
            result = insert(result, p2.coeff, p2.power)
            p2 = p2.next

    while p1:
        result = insert(result, p1.coeff, p1.power)
        p1 = p1.next

    while p2:
        result = insert(result, p2.coeff, p2.power)
        p2 = p2.next

    return result


def display(head):
    while head:
        print(f"{head.coeff}x^{head.power}", end="")
        if head.next:
            print(" + ", end="")
        head = head.next
    print()

n1 = int(input("Enter number of terms in first polynomial: "))
poly1 = None

print("Enter coefficient and power:")
for i in range(n1):
    c = int(input("Coefficient: "))
    p = int(input("Power: "))
    poly1 = insert(poly1, c, p)

n2 = int(input("Enter number of terms in second polynomial: "))
poly2 = None

print("Enter coefficient and power:")
for i in range(n2):
    c = int(input("Coefficient: "))
    p = int(input("Power: "))
    poly2 = insert(poly2, c, p)

print("\nFirst Polynomial:")
display(poly1)

print("Second Polynomial:")
display(poly2)

result = add_poly(poly1, poly2)

print("Sum Polynomial:")
display(result)