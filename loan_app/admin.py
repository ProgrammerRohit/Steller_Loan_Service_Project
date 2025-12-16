from django.contrib import admin
from loan_app.models import LoanApplications, ContactUs, UpdateTips

# Register your models here.
@admin.register(LoanApplications)
class LoanApplicationAdmin(admin.ModelAdmin):
    list_display = [
        "loan_amount",
        "purpose",
        "title",
        "first_name",
        "middle_name",
        "last_name",
        "dob",
        "email",
        "mobile",
        "land_line",
        "martial_status",
        "dependents",
        "residental",
        "house_number",
        "street",
        "city",
        "postcode",
        "time_at_residence",
        "employement_status",
        "company",
        "job_title",
        "year_of_employement",
        "monthly_income",
        "bank_name",
        "account_number",
        "sort_code"
    ]

@admin.register(ContactUs)
class ContactAdmin(admin.ModelAdmin):
    list_display = ["first_name","last_name","email_address","phone_number","subject","message"]

@admin.register(UpdateTips)
class UpdateTipsAdmin(admin.ModelAdmin):
    list_display = ["email"]