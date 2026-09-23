import os
from tickets import add_ticket

# Test: add new ticket
add_ticket("tickets.csv", "4", "New keyboard request", "open", "low")
print("Test passed: ticket added successfully")
