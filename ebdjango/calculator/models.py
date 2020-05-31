from django.db import models

#store the strings and calculations generated as models 
class Calculation(models.Model): 
	calculation = models.TextField(blank = False, null = False) #store full calculation
	
	
