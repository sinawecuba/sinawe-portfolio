from django.shortcuts import render, redirect, get_object_or_404
from .models import User
from userapp.forms import UserForm

# List all users
def user_list(request):
    records = User.objects.all()
    context = {'records': records}
    return render(request, 'Listingpage.html', context)

# Add a new user
def AddUser(request):
    form = UserForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('/')  # redirect to list page

    context = {'form': form}
    return render(request, 'Add.html', context)

# Edit an existing user
def EditUser(request, id=None):
    one_rec = get_object_or_404(User, pk=id)
    form = UserForm(request.POST or None, request.FILES or None, instance=one_rec)
    if form.is_valid():
        form.save()
        return redirect('/')
    context = {'form': form}
    return render(request, 'Edit.html', context)

# Delete a user
def DeleteUser(request, eid=None):
    one_rec = get_object_or_404(User, pk=eid)
    if request.method == "POST":
        one_rec.delete()
        return redirect('/')
    context = {'user': one_rec}
    return render(request, 'Delete.html', context)

# View user details
def ViewUser(request, eid=None):
    one_rec = get_object_or_404(User, pk=eid)
    context = {'user': one_rec}
    return render(request, 'View.html', context)
