from tickets import export_open_tickets

# ISSUE-3: Test export open tickets to CSV
print("Testing export_open_tickets function...")
export_open_tickets("tickets.csv", "open_tickets_export.csv")
print("Test passed: open tickets exported")