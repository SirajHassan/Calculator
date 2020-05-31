from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from .forms import CalculationForm
from .models import Calculation
from .utils import calculate
from django.http import HttpResponse, JsonResponse
from tabulate import tabulate

import time
import json

#Deals with form and input of user into calculator
def calculator_view(request, *args, **kwargs):
	
	form = CalculationForm(request.POST or None) 
	result = ''
	calc_input = ''
	result_string = ''
	equals = '' 
	obj = None 

	if form.is_valid():
		calc_input = form.cleaned_data["calc_input"]
		result = calculate(calc_input)
		obj = Calculation(calc_input = calc_input, result = result, time = time.time())
		obj.save()
		form = CalculationForm() #resets form 

	equals = '='

	context = { 
		"form": form,
		"output" : calc_input + ' = ' + result ,
	}

	return render(request,"calculator/calculator_window.html",context)




#returns JSON w/ HTML unordered list last 10 inputs and deletes any extras
def list_calculations_view(request):
	ordered_objects = Calculation.objects.all().order_by('-time')
	i = 0
	data = []
	for obj in ordered_objects:
		if i < 10:
			data.append(str(obj.calc_input) + ' = ' + str(obj.result))
		else:
			obj.delete()  #delete old objects
			
		i +=1 

	html = tabulate(data, tablefmt='html')
	return JsonResponse({"html" : html}) #send as JSON
	










