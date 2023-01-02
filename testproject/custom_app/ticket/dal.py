from ticket import models


def search(title: str, email: str) -> models.Ticket:
    """Searches ticket by title."""

    return models.Ticket.objects.filter(
        title__startswith=title, client__email__startswith=email
    ).values().order_by('-id')


def save(title: str, description: str, client_id: int, agent_id: int) -> models.Ticket:
    """Searches ticket by title."""

    return models.Ticket.objects.create(
        title=title, description=description, client_id=client_id, agent_id=agent_id
    )

