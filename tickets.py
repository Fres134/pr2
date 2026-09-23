import csv
import os
DEFAULT_STATUS = 'new'
def load_tickets(filename="tickets.csv"):
    tickets = []
    if not os.path.exists(filename):
        print(f"File {filename} not found.")
        return tickets
    with open(filename, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=';')
        for row in reader:
            tickets.append(row)
    return tickets

def add_ticket(filename, ticket_id, title, status, priority):
    """Add a new ticket to the CSV file (ISSUE-1)."""
    from datetime import date
    file_exists = os.path.exists(filename)
    with open(filename, mode='a', encoding='utf-8', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        if not file_exists:
            writer.writerow(['id', 'title', 'status', 'priority', 'created_at'])
        writer.writerow([ticket_id, title, status, priority, date.today()])
    print(f"Ticket {ticket_id} added successfully.")

    def export_open_tickets(filename, export_filename):
    """Export open tickets to a new CSV file (ISSUE-3)."""
    tickets = load_tickets(filename)
    open_tickets = [t for t in tickets if t['status'] == 'open']
    
    with open(export_filename, mode='w', encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['id', 'title', 'status', 'priority', 'created_at'], delimiter=';')
        writer.writeheader()
        writer.writerows(open_tickets)
    
    print(f"Exported {len(open_tickets)} open tickets to {export_filename}.")

if __name__ == "__main__":
    print("Ticket Journal System started.")