



from base_class.ticket.type import Ticket


class TicketRecord(Ticket):

    def __init__(self):
        
        ticket:Ticket = Ticket.get_instance()
        Ticket.__init__(self, ticket.get_id(),ticket.get_create_time())
        
        pass
        
    pass
        