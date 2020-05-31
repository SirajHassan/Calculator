from django import forms 
from .models import Calculation
from .utils import calculate


class CalculationForm(forms.ModelForm):
	#customizing things w/ widgets
	print("FROMFROM")
	calc_input = forms.CharField(label = '')
	class Meta:
		model = Calculation
		fields = [
			'calc_input',
		]

	#validation
	def clean_calc_input(self, *args, **kwargs):
		print("HELOLO")
		calc_input = self.cleaned_data.get("calc_input")
		allowed_symbols = {'0','1','2','3','4','5','6','7','8','9','+','-','/','x','*',' ','(',')','.'} 
		result = calculate(calc_input)
		invalid = False

		if result == 'ERROR':
			invalid = True
		else:
			for i in calc_input:
				if i not in allowed_symbols:
					invalid = True 

		if invalid:
				print("HEELLERLLER")
				raise forms.ValidationError("Invalid input: Please only use numbers, parentheses and supported operations")
		else:

			return calc_input
