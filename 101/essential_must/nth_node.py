class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


node1 = Node(11)
node2 = Node(22)
node3 = Node(33)
node4 = Node(44)
node5 = Node(55)

head = Node(0)
head.next = node1
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = None

start = head.next
while start:
    print(start.val)
    start = start.next

print("Nth node from back")
start = head.next


def find_nth(start, n):
    left = head
    right = head
    for i in range(n):
        if right == None:
            return None
        right = right.next

    while right:
        right = right.next
        left = left.next
    print(left.val)


find_nth(start, 2)


def find_the_path(A, rows, cols, i, j):  #
    stack = []
    count = 0
    result = []
    seen = set()
    stack.append((i, j))
    while stack:
        if len(result) == 4:
            result = result[1:]
            seen.clear()

        x, y = stack.pop()
        result.append(A[x][y])
        seen.add(A[x][y])
        count += 1
        # Checking right, left, down, up
        # Trying to use stack, so that I can pop the last element
        # Storing the result in a list and checking for length 4
        for d in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            next_x, next_y = x + d[0], y + d[1]
            if 0 <= next_x < rows and 0 <= next_y < cols:
                if A[next_x][next_y] not in seen and len(result) < 4:
                    stack.append((next_x, next_y))
                    # result.append(A[next_x][next_y])
                    seen.add(A[next_x][next_y])
                    count += 1
                if len(result) == 4:
                    print(result)
                    break