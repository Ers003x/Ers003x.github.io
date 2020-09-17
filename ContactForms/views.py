from django.shortcuts import render

from .models import *




def contacts(request):
	context = {
		'contactNr': ContactNumber.objects.all(),
		'contactEm': ContactEmail.objects.all(),
	}
	return render(request, 'ContactForms/contact.html', context)