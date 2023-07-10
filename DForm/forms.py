from django import forms

def validate_name(jelly):
    if jelly[0].lower()=='a':
        raise forms.ValidationError("Name shouldn't starts with A")
    
def validate_len(value):
    if len(value)<=5:
        raise forms.ValidationError("Name should be more than 5 chars")
    
class StudentForm(forms.Form):
    name=forms.CharField(max_length=100,help_text='Enter name',label="Name",validators=[validate_name,validate_len])
    age=forms.IntegerField(help_text='Enter age',label='Age')
    cls=forms.IntegerField(help_text='Enter class',label='Class')
    loc=forms.CharField(help_text='Enter location',label='Location')
    email=forms.EmailField(help_text='Enter email',label='Email',validators=[validate_name])