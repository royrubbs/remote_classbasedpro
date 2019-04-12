from django import forms
class PersonForm(forms.Form):
    name=forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Enter name',
            }
        )
    )
    desc=forms.CharField(help_text="write a brief about a person",
         widget=forms.Textarea(
             attrs={
                 'class':'form-control',
                 'placeholder':'Enter Description',
             }
         )
    )
