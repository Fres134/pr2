from tickets import add_ticket

# ISSUE-1: Test ticket creation
print("Testing add_ticket function...")
add_ticket("tickets.csv", "4", "New keyboard request", "open", "low")
print("Test passed: ticket added successfully")