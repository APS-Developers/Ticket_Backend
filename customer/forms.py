from django.forms import ModelForm
from .models import Customer, Organisation


class CreateCustomerForm(ModelForm):

    class Meta:
        model = Customer
        fields = ['Name', 'Organisation', 'ContactNo', 'EmailAddress']


class CreateOrganisationForm(ModelForm):

    class Meta:
        model = Organisation
        fields = ['Name', 'ContactNo', 'EmailAddress', 'Address']

