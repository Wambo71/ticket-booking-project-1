from model import User, Event, Ticket, session

def add_user(first_name, last_name, phone):
    new_user = User(first_name=first_name, last_name=last_name, phone=phone)
    session.add(new_user)
    session.commit()
    print(f"{first_name} {last_name} added successfully")


def delete_user(user_id):
    user = session.query(User).filter_by(id=user_id).first()  # renamed variable
    if user:
        session.delete(user)
        session.commit()
        print(f"User ID {user_id} deleted successfully")
    else:
        print(f"User ID {user_id} not found")


def add_event(name, date, capacity):
    new_event = Event(name=name, date=date, capacity=capacity)
    session.add(new_event)
    session.commit()
    print(f"Event '{name}' added successfully")


def book_ticket(user_id, event_id):
    """Book a ticket if event still has space"""
    event = session.query(Event).filter_by(id=event_id).first()
    user = session.query(User).filter_by(id=user_id).first()

    if not event or not user:
        print(" Event or User not found.")
        return

    current_tickets = session.query(Ticket).filter_by(event_id=event_id).count()
    if current_tickets >= event.capacity:
        print("Event is fully booked.")
        return

    new_ticket = Ticket(user_id=user_id, event_id=event_id)
    session.add(new_ticket)
    session.commit()
    print(f" Ticket booked for {user.first_name} {user.last_name} to {event.name}")


def get_all_tickets():
    tickets = session.query(Ticket).all()   # call all()
    for ticket in tickets:
        print(f"Ticket {ticket.id}: {ticket.user.first_name} {ticket.user.last_name} "
              f"booked for {ticket.event.name} on {ticket.booked_at}")
