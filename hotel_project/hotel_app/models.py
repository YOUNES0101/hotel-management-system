from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    username = None  # Remove the username field
    email = models.EmailField(unique=True)  # Make email the unique identifier

    USERNAME_FIELD = 'email'  # Set email as the unique identifier
    REQUIRED_FIELDS = []  # No additional required fields

    def __str__(self):
        return self.email


class room(models.Model):

    room_number = models.CharField(max_length=10, unique=True)
    room_type = models.CharField(max_length=50)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.room_type} - {self.room_number}"


class reservation(models.Model):

    client = models.ForeignKey( CustomUser, on_delete=models.CASCADE)
    room = models.ForeignKey(room, on_delete=models.CASCADE)
    check_in_date = models.DateField()
    check_out_date = models.DateField()

    def __str__(self):
        return f"Reservation by ( {self.client.last_name} {self.client.first_name} ) for {self.room.room_number}"

