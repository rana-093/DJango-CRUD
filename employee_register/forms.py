from django import forms
from django.forms import fields
from .models import Employee


class EmployeeFrom(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ('fullName', 'emp_code', 'mobile', 'position')
        labels = {
            'fullName': 'Full Name',
            'emp_code': 'EMP CODE'
        }

    def __init__(self, *args, **kwargs):
        super(EmployeeFrom, self).__init__(*args, **kwargs)
        self.fields['position'].empty_label = "Select"
        self.fields['emp_code'].required = False
