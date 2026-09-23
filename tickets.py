import csv
import os

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
if __name__ == "__main__":
    print("Ticket Journal System started.")