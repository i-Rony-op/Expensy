from django.shortcuts import render, redirect
from transacts.models import *


def index(request):
    obj = Transactions.objects.all()
    sum = 0
    for i in obj:
        sum += i.price
    return render(request, "index.html", {"obj": obj, "sum": sum})


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")
