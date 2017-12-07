from django import forms

class SurveyForms(forms.Form):

    # name = forms.CharField(max_length=20)

    text = forms.CharField(max_length=100)

    date = forms.DateField(widget=forms.SelectDateWidget(attrs={'form':'survey'}))

    choices = [('love','Sex a lot'), ('hate', 'Sex a few')]

    # choice = forms.ChoiceField(choices=choices,widget=forms.CheckboxInput())

    mchoice = forms.MultipleChoiceField(choices=choices,widget=forms.CheckboxSelectMultiple(attrs={'id':'test1'}))