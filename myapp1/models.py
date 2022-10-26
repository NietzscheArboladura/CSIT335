from django.db import models

 

# Create your models here.

 

class Customer(models.Model):
    cust_id = models.CharField(max_length = 10)
    cust_fname = models.CharField(max_length = 20)
    cust_lname = models.CharField(max_length = 20)
    cust_pword = models.CharField(max_length = 20)
    cust_address = models.CharField(max_length = 20)
    cust_phone_number = models.IntegerField()

 

    class meta:
        db_table = 'Customer'

 

class Booking(models.Model):
    book_id = models.CharField(max_length = 10)
    book_name = models.CharField(max_length = 20)
    book_date = models.CharField(max_length = 20)
    book_no_children = models.IntegerField()
    book_no_adult =models.IntegerField()
    book_depart =models.CharField(max_length = 20)
    book_return = models.CharField(max_length = 20)

 


class BookingList(models.Model):
    seqid = models.IntegerField()
    cust_id = models.ForeignKey(Customer, on_delete = models.CASCADE)
    book_id = models.ForeignKey(Booking, on_delete = models.CASCADE)

 

class Payment(models.Model):
    pay_receipt = models.CharField(max_length = 10)
    pay_date = models.CharField(max_length = 20)
    pay_amount = models.IntegerField()

 

class PaymentList(models.Model):
    seqid = models.IntegerField()
    cust_id = models.ForeignKey(Customer, on_delete = models.CASCADE)
    book_id = models.ForeignKey(Booking, on_delete = models.CASCADE)
    pay_receipt = models.ForeignKey(Payment, on_delete = models.CASCADE)
    
class Admin(models.Model):
    admin_name =models.CharField(max_length = 20)
    admin_email = models.CharField(max_length = 20)
    admin_pass =models.CharField(max_length = 20)