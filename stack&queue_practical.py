# STACK QUESTIONS

# practical 1
# Stack implementation using list
stack = []

# Push operations
stack.append("Class1")
stack.append("Class2")
stack.append("Class3")

# Pop two elements
stack.pop()  # Removes "Class3"
stack.pop()  # Removes "Class2"

# Check top of stack
top_element = stack[-1] if stack else None
print("Top of stack:", top_element)

# practical 2
# Stack implementation using list
stack = []

# Push operations
stack.append("Form1")
stack.append("Form2")
stack.append("Form3")

# Pop all elements
stack.pop()  # Removes "Form3"
stack.pop()  # Removes "Form2"
stack.pop()  # Removes "Form1"

# Check what's left
print("Stack is empty:", len(stack) == 0)
# QUEUE QUESTIONS 

# practical 1
from collections import deque

# Step 1: Create queue of 6 clients
queue = deque(["Client1", "Client2", "Client3", "Client4", "Client5", "Client6"])

print("Initial queue:", list(queue))

# Step 2: Serve first 2 clients (remove from front)
queue.popleft()
queue.popleft()

# Step 3: Check who is in front now
print("Queue after serving 2 clients:", list(queue))
print("Now in front:", queue[0])

# practical 2
from collections import deque

# Step 1: Create queue of 8 buses
queue = deque(["Bus1", "Bus2", "Bus3", "Bus4", "Bus5", "Bus6", "Bus7", "Bus8"])

print("Queue of buses:", list(queue))

# Step 2: Identify last bus
print("The last bus is:", queue[-1])
