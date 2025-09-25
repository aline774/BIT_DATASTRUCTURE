# STACK CHALLENGE
# 1) start with empty stack
stack = []                      # []

# 2) push "1","2","3","4" in that order
stack.append("1")               # stack => ["1"]
stack.append("2")               # stack => ["1","2"]
stack.append("3")               # stack => ["1","2","3"]
stack.append("4")               # stack => ["1","2","3","4"]

# 3) pop 1 (removes the top element — LIFO)
popped = stack.pop()            # popped == "4", stack => ["1","2","3"]

# 4) push "5"
stack.append("5")               # stack => ["1","2","3","5"]

# 5) read top (last element)
top = stack[-1]                 # top == "5"

# QUEUE CHALLENGE
from collections import deque

# 1. Use a FIFO queue to hold incoming orders
orders = deque()                        # empty queue

# 2. When a customer places an order, enqueue it
order = {"id": 101, "items": ["burger","fries"], "time": "12:00"}
orders.append(order)                    # newest order goes to the tail

# 3. Kitchen takes the next order from the front (dequeue)
next_order = orders.popleft()           # removes & returns the oldest order

# 4. Prepare and mark ready, then hand to server
#  (preparation steps follow; once ready, notify server/customer)

# 5. Optional: handle cancellations or VIPs:
# - If cancellation: remove order if still in queue (search & remove)
# - If priority customers exist: use a priority queue or place VIPs into a separate fast-lane queue

# 6. Monitor queue length to inform customers of expected wait times
queue_length = len(orders)
