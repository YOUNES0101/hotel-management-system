from django.contrib import admin
from .models import room, client, reservation


@admin.register(room)
class roomAdmin(admin.ModelAdmin):
    list_display = ('room_number', 'room_type', 'price_per_night', 'is_available')
    list_filter = ('room_type', 'is_available')
    search_fields = ('room_number',)

@admin.register(client)
class GuestAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone_number')
    search_fields = ('first_name', 'last_name', 'email')

@admin.register(reservation)
class reservationAdmin(admin.ModelAdmin):
    list_display = ('client', 'room', 'check_in_date', 'check_out_date')
    list_filter = ('check_in_date', 'check_out_date')
    search_fields = ('client__first_name', 'client__last_name', 'room__room_number')
    date_hierarchy = ('check_in_date')

