
import uuid

from django.db import models
from django.contrib.auth.models import User
from apps.organizations.models import Organization


class Ticket(models.Model):

    class Status(models.TextChoices):
        OPEN = "OPEN", "Aberto"
        IN_PROGRESS = "IN_PROGRESS", "Em atendimento"
        WAITING = "WAITING", "Aguardando"
        RESOLVED = "RESOLVED", "Resolvido"
        CLOSED = "CLOSED", "Fechado"

    class Priority(models.TextChoices):
        LOW = "LOW", "Baixa"
        MEDIUM = "MEDIUM", "Média"
        HIGH = "HIGH", "Alta"
        URGENT = "URGENT", "Urgente"

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        related_name="tickets"
    )

    title = models.CharField(max_length=200)
    description = models.TextField()

    requester = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name="requested_tickets"
    )

    assigned_to = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="assigned_tickets"
    )

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.OPEN
    )

    priority = models.CharField(
        max_length=20,
        choices=Priority.choices,
        default=Priority.MEDIUM
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        indexes = [
            models.Index(fields=["organization", "status"]),
            models.Index(fields=["organization", "created_at"]),
        ]

    def __str__(self):
        return self.title


class Comment(models.Model):

    ticket = models.ForeignKey(
        Ticket,
        on_delete=models.CASCADE,
        related_name="comments"
    )

    author = models.ForeignKey(
        User,
        on_delete=models.PROTECT
    )

    message = models.TextField()
    is_internal = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_at"]

    def __str__(self):
        return f"Comentário em {self.ticket.title}"

