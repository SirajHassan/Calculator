from django.db import models
import time 

#store the strings and calculations generated as models 
class Calculation(models.Model): 
	calc_input = models.TextField(blank = False, null = False) #inputted calculation
	result= models.CharField(blank = False, null = False, max_length = 120) #calculations result
	time = models.DecimalField(default = time.time(), blank = False, null = False, decimal_places = 0, max_digits = 10000000000000) #time of calculation

	
