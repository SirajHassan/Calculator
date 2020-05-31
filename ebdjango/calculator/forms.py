from django import forms 
from .models import Calculation
from .utils import calculate


class CalculationForm(forms.ModelForm):
	#customizing things w/ widgets
	calculation = 	forms.CharField()
	class Meta:
		model = Calculation
		fields = [
			'calculation',
		]

	#validation
	def clean_calculation(self, *args, **kwargs):
		calculation = self.cleaned_data.get("calculation")
		allowed_symbols = {'0','1','2','3','4','5','6','7','8','9','+','-','/','x','*','^',' '} 
		invalid = False

		for i in calculation:
			if i not in allowed_symbols:
				invalid = True 

		if invalid:
				raise forms.ValidationError("Invalid input, Please use digits from 0-9, and +,-,/,x,*,^,(,) symbols")
		else:
			return calculation
