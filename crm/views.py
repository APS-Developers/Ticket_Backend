from django.shortcuts import redirect, render
from .models import Ticket
from customer.models import Customer, Organisation
from .forms import ProductForm, FaultForm, UpdateForm
from customer.forms import CreateCustomerForm
from .filters import TicketFilter
from django.contrib import messages

# Create your views here.


def customerDetails(request):
    form = CreateCustomerForm()
    if request.method == 'POST':
        form = CreateCustomerForm(request.POST)
        if form.is_valid():
            customerForm = form.save(commit=False)
            customer = Customer.objects.filter(ContactNo=form.cleaned_data.get('ContactNo'),
            Organisation=form.cleaned_data.get('Organisation'), 
            Name=form.cleaned_data.get('Name'), 
            EmailAddress=form.cleaned_data.get('EmailAddress'))

            if not customer.exists():
                allContactNos = list(Customer.objects.values('ContactNo').distinct())
                for i in range(len(allContactNos)):
                    if form.cleaned_data.get('ContactNo') == allContactNos[i]['ContactNo']:
                        messages.error(request, 'Customer with this contact number already exists!')
                        return redirect('customerDetails')

                customerForm.save()
                return redirect('/productDetails/' + str(customerForm.CustomerID))
            
            
            return redirect('/productDetails/' + str(customer[0].CustomerID))
    context = {'form': form}
    return render(request, 'customer/create.html', context)


def productDetails(request, customerID):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            newTicket = form.save(commit=False)
            newTicket.Customer_id = customerID
            newTicket.Status = 'Open'
            newTicket.save()
            return redirect('/faultDetails/' + str(newTicket.TicketID))
    context = {'form': form}
    return render(request, 'crm/create.html', context)


def faultDetails(request, ticketID):
    form = FaultForm()
    if request.method == 'POST':
        form = FaultForm(request.POST)
        if form.is_valid():
            fault = form.save(commit=False)
            ticket = Ticket.objects.get(TicketID=ticketID)
            ticket.Priority = form.cleaned_data.get('Priority')
            ticket.FaultFoundCode = fault.FaultFoundCode
            ticket.ResolutionCode = fault.ResolutionCode
            ticket.ResolutionRemarks = fault.ResolutionRemarks
            ticket.OnlineResolvable = fault.OnlineResolvable
            ticket.save()
            return redirect('showTickets')
    context = {'form': form}
    return render(request, 'crm/create.html', context)


def showTickets(request):
    all_tickets = Ticket.objects.all()
    ticket_filter = TicketFilter(request.GET, queryset=all_tickets)
    all_tickets = ticket_filter.qs
    context = {'all_tickets': all_tickets, 'ticket_filter': ticket_filter}
    return render(request, 'crm/show.html', context)


def updateTicket(request, ticketID):
    ticket = Ticket.objects.get(TicketID=ticketID)
    form = UpdateForm(instance=ticket)

    if request.method == 'POST':
        form = UpdateForm(request.POST, instance=ticket)

        if form.is_valid():
            form.save()
            return redirect('showTickets')
            
    context = {'form': form}
    return render(request, 'crm/update.html', context)


def deleteTicket(request, ticketID):
    ticket = Ticket.objects.get(TicketID=ticketID)

    if request.method == 'POST':
        ticket.delete()
        return redirect('showTickets')

    context = {'ticket': ticket}
    return render(request, 'crm/delete.html', context)


    # show ticket ka nme se kia , int str se farak?
    # update, autofill, contact vala, 
    # .models matlab sare models ?

    # org 