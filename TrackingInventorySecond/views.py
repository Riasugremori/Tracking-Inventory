from django.shortcuts import render, redirect
from .models import TrackingInventoryList

def main_text(request):
    if request.method == "POST":
        name = request.POST.get('name')
        serial_number = request.POST.get('SerialNumber')
        value = request.POST.get('value')


        TrackingInventoryList.objects.create(name=name, SerialNumber=serial_number, value=value)
        return redirect('main_text')


    inventory_items = TrackingInventoryList.objects.all()
    return render(request, 'tracking.html', {'inventory_items': inventory_items})

