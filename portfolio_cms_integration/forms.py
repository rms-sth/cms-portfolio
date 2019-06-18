from django import forms

from portfolio_app.models import Portfolio


class PortfolioWizardForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        # fields = ('poll', 'choice_text')
        exclude = []