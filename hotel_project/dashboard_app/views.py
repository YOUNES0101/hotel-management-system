from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from hotel_app.models import reservation, room, CustomUser

# Home View
class DashboardHomeView(TemplateView):
    template_name = "dashboard_app/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_count'] = CustomUser.objects.count()
        context['reservation_count'] = reservation.objects.count()
        context['room_count'] = room.objects.count()
        return context


class UserListView(ListView):
    model = CustomUser
    template_name = "dashboard_app/users/list.html"
    context_object_name = "users"
    paginate_by = 10  # Number of users per page
    ordering = ['email']

    def get_queryset(self):
        return CustomUser.objects.all().order_by('email')

# Add a class-based view for creating users
class UserCreateView(CreateView):
    model = CustomUser
    template_name = "dashboard_app/users/add.html"
    fields = ['email','password', 'is_active', 'is_staff']
    success_url = reverse_lazy('users')  # Removed dashboard: namespace

    def form_valid(self, form):
        user = form.save(commit=False)
        # Set password properly
        user.set_password(form.cleaned_data['password'])
        user.save()
        return super().form_valid(form)

# Class-based views for editing and deleting users
class UserUpdateView(UpdateView):
    model = CustomUser
    template_name = "dashboard_app/users/edit.html"
    fields = ['email','is_active', 'is_staff']
    success_url = reverse_lazy('users')  # Removed dashboard: namespace

class UserDeleteView(DeleteView):
    model = CustomUser
    template_name = "dashboard_app/users/delete.html"
    success_url = reverse_lazy('users')  # Removed dashboard: namespace

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.get_object()
        return context

# Room Views
class RoomListView(ListView):
    model = room
    template_name = "dashboard_app/rooms/list.html"
    context_object_name = "room_list"
    paginate_by = 10
    ordering = ['room_number']

    def get_queryset(self):
        return room.objects.all().order_by('room_number')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add available room count to context
        context['available_count'] = room.objects.filter(is_available=True).count()
        return context

class RoomCreateView(CreateView):
    model = room
    template_name = "dashboard_app/rooms/add.html"
    fields = ['room_number', 'room_type', 'price_per_night', 'capacity', 'is_available', 'description', 'image']
    success_url = reverse_lazy('room_list')

class RoomUpdateView(UpdateView):
    model = room
    template_name = "dashboard_app/rooms/edit.html"
    fields = ['room_number', 'room_type', 'price_per_night', 'capacity', 'is_available', 'description', 'image']
    success_url = reverse_lazy('room_list')

class RoomDeleteView(DeleteView):
    model = room
    template_name = "dashboard_app/rooms/delete.html"
    success_url = reverse_lazy('room_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['room'] = self.get_object()
        return context

