from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import get_list_or_404, get_object_or_404                             
from .models import Inventory
from .forms import Form
from .forms import CsvsModelForm
from .filter1 import InventoryFilter
from .models import Csvs 
from datetime import datetime


import csv
from django.contrib.auth.models import User

def upload_file(request):
    form= CsvsModelForm(request.POST or None , request.FILES or None)
    if form.is_valid():
        form.save()
        form=CsvsModelForm()
        obj=Csvs.objects.filter(activated=False).first()
        with open(obj.file_name.path, 'r',encoding='windows-1252') as f:
            reader=csv.reader(f)
            for i, row in enumerate(reader):
                if i==0:
                    pass
                else:
                    inv = Inventory.objects.create(
                            Make = row[0],
                            Part_Code=row[1],
                            Serial_Number=row[2],
                            Item=row[3],
                            Location=row[4],
                            Purchase_Date=None if not row[5] else row[5],
                            Item_dispatched_Date=None if not row[6] else row[6],
                            OrgId=row[7],
                            Status=row[8],
                            Slip=row[9])
                    inv.save()
        obj.activated=True
        obj.save()
    return render(request,'upload.html',{'form':form})

'''def show_product(request):
    return HttpResponse()'''


def create_view(request):
    
    context ={}
 
    form = Form(request.POST or None,request.FILES or None)
    print(form.is_valid())
    if form.is_valid():
        form.save()
         
    context['form']= form
    return render(request, "create_view.html", context)


def update_view(request,pk):

	order = Inventory.objects.get(Serial_Number=pk)
	form = Form(instance=order)

	if request.method == 'POST':
		form = Form(request.POST, instance=order)
		if form.is_valid():
			form.save()
			return redirect('/update_view/'+pk)

	context = {'form':form}
	return render(request, 'create_view.html', context)

def showInventory(request):
    all_inventory = Inventory.objects.all()
    Inven_filter = InventoryFilter(request.GET, queryset=all_inventory)
    all_inventory=Inven_filter.qs 
    context = {'inventories': all_inventory, 'filter': Inven_filter}
    return render(request,'inven_show.html', context)



def deleteOrder(request, pk):
	order = Order.objects.get(id=pk)
	if request.method == "POST":
		order.delete()
		return redirect('/')

	context = {'item':order}
	return render(request, 'create_view.html', context)
    


  