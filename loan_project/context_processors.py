from loan_app.forms import UpdateTipsForm

def update_tips_forms(request):
    return {
        "tips_form": UpdateTipsForm()
    }