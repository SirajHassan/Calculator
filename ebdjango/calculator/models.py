from django.db import models

#store the strings and calculations generated as models 
class Calculation(models.Model): 
	calculation = models.TextField(blank = False, null = False) #store full calculation
	result= models.CharField(blank = False, null = False, max_length = 120) #store full calculation

	
