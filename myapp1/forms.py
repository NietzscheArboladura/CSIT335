from django import forms
from .models import *

 

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('cust_fname', 'cust_lname')

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('book_name', 'book_date')

class AdminForm(forms.ModelForm):
    class Meta:
        model = Admin
        fields = '__all__'

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ('pay_date','pay_amount')

class PaymentListForms(forms.ModelForm):
    class Meta:
        model = PaymentList
        fields = '__all__'


class BookingListForm(forms.ModelForm):
    class Meta:
        model = BookingList
        fields = '__all__'


