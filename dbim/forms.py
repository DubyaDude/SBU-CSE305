from django import forms

class ResultForm(forms.Form):
    search_input = forms.CharField(label='Search', max_length=100)
    type_list = [('title','title'),
    			('person','person'),
    			('year','year')]
    search_type = forms.ChoiceField(label='Pick one',choices=type_list)