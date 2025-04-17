# from django.shortcuts import render, get_object_or_404, redirect
# from .forms import UserForm
# # from django.shortcuts import render
# # from django.contrib.auth.models import User
# from hotel_app.models import reservation, room ,CustomUser  # Assuming these models exist

# def dashboard_home(request):
#     return render(request, 'dashboard_app/home.html')

# def manage_reservations(request):
#     reservations = reservation.objects.all()
#     return render(request, 'dashboard_app/manage_reservations.html', {'reservations': reservations})

# def manage_rooms(request):
#     rooms = room.objects.all()
#     return render(request, 'dashboard_app/manage_rooms.html', {'rooms': rooms})


# def manage_users(request):
#     users = CustomUser.objects.all()
#     return render(request, 'dashboard_app/manage_users.html', {'users': users})

# def add_user(request):
#     if request.method == 'POST':
#         form = UserForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('manage_users')
#     else:
#         form = UserForm()
#     return render(request, 'dashboard_app/add_user.html', {'form': form})

# def edit_user(request, user_id):
#     user = get_object_or_404(CustomUser, id=user_id)
#     if request.method == 'POST':
#         form = UserForm(request.POST, instance=user)
#         if form.is_valid():
#             form.save()
#             return redirect('manage_users')
#     else:
#         form = UserForm(instance=user)
#     return render(request, 'dashboard_app/edit_user.html', {'form': form})

# def delete_user(request, user_id):
#     user = get_object_or_404(CustomUser, id=user_id)
#     if request.method == 'POST':
#         user.delete()
#         return redirect('manage_users')
#     return render(request, 'dashboard_app/delete_user.html', {'user': user})



from django.shortcuts import render, redirect
from hotel_app.models import CustomUser
from .forms import CustomUserForm
def dashboard(request):

    CustomUser_count = CustomUser.objects.count()  # Count total users
    # You can also get booking and revenue stats here
    return render(request, 'dashboard_app/home.html', {'user_count': CustomUser_count})


def manage_reservations(request):
    return render(request, 'dashboard_app/manage_reservations.html')


def settings(request):
    return render(request, 'settings.html')




def manage_users(request):
    users = CustomUser.objects.all()  # You can filter or order if needed
    return render(request, 'dashboard_app/manage_users.html', {'users': users})





def add_user_view(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manage_users')  # Replace with your actual user management page
    else:
        form = CustomUserForm()
    return render(request, 'dashboard_app/add_user.html', {'form': form})



def home_view(request):
    signup_form = CustomUserCreationForm(data=request.POST or None)  # Create or bind the form

    if request.method == "POST" and signup_form.is_valid():
        signup_form.save()  # Save the user if the form is valid
        messages.success(request, "Your account has been created successfully!")
        return redirect('home')  # Redirect to the home page

    context = {
        'signup_form': signup_form,  # Pass the form to the template
    }
    return render(request, 'hotel_app/home.html', context)

