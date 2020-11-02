from django import forms
from .models import Signup,Order,Contact

class SignupForm(forms.ModelForm):
	class Meta:
		model = Signup
		fields = {'name','email','mobile','address','password','pin'}
class OrderForm(forms.ModelForm):
	class Meta:
		model = Order
		fields = {'pname','pdiscount','pbrand','ppic','pdesc','pprice'}

class ContactForm(forms.ModelForm):
	class Meta:
		model = Contact
		fields = {'name', 'email', 'message'}