from django import forms
from .models import Company, Jobs
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget
from django_countries.data import COUNTRIES
class CompanyForm(forms.ModelForm):
    # country = CountryField(blank=True).formfield(widget=CountrySelectWidget(
    #        attrs={"class": "chosen"}
    #     ))
    country = forms.ChoiceField(choices = sorted(COUNTRIES.items()))

    class Meta:
        model = Company
        # fields = ['name']
        fields = '__all__'
        exclude = ('slug',)

class PostJobForm(forms.ModelForm):
    class Meta:
        model = Jobs
        fields = '__all__'
        exclude = ('slug',)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Init empty did queryset
        self.fields['company'].queryset = Company.objects.all()
