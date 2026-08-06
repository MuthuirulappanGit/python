stack = []
queue = []

def push(item):
    stack.append(item)

def pop():
    return stack.pop()

def enqueue(item):
    queue.append(item)

def dequeue():
    return queue.pop(0)

text = input("Enter a string: ")

clean = ""

for ch in text:
    if ch.isalnum():
        clean += ch.lower()

for ch in clean:
    push(ch)
    enqueue(ch)

palindrome = True

while stack:
    if pop() != dequeue():
        palindrome = False
        break

if palindrome:
    print("Palindrome")
else:
    print("Not a Palindrome")
