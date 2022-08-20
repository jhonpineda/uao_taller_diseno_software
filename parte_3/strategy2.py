import string
import random
from typing import List
from abc import ABC, abstractmethod


def generar_id(length=8):
    # helper function for generating an id
    return ''.join(random.choices(string.ascii_uppercase, k=length))


class TicketSoporte:

    def __init__(self, customer, issue):
        self.id = generar_id()
        self.customer = customer
        self.issue = issue


class EstrategiaPedidoTicket(ABC):
    @abstractmethod
    def crear_orden(self, list: List[TicketSoporte]) -> List[TicketSoporte]:
        pass


class EstrategiaOrdenamientoFIFO(EstrategiaPedidoTicket):
    def crear_orden(self, list: List[TicketSoporte]) -> List[TicketSoporte]:
        return list.copy()


class EstrategiaOrdenamientoFILO(EstrategiaPedidoTicket):
    def crear_orden(self, list: List[TicketSoporte]) -> List[TicketSoporte]:
        list_copy = list.copy()
        list_copy.reverse()
        return list_copy


class EstrategiaOrdenamientoAleatorio(EstrategiaPedidoTicket):
    def crear_orden(self, list: List[TicketSoporte]) -> List[TicketSoporte]:
        list_copy = list.copy()
        random.shuffle(list_copy)
        return list_copy


class BlackHoleStrategy(EstrategiaPedidoTicket):
    def crear_orden(self, list: List[TicketSoporte]) -> List[TicketSoporte]:
        return []


class SoporteCliente:

    def __init__(self, processing_strategy: EstrategiaPedidoTicket):
        self.tickets = []
        self.processing_strategy = processing_strategy

    def crear_ticket(self, customer, issue):
        self.tickets.append(TicketSoporte(customer, issue))

    def procesar_tickets(self):
        # create the ordered list
        ticket_list = self.processing_strategy.crear_orden(self.tickets)

        # if it's empty, don't do anything
        if len(ticket_list) == 0:
            print("There are no tickets to process. Well done!")
            return

        # go through the tickets in the list
        for ticket in ticket_list:
            self.procesar_ticket(ticket)

    def procesar_ticket(self, ticket: TicketSoporte):
        print("==================================")
        print(f"Processing ticket id: {ticket.id}")
        print(f"Customer: {ticket.customer}")
        print(f"Issue: {ticket.issue}")
        print("==================================")


# create the application
app = SoporteCliente(EstrategiaOrdenamientoAleatorio())

# register a few tickets
app.crear_ticket("John Smith", "My computer makes strange sounds!")
app.crear_ticket("Linus Sebastian", "I can't upload any videos, please help.")
app.crear_ticket("Arjan Egges", "VSCode doesn't automatically solve my bugs.")

# process the tickets
app.procesar_tickets()