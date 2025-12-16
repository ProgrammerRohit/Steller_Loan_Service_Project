from django.shortcuts import render, redirect, get_object_or_404
from loan_app.forms import LoanForms, ProfileForms, HomeForms, EmployeForms, BankForms, ContactUsForm, UpdateTipsForm, TermsForm, StatusCheckForm
from loan_app.models import LoanApplications
from django.utils.crypto import get_random_string
from django.contrib import messages
from django import forms
from django.utils import timezone
from datetime import timedelta

# Create your views here.
FORM_CLASSES = [LoanForms, ProfileForms, HomeForms, EmployeForms, BankForms, TermsForm]

def generate_unique_application_number():
    """Ensure SF######## is unique"""
    while True:
        number = f"SF{get_random_string(length=8, allowed_chars='0123456789')}"
        if not LoanApplications.objects.filter(application_number=number).exists():
            return number

def loan_step(request, step):
    step = int(step)
    FormClass = FORM_CLASSES[step - 1]

    app_id = request.session.get('loan_app_id')
    if not app_id and step == 1:
        application = LoanApplications.objects.create(application_number=generate_unique_application_number())
        request.session['loan_app_id'] = application.id
    else:
        application = get_object_or_404(LoanApplications, id=app_id)

    if issubclass(FormClass, forms.ModelForm):
        form = FormClass(request.POST or None, instance=application)
    else:
        form = FormClass(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            if isinstance(form, forms.ModelForm):
                form.save()

            if "next" in request.POST and step < len(FORM_CLASSES):
                return redirect("loan_step", step=step + 1)
            elif "previous" in request.POST and step > 1:
                return redirect("loan_step", step=step - 1)
            elif step == len(FORM_CLASSES):
                application.completed = True
                application.save()
                if "loan_app_id" in request.session:
                    del request.session["loan_app_id"]
                return render(request, "loan_app/success.html", {"app_number": application.application_number})

    return render(request, "loan_app/apply_now.html", {"form": form, "step": step})

def loan_success(request):
    return render(request, 'loan_app/success.html')

def home(request):
    return render(request, 'loan_app/index.html')

def about(request):
    return render(request, 'loan_app/about.html')

def contact(request):
    contact_form = ContactUsForm(request.POST or None)
    if request.method == "POST" and contact_form.is_valid():
        contact_form.save()
        messages.success(request, "Your message has been sent successfully! We will get back to you soon.")
        contact_form = ContactUsForm()

    tips_form = UpdateTipsForm()
    return render(request, "loan_app/contact.html", {
        "contact_form": contact_form,
        "form": tips_form,
    })

def privacy_policies(request):
    return render(request, 'loan_app/privacy_policies.html')

def terms_and_conditions(request):
    return render(request, 'loan_app/terms_and_conditions.html')

def submit_tips_email(request):
    if request.method == "POST":
        form = UpdateTipsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thank you for subscribing!")
        else:
            messages.error(request, "Please enter a valid email.")
    return redirect(request.META.get("HTTP_REFERER", "/"))

def check_status_view(request):
    message = None
    application = None

    if request.method == 'POST':
        form = StatusCheckForm(request.POST)
        if form.is_valid():
            app_number = form.cleaned_data['application_number']
            try:
                application = LoanApplications.objects.get(application_number=app_number)
                time_diff = timezone.now() - application.submitted_at

                if time_diff < timedelta(hours=5):
                    message = 'under_review'
                else:
                    message = 'rejected'

            except LoanApplications.DoesNotExist:
                message = 'not_found'
    else:
        form = StatusCheckForm()

    return render(request, 'loan_app/check_status.html', {
        'check_status_form': form,
        'message': message,
        'application': application,
    })

def business_expense_loan(request):
    return render(request, 'loan_app/business_expense_loan.html')

def debt_consolidation_loan(request):
    return render(request, 'loan_app/debt_consolidation_loan.html')

def education_cost_loan(request):
    return render(request, 'loan_app/education_cost_loan.html')

def emergency_expense_loan(request):
    return render(request, 'loan_app/emergency_expense_loan.html')

def home_improvement_loan(request):
    return render(request, 'loan_app/home_improvement_loan.html')

def one_of_purchase_loan(request):
    return render(request, 'loan_app/one_of_purchase_loan.html')

def personal_expense_loan(request):
    return render(request, 'loan_app/personal_expense_loan.html')

def travel_expense_loan(request):
    return render(request, 'loan_app/travel_expense_loan.html')

def vehicle_expense_loan(request):
    return render(request, 'loan_app/vehicle_expense_loan.html')

def wedding_event_loan(request):
    return render(request, 'loan_app/wedding_event_loan.html')
