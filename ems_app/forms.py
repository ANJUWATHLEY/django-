from django import forms
from ems_app.models import*
from django.contrib.auth.models import User
class EmployeeForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields=["name","age","salary"]

# class DepartmentForm(forms.ModelForm):
#     class Meta:
#         model=Department 
#         Fields=["name"]
class userForm(forms.ModelForm):
     class Meta:
         model = User
         fields = "__all__"
