from django.shortcuts import render
from django.contrib import messages
# Create your views here.

from app.models import Form

def form(request):

    if request.method == "POST":

        email=request.POST.get('email')
        phone=request.POST.get('phone')

        con=Form(email=email, phone=phone)
        con.save()

        messages.success(request, "Successfully sent...")

    return render(request, 'form.html')


