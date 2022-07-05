from django.forms import ModelForm
from .models import Ticket


class ProductForm(ModelForm):

    class Meta:
        model = Ticket
        fields = ['DateCreated', 'Category', 'SubCategory', 'ModelNo', 'SerialNo', 'Summary']


class FaultForm(ModelForm):

    class Meta:
        model = Ticket
        fields = ['Priority', 'FaultFoundCode', 'ResolutionCode', 'ResolutionRemarks', 'OnlineResolvable']


class UpdateForm(ModelForm):

    class Meta:
        model = Ticket
        fields = '__all__'