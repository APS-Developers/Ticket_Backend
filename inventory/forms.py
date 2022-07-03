from django import forms
from .models import Inventory
from .models import Csvs
 
# creating a form
class Form(forms.ModelForm):
 
    # create meta class
    class Meta:
        # specify model to be used
        model = Inventory
 
        # specify fields to be used
        fields = [
            'Make',
            'Part_Code',
            'Serial_Number',
            'Item',
            'Location',
            'Purchase_Date',
            'Item_dispatched_Date',
            'OrgId',
            'Status',
            'Slip',
        ]



class CsvsModelForm(forms.ModelForm):
	class Meta:
		model=Csvs
		fields=("file_name",)







