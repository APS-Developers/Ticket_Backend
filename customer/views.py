from django.shortcuts import redirect, render
from customer.filters import CustomerFilter
from .models import *
from .forms import CreateCustomerForm, CreateOrganisationForm
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='login')
def createCustomer(request):
    form = CreateCustomerForm()
    if request.method == 'POST':
        form = CreateCustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('showCustomer')
    context = {'form': form, 'type': 'Customer'}
    return render(request, 'customer/create.html', context)


@login_required(login_url='login')
def createOrganisation(request):
    form = CreateOrganisationForm()
    if request.method == 'POST':
        form = CreateOrganisationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('showOrganisation')
    context = {'form': form, 'type': 'Organisation'}
    return render(request, 'customer/create.html', context)


@login_required(login_url='login')
def showCustomer(request):
    all_customers = Customer.objects.all()
    customer_filter = CustomerFilter(request.GET, queryset=all_customers)
    all_customers = customer_filter.qs
    context = {'all_customers': all_customers, 'type': 'Customer', 'customer_filter': customer_filter}
    return render(request, 'customer/show.html', context)


@login_required(login_url='login')
def showOrganisation(request):
    all_organisations = Organisation.objects.all()
    context = {'all_organisations': all_organisations, 'type': 'Organisation'}
    return render(request, 'customer/show.html', context)


@login_required(login_url='login')
def updateCustomer(request, pk):
    customer = Customer.objects.get(CustomerID=pk)
    form = CreateCustomerForm(instance=customer)

    if request.method == 'POST':
        form = CreateCustomerForm(request.POST, instance=customer)

        if form.is_valid():
            form.save()
            return redirect('showCustomer')

    context = {'form': form, 'type': 'Customer'}
    return render(request, 'customer/update.html', context)
    

@login_required(login_url='login')
def updateOrganisation(request, pk):
    organisation = Organisation.objects.get(OrgID=pk)
    form = CreateOrganisationForm(instance=organisation)

    if request.method == 'POST':
        form = CreateOrganisationForm(request.POST, instance=organisation)

        if form.is_valid():
            organisation = form.save()
            return redirect('showOrganisation')

    context = {'form': form, 'type': 'Organisation'}
    return render(request, 'customer/update.html', context)


@login_required(login_url='login')
def deleteCustomer(request, pk):
        customer = Customer.objects.get(CustomerID=pk)

        if request.method == 'POST':
            customer.delete()
            return redirect('showCustomer')

        context = {'customer': customer, 'type': 'Customer'}
        return render(request, 'customer/delete.html', context)


@login_required(login_url='login')
def deleteOrganisation(request, pk):
        organisation = Organisation.objects.get(OrgID=pk)

        if request.method == 'POST':
            organisation.delete()
            return redirect('showOrganisation')

        context = {'organisation': organisation, 'type': 'Organisation'}
        return render(request, 'customer/delete.html', context)
