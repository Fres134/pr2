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

if __name__ == "__main__":
    print("Ticket Journal System started.")