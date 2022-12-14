# Generated by Django 3.2.6 on 2021-09-13 13:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admin_name', models.CharField(max_length=20)),
                ('admin_email', models.CharField(max_length=20)),
                ('admin_pass', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_id', models.CharField(max_length=10)),
                ('book_name', models.CharField(max_length=20)),
                ('book_date', models.CharField(max_length=20)),
                ('book_no_children', models.IntegerField()),
                ('book_no_adult', models.IntegerField()),
                ('book_depart', models.CharField(max_length=20)),
                ('book_return', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cust_id', models.CharField(max_length=10)),
                ('cust_fname', models.CharField(max_length=20)),
                ('cust_lname', models.CharField(max_length=20)),
                ('cust_pword', models.CharField(max_length=20)),
                ('cust_address', models.CharField(max_length=20)),
                ('cust_phone_number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pay_receipt', models.CharField(max_length=10)),
                ('pay_date', models.CharField(max_length=20)),
                ('pay_amount', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PaymentList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seqid', models.IntegerField()),
                ('book_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp1.booking')),
                ('cust_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp1.customer')),
                ('pay_receipt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp1.payment')),
            ],
        ),
        migrations.CreateModel(
            name='BookingList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seqid', models.IntegerField()),
                ('book_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp1.booking')),
                ('cust_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp1.customer')),
            ],
        ),
    ]
