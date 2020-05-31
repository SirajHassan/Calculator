from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from .forms import CalculationForm
from .models import Calculation
from .utils import calculate
from django.http import HttpResponse, JsonResponse
from tabulate import tabulate

import time
import json


def calculator_view(request, *args, **kwargs):
	
	form = CalculationForm(request.POST or None) #renders form is post data comes through or empty form 
	result = ''
	obj = None 

	#Deal with form and do calculation 
	if form.is_valid():
		calculation = form.cleaned_data['calculation']
		result = calculate(calculation) #see utls
		print(result)

		if result == 'ERROR':
			raise Exception('ERROR in input') ##TODO 
		else:
			obj = Calculation(calculation = calculation, result = result, time = time.time())
			obj.save()
			form = CalculationForm()


	context = { 
		"form": form,
		"obj" : obj,
	}

	return render(request,"calculator/calculator_window.html",context)




#sends data of the last 10 inputs and deletes any extras
def list_calculations_view(request):
	ordered_objects = Calculation.objects.all().order_by('-time')
	i = 0
	data = []
	for obj in ordered_objects:
		if i < 10:
			data.append(str(obj.calculation) + ' = ' + str(obj.result))
		else:
			obj.delete()  #delete old objects
			
		i +=1 

	html = tabulate(data, tablefmt='html')
	return JsonResponse({"html" : html}) #send as JSON
	










