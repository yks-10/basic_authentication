from django import forms 

class Students(forms.Form):
	first_name = forms.CharField(max_length = 200)
	last_name = forms.CharField(max_length = 200)
	roll_number = forms.CharField()
	password1 = forms.CharField(widget =forms.PasswordInput())
	password2 = forms.CharField(widget =forms.PasswordInput())


class Studentlog(forms.Form):
	roll_number = forms.CharField()
	password = forms.CharField(widget =forms.PasswordInput())