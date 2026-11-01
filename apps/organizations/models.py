
from django.db import models
from django.contrib.auth.models import User


class Organization(models.Model):
    name = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Membership(models.Model):

    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Administrador"
        TECHNICIAN = "TECHNICIAN", "Técnico"
        REQUESTER = "REQUESTER", "Solicitante"

    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        related_name="memberships"
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="memberships"
    )

    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.REQUESTER
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["organization", "user"],
                name="unique_organization_user"
            )
        ]

    def __str__(self):
        return f"{self.user.username} - {self.organization.name}"

