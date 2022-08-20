import string
import random
from typing import List


def generar_id(length=8):
    # helper function for generating an id
    return ''.join(random.choices(string.ascii_uppercase, k=length))


class TicketSoporte:

    def __init__(self, customer, issue):
        self.id = generar_id()
        self.customer = customer
        self.issue = issue


class SoporteCliente:

    def __init__(self, processing_strategy: str = "fifo"):
        self.tickets = []
        self.processing_strategy = processing_strategy

    def crear_ticket(self, customer, issue):
        self.tickets.append(TicketSoporte(customer, issue))

    def procesar_tickets(self):
        # if it's empty, don't do anything
        if len(self.tickets) == 0:
            print("There are no tickets to process. Well done!")
            return

        if self.processing_strategy == "fifo":
            for ticket in self.tickets:
                self.procesar_ticket(ticket)
        elif self.processing_strategy == "filo":
            for ticket in reversed(self.tickets):
                self.procesar_ticket(ticket)
        elif self.processing_strategy == "random":
            list_copy = self.tickets.copy()
            random.shuffle(list_copy)
            for ticket in list_copy:
                self.procesar_ticket(ticket)

    def procesar_ticket(self, ticket: TicketSoporte):
        print("==================================")
        print(f"Processing ticket id: {ticket.id}")
        print(f"Customer: {ticket.customer}")
        print(f"Issue: {ticket.issue}")
        print("==================================")


# create the application
app = SoporteCliente("filo")

# register a few tickets
app.crear_ticket("John Smith", "My computer makes strange sounds!")
app.crear_ticket("Linus Sebastian", "I can't upload any videos, please help.")
app.crear_ticket("Arjan Egges", "VSCode doesn't automatically solve my bugs.")

# process the tickets
app.procesar_tickets()