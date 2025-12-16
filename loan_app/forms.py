from django import forms
from loan_app.models import LoanApplications, ContactUs, UpdateTips

class LoanForms(forms.ModelForm):
    class Meta:
        model = LoanApplications
        fields = ["loan_amount","purpose"]

class ProfileForms(forms.ModelForm):
    dob = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        label='Date of Birth'
    )
    class Meta:
        model = LoanApplications
        fields = ["title","first_name","middle_name","last_name","dob","email","mobile","land_line"]

class HomeForms(forms.ModelForm):
    class Meta:
        model = LoanApplications
        fields = ["martial_status","dependents","residental","house_number","street","city","postcode","time_at_residence"]

class EmployeForms(forms.ModelForm):
    class Meta:
        model = LoanApplications
        fields = ["employement_status","company","job_title","year_of_employement","monthly_income"]

class BankForms(forms.ModelForm):
    skip_bank = forms.BooleanField(required=False, label="I don’t want to provide bank details.")

    class Meta:
        model = LoanApplications
        fields = ['bank_name', 'account_number', 'sort_code', 'skip_bank']
    
    def clean(self):
        cleaned_data = super().clean()
        skip = cleaned_data.get('skip_bank')

        if not skip:
            for field in ['bank_name', 'account_number', 'sort_code']:
                if not cleaned_data.get(field):
                    self.add_error(field, 'This field is required.')
        return cleaned_data


class TermsForm(forms.Form):
    accept_terms = forms.BooleanField(
        required=True, 
        label="I accept the Terms and Conditions"
    )
    accept_privacy = forms.BooleanField(
        required=True, 
        label="I accept the Privacy Policy"
    )

class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ["first_name","last_name","email_address","phone_number","subject","message"]
        widgets = {
            "first_name": forms.TextInput(attrs={"placeholder": "First Name"}),
            "last_name": forms.TextInput(attrs={"placeholder": "Last Name"}),
            "email_address": forms.EmailInput(attrs={"placeholder": "Your Email"}),
            "phone_number": forms.TextInput(attrs={"placeholder": "Your Phone"}),
            "subject": forms.TextInput(attrs={"placeholder": "Subject"}),
            "message": forms.Textarea(attrs={"placeholder": "Message", "rows": 4}),
        }

class UpdateTipsForm(forms.ModelForm):
    class Meta:
        model = UpdateTips
        fields = ["email"]

class StatusCheckForm(forms.Form):
    application_number = forms.CharField(
        label="Enter your Application Number",
        max_length=20,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'e.g., SH*********'
        })
    )