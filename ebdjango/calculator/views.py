from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from .forms import CalculationForm
from .models import Calculation
from .utils import calculate

def calculator_view(request, *args, **kwargs):
	quereyset = Calculation.objects.all() #list of all objects
	form = CalculationForm(request.POST or None) #renders form is post data comes through or empty form 
	result = ''
	#Deal with form and do calculation 
	if form.is_valid():
		print("1-------")
		calculation = form.cleaned_data['calculation']
		print("2-------")
		result = calculate(calculation) #see utls
		print(result)

		if result == 'ERROR':
			raise Exception('ERROR in input')
		else:
			print("3-------")
			obj = form.save()
			print("4-------")
			obj.result = result #fill result field
			form = CalculationForm()
			print("5-------")

	
	context = { 
		"form": form,
		"calculations_list": quereyset,
		"result" : result,
	}

	return render(request,"calculator/calculator_window.html",context)



