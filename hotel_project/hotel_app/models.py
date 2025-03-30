from django.db import models

# Create your models here.

class client(models.Model):
    """
    Model representing a client in the hotel management system.
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.name +" (" + self.email + ")"


class room(models.Model):
    """
    Model representing a room in the hotel.
    """
    id = models.AutoField(primary_key=True)
    room_number = models.CharField(max_length=10, unique=True)
    room_type = models.CharField(max_length=50)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.room_type} - {self.room_number}"


class reservation(models.Model):
    """
    Model representing a reservation made by a client.
    """
    client = models.ForeignKey(client, on_delete=models.CASCADE)
    room = models.ForeignKey(room, on_delete=models.CASCADE)
    check_in_date = models.DateField()
    check_out_date = models.DateField()

    def __str__(self):
        return f"Reservation by {self.client.name} for {self.room.room_number}"

