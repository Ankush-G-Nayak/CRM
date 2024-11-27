from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import Userform, Addcutstomer,Updatecutstomer
from .models import Record
# from datetime import timedelta
# from django.utils import timezone
# from django.core.mail import send_mail
from django.db import connection
def home(request):
    records = Record.objects.all()
    if request.method == 'POST':
        email = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You are logged in')
            return redirect('home')
        else:
            messages.error(request, 'Invalid credentials')
            return render(request, 'website/home.html')
    return render(request, 'website/home.html', {'records': records})

def register(request):
    if request.method == 'POST':
        form = Userform(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, 'You are registered...')
            return redirect('home')
    else:
        form = Userform()
    return render(request, 'website/register.html', {'form': form})

def logout_user(request):
    logout(request)
    messages.success(request, 'You are logged out...')
    return redirect('home')

def record(request, pk):
    if request.user.is_authenticated:
        crec = Record.objects.get(id=pk)
        return render(request, 'website/record.html', {'crec': crec})
    else:
        messages.success(request, 'You must be logged in to view Records')
        return redirect('home')

def delete(request, pk):
    if request.user.is_authenticated:
        drec = Record.objects.get(id=pk)
        drec.delete()
        messages.success(request, 'Record has been deleted')
        return redirect('home')

def addrec(request):
    form = Addcutstomer(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                messages.success(request, 'Record has been added')
                return redirect('home')
        return render(request, 'website/addrec.html', {'form': form})  # Ensure correct template here
    else:
        messages.success(request, 'You must be logged in to add Records')
        return redirect('home')

def updrec(request,pk):
    if request.user.is_authenticated:
        crec=Record.objects.get(id=pk)
        form = Updatecutstomer(request.POST or None,instance=crec)
        if form.is_valid():
            form.save()
            messages.success(request, 'Record has been updated')
            return redirect('home')
        return render(request, 'website/updrec.html', {'form': form})
    else:
        messages.success(request, 'You must be logged in to update Records')
        return redirect('home')

def reset_table(request):
    if request.user.is_authenticated:
        # Delete all records in the table
        Record.objects.all().delete()

        # Reset the auto-increment ID to 1 for MySQL
        with connection.cursor() as cursor:
            cursor.execute("ALTER TABLE website_record AUTO_INCREMENT = 1;")

        messages.success(request, 'All records have been deleted and ID reset to 1.')
        return redirect('home')
    else:
        messages.error(request, 'You must be logged in to perform this action.')
        return redirect('home')


# def send_email_notification(record):
#     subject = "3 Days Passed Since Record Creation"
#     message = f"A record has been created and it has been 3 days since its creation.\n\nRecord details:\nUsername: {record.username}\nEmail: {record.email}\nPhone: {record.PhNo}"
#     recipient_list = ['to@gmail.com']  # Replace with the recipient's email
#
#     # Sending the email
#     send_mail(subject, message, 'from@gmail.com', recipient_list)
#
# def check_and_send_email(record):
#     created_date = record.Created
#     current_date = timezone.now()
#
#     # Calculate the date difference
#     date_difference = current_date - created_date
#
#     # If the difference is exactly 3 days, send an email
#     if date_difference.days == 3:
#         send_email_notification(record)
