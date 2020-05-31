from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from .forms import CalculationForm
from .models import Calculation
from .utils import calculate

def calculator_view(request, *args, **kwargs):
	quereyset = Product.objects.all() #list of all objects
	form = CalculationForm(request.POST or None) #renders form is post data comes through or empty form 
	
	#Deal with form and do calculation 
	if form.is_valid():
		calculation = form.cleaned_data['calculation']
		result = calculate(calculation) #see utls

		if result == 'ERROR':
			raise Exception('ERROR in input')
		else:
			obj = form.save()
			obj.result = result #fill result field
			form = CalculationForm()

	
	context = { 
		"form": form,
		"calculations_list": quereyset
	}

	return render(request,"calculator_window.html",context)



