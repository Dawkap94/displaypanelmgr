from django.db import models
from users.models import CustomUser

class Website(models.Model):
    STATUS_CHOICES = (
        ('online', 'Online'),
        ('offline', 'Offline'),
    )
    owner = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='urls',
        verbose_name='User'
    )
    address = models.URLField(
        max_length=255,
        verbose_name='Url address'
    )
    status = models.CharField(
        max_length=7,
        choices=STATUS_CHOICES,
        default='offline',
        verbose_name='Status'
    )

    last_checked = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name='Last checked at'
    )

    def __str__(self):
        return f"{self.address} (status: {self.status})"

