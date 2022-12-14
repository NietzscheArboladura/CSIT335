"""mydbproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp1 import views

app_name = 'myapp1'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index', views.MyIndexView.as_view(), name="my_index_view"),
    path('dashboard', views.DashboardView.as_view(), name="my_dashboard_view"),
    path('listOfBooking', views.listOfBookingsView.as_view(), name="my_bookings_view"),
    path('listOfPayment', views.listOfPaymentView.as_view(), name="my_Payment_view"),
    path('signin', views.signinView.as_view(), name="my_signin_view"),
    path('adminsignin', views.adminSigninView.as_view(), name="my_adminsignin_view"),
    path('signup', views.signupView.as_view(), name="my_signup_view"),
    path('adminSignup', views.adminSignupView.as_view(), name="my_adminSignup_view"),
]
