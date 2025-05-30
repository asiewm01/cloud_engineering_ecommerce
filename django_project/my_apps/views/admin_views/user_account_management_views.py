from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test

# Admin check
def is_admin(user):
    return user.is_staff or user.is_superuser

# View: List All Users
@login_required
@user_passes_test(is_admin)
def user_list(request):
    users = User.objects.all()
    return render(request, 'admin/user_management/manage_user.html', {'users': users})

# View: User Details + Edit Form
@login_required
@user_passes_test(is_admin)
def user_detail(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        user.username = request.POST.get('username')
        user.email = request.POST.get('email')
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.save()
        messages.success(request, f'User "{user.username}" updated.')
        return redirect('user_detail', user_id=user.id)
    return render(request, 'admin/user_management/user_detail.html', {'user': user})

# View: Delete User
@login_required
@user_passes_test(is_admin)
def user_delete(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.delete()
    messages.success(request, 'User deleted successfully.')
    return redirect('user_list')

# Manage Users
@login_required
@user_passes_test(is_admin)
def manage_users(request):
    users = User.objects.all()
    return render(request, 'admin/user_management/manage_user.html', {'users': users})
