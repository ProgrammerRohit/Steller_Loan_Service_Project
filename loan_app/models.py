from django.db import models
import uuid
import datetime


# Create your models here.
def generate_application_number():
    from random import randint
    return f"SF{randint(10000000,99999999)}"

class LoanApplications(models.Model):
    PURPOSE_CHOICES = [
        ("business","Business Expenses"),
        ("debt","Debt Consolidation"),
	    ("education","Education Cost"),
	    ("emergencey","Emergencey Expenses"),
	    ("home","Home Improvements"),
	    ("one","One of Purchases"),
	    ("personal","Personal Expenses"),
	    ("travel","Travel Expenses"),
	    ("vehicle","Vehicle Expenses"),
	    ("weddinge_event","Weddings or Events")
    ]

    LOAN_AMOUNTS = [
        ("1000", "£1000"),
        ("1500", "£1500"),
        ("2000", "£2000"),
        ("2500", "£2500"),
        ("3000", "£3000"),
        ("3500", "£3500"),
        ("4000", "£4000"),
        ("4500", "£4500"),
        ("5000", "£5000"),
        ("5500", "£5500"),
        ("6000", "£6000"),
        ("6500", "£6500"),
        ("7000", "£7000"),
        ("7500", "£7500"),
        ("8000", "£8000"),
        ("8500", "£8500"),
        ("9000", "£9000"),
        ("9500", "£9500"),
        ("10000", "£10000"),
        ("10500", "£10500"),
        ("11000", "£11000"),
        ("11500", "£11500"),
        ("12000", "£12000"),
        ("12500", "£12500"),
        ("13000", "£13000"),
        ("13500", "£13500"),
        ("14000", "£14000"),
        ("14500", "£14500"),
        ("15000", "£15000"),
        ("15500", "£15500"),
        ("16000", "£16000"),
        ("16500", "£16500"),
        ("17000", "£17000"),
        ("17500", "£17500"),
        ("18000", "£18000"),
        ("18500", "£18500"),
        ("19000", "£19000"),
        ("19500", "£19500"),
        ("20000", "£20000"),
        ("20500", "£20500"),
        ("21000", "£21000"),
        ("21500", "£21500"),
        ("22000", "£22000"),
        ("22500", "£22500"),
        ("23000", "£23000"),
        ("23500", "£23500"),
        ("24000", "£24000"),
        ("24500", "£24500"),
        ("25000", "£25000"),
        ("25500", "£25500"),
        ("26000", "£26000"),
        ("26500", "£26500"),
        ("27000", "£27000"),
        ("27500", "£27500"),
        ("28000", "£28000"),
        ("28500", "£28500"),
        ("29000", "£29000"),
        ("29500", "£29500"),
        ("30000", "£30000"),
        ("30500", "£30500"),
        ("31000", "£31000"),
        ("31500", "£31500"),
        ("32000", "£32000"),
        ("32500", "£32500"),
        ("33000", "£33000"),
        ("33500", "£33500"),
        ("34000", "£34000"),
        ("34500", "£34500"),
        ("35000", "£35000"),
        ("35500", "£35500"),
        ("36000", "£36000"),
        ("36500", "£36500"),
        ("37000", "£37000"),
        ("37500", "£37500"),
        ("38000", "£38000"),
        ("38500", "£38500"),
        ("39000", "£39000"),
        ("39500", "£39500"),
        ("40000", "£40000"),
        ("40500", "£40500"),
        ("41000", "£41000"),
        ("41500", "£41500"),
        ("42000", "£42000"),
        ("42500", "£42500"),
        ("43000", "£43000"),
        ("43500", "£43500"),
        ("44000", "£44000"),
        ("44500", "£44500"),
        ("45000", "£45000"),
        ("45500", "£45500"),
        ("46000", "£46000"),
        ("46500", "£46500"),
        ("47000", "£47000"),
        ("47500", "£47500"),
        ("48000", "£48000"),
        ("48500", "£48500"),
        ("49000", "£49000"),
        ("49500", "£49500"),
        ("50000", "£50000"),
    ]

    TITLES = [
        ("mr","Mr"),
	    ("mrs","Mrs"),
	    ("miss","Miss"),
	    ("ms","Ms"),
	    ("dr","Dr.")
    ]

    MARTIAL_STATUS = [
        ("single","Single"),
	    ("married","Married"),
	    ("divorced","Divorced"),
	    ("separated","Separated"),
	    ("widowed","Widowed")
    ]

    EMPLOYEMENT_STATUS = [
        ("full","Full Time Employed"),
	    ("self","Self Employed"),
	    ("part","Part Time Employed"),
	    ("retired","Retired"),
	    ("benefits","Benefits"),
	    ("unemployed","Unemployed")
    ]
    application_number = models.CharField(max_length=20, unique=True, default=generate_application_number)

    # step 1: loan details
    loan_amount = models.CharField(max_length=10, choices=LOAN_AMOUNTS, null=False)
    purpose = models.CharField(max_length=50, choices=PURPOSE_CHOICES, null=False)

    # step 2: profile details
    title = models.CharField(max_length=30, choices=TITLES, null=False)
    first_name = models.CharField(max_length=20, null=False)
    middle_name = models.CharField(max_length=20, null=False)
    last_name = models.CharField(max_length=20, null=False)
    dob = models.DateField(default=datetime.date.today)
    email = models.EmailField(max_length=100, null=False)
    mobile = models.CharField(max_length=15, null=False)
    land_line = models.CharField(max_length=15, blank=True, null=True)
    

    # step 3: home details
    residental = models.CharField(max_length=100, blank=True, null=True)
    martial_status = models.CharField(max_length=50, choices=MARTIAL_STATUS, blank=True, null=True)
    dependents = models.IntegerField(blank=True, null=True)
    house_number = models.CharField(max_length=100, blank=True, null=True)
    street = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    postcode = models.CharField(max_length=20, blank=True, null=True)
    time_at_residence = models.CharField(max_length=100, blank=True, null=True)

    # step 4: employement details
    employement_status = models.CharField(max_length=50, choices=EMPLOYEMENT_STATUS, blank=True, null=True)
    company = models.CharField(max_length=50, blank=True, null=True)
    job_title = models.CharField(max_length=100, blank=True, null=True)
    year_of_employement = models.IntegerField(blank=True, null=True)
    monthly_income = models.IntegerField(blank=True, null=True)

    # step 5: bank details
    bank_name = models.CharField(max_length=100, blank=True, null=True)
    account_number = models.CharField(max_length=200, blank=True, null=True)
    sort_code = models.CharField(max_length=6, blank=True, null=True)

    provide_bank_details = models.BooleanField(default=True)
    completed = models.BooleanField(default=False)
    submitted_at = models.DateTimeField(auto_now_add=True)

class ContactUs(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email_address = models.EmailField(max_length=200)
    phone_number = models.CharField(max_length=15)
    subject = models.CharField(max_length=100)
    message = models.TextField(max_length=400)

class UpdateTips(models.Model):
    email = models.EmailField(max_length=200)