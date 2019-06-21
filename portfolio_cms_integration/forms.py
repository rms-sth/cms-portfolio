from django import forms

from portfolio_app.models import Portfolio, Project, Blog


class PortfolioWizardForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        # fields = ('poll', 'choice_text')
        exclude = []

class ProjectoWizardForm(forms.ModelForm):
    class Meta:
        model = Project
        # fields = ('poll', 'choice_text')
        exclude = []

class BlogWizardForm(forms.ModelForm):
    class Meta:
        model = Blog
        # fields = ('poll', 'choice_text')
        exclude = []