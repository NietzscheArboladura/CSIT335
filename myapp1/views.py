# from django.shortcuts import render
# from django.views.generic import  View
# from .forms import *
# # Create your views here.

 

# class MyIndexView(View):
#     def get(self,request):
#         return render(request, 'index.html')

 

# class DashboardView(View):
#     def get(self,request):
#         cust = Customer.objects.all()
#         book = Booking.objects.all()
#         admin = Admin.objects.all()
#         context = {
#             'customers' : cust,
#             'booking' : book,
#             'admin' : admin,

#         }
#         return render(request, 'dashboard.html', context)

from django.shortcuts import render,redirect
from django.views.generic import  View
from .forms import *
from django.http import HttpResponse
from .forms import *
from .models import *

# Create your views here.

class MyIndexView(View):
    def get(self,request):
        return render(request, 'index.html')

class DashboardView(View):
    def get(self,request):
        book = Booking.objects.all()
        pay = Payment.objects.all()
        return render(request, 'dashboard.html',{ "bookings" : book, "payments" : pay})

    def post(self,request):
					if request.method == 'POST':	
						if 'btnUpdate' in request.POST:	
							print('update profile button clicked')
							pid = request.POST.get("booking-id")			
							book_name = request.POST.get("booking-book_name")
							book_date = request.POST.get("booking-book_date")
							book_no_children = request.POST.get("booking-book_no_children")
							book_no_adult = request.POST.get("booking-book.book_no_adult")
							book_depart = request.POST.get("booking-book_depart")
							book_return = request.POST.get("booking-book_return")
							print(book_return)
				# email = request.POST.get("student-email")
				# phone = request.POST.get("student-phone")
							update_Booking = Booking.objects.filter(id = pid).update(book_name = book_name, book_date = book_date, book_no_children = book_no_children, book_no_adult = book_no_adult, 
							book_depart = book_depart, book_return = book_return)
							print(update_Booking)
							print('profile updated')
						elif 'btnDelete' in request.POST:
							print('delete button clicked')
						pid = request.POST.get("bbooking-id")
						pay = Booking.objects.filter(id = pid).delete()
						print('Booking deleted')
						# return HttpResponse ('post')
						# return redirect('my_dashboard_view')
	
					if request.method == 'POST':
						if 'btnUpdate1' in request.POST:	
							print('update profile button clicked')
							pid = request.POST.get("pay-id")			
							pay_receipt = request.POST.get("pay-pay_receipt")
							pay_date = request.POST.get("pay-pay_date")
							pay_amount = request.POST.get("pay-pay_amount")
							
							print(pay_amount)
				# email = request.POST.get("student-email")
				# phone = request.POST.get("student-phone")
							update_Payment = Payment.objects.filter(id = pid).update(pay_receipt = pay_receipt, pay_date = pay_date,  pay_amount = pay_amount )
							print(update_Payment)
							print('profile updated')
						elif 'btnDelete1' in request.POST:
							print('delete button clicked')
							pid = request.POST.get("ppay-id")
							pay = Payment.objects.filter(id = pid).delete()
						print('Payment deleted')
						# return HttpResponse ('post')
						return redirect('my_dashboard_view')
						

class listOfBookingsView(View):
	def get(self, request):
		return render(request, 'listOfBooking.html')

	def post(self, request):		
		form = BookingForm(request.POST)		
		# fname = request.POST.get("firstname")
		# print(fname)
		# lname = request.POST.get("lastname")
		# print(lname)
		if form.is_valid():
			# try:
			destination = request.POST.get("book_name")
			date = request.POST.get("book_date")
			child = request.POST.get("book_no_children")
			adult = request.POST.get("book_no_adult")
			depart = request.POST.get("book_depart")
			return1 = request.POST.get("book_return")

			form = Booking(book_name = destination, book_date = date, book_no_children = child, book_no_adult = adult, 
            book_depart = depart, book_return = return1)
			form.save()

            
			#return HttpResponse('Student record saved!')			
			return redirect('my_dashboard_view')
			# except:
			# 	raise Http404
		else:
			print(form.errors)
			return HttpResponse('not valid')

class listOfPaymentView(View):
	def get(self, request):
		return render(request, 'listOfPayment.html')

	def post(self, request):		
		form = PaymentForm(request.POST)		
		# fname = request.POST.get("firstname")
		# print(fname)
		# lname = request.POST.get("lastname")
		# print(lname)
		if form.is_valid():
			# try:
			receipt = request.POST.get("pay_receipt")
			date = request.POST.get("pay_date")
			amount = request.POST.get("pay_amount")
			

			form = Payment(pay_receipt = receipt, pay_date = date, pay_amount = amount)
			form.save()

            
			#return HttpResponse('Student record saved!')			
			return redirect('my_dashboard_view')
			# except:
			# 	raise Http404
		else:
			print(form.errors)
			return HttpResponse('not valid')

class signinView(View):
    def get(self,request):
        return render(request, 'signin.html')

class adminSigninView(View):
    def get(self,request):
        return render(request, 'adminsignin.html')

class signupView(View):
	def get(self, request):
		return render(request, 'signup.html')

	def post(self, request):		
		form = CustomerForm(request.POST)		
		# fname = request.POST.get("firstname")
		# print(fname)
		# lname = request.POST.get("lastname")
		# print(lname)
		if form.is_valid():
			# try:
			cust_fname = request.POST.get("cust_fname")
			cust_lname = request.POST.get("cust_lname")
			cust_address = request.POST.get("cust_address")
			cust_phone_number = request.POST.get("cust_phone_number")
			cust_pword = request.POST.get("cust_pword")
			
			print(cust_phone_number)
			# course = request.POST.get("course")
			# year = request.POST.get("year")
			form = Customer(cust_fname = cust_fname, cust_lname = cust_lname, cust_address = cust_address, 
			cust_phone_number = cust_phone_number, cust_pword = cust_pword)
			form.save()	

			#return HttpResponse('Student record saved!')			
			return redirect('my_dashboard_view')
			# except:
			# 	raise Http404
		else:
			print(form.errors)
			return HttpResponse('not valid')

class adminSignupView(View):
	def get(self, request):
		return render(request, 'adminSignup.html')

	def post(self, request):		
		form = AdminForm(request.POST)		
		# fname = request.POST.get("firstname")
		# print(fname)
		# lname = request.POST.get("lastname")
		# print(lname)
		if form.is_valid():
			# try:
			admin_name = request.POST.get("admin_name")
			admin_email = request.POST.get("admin_email")
			admin_pass = request.POST.get("admin_pass")
			

			form = Admin(admin_name = admin_name, admin_email = admin_email, admin_pass = admin_pass)
			form.save()

            
			#return HttpResponse('Student record saved!')			
			return redirect('my_dashboard_view')
			# except:
			# 	raise Http404
		else:
			print(form.errors)
			return HttpResponse('not valid')



	