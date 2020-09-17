from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from .models import Ekipet, Grupmoshat, Trainer

				
class index(ListView):
	model = Ekipet
	template_name = 'Ekipet/index.html'
	context_object_name = 'teams'

	def get_queryset(self):
			mosha = get_object_or_404(Grupmoshat, mbarim = self.kwargs.get('mbarim'))
			return Ekipet.objects.filter(category = mosha)






def trainerView(request, first):
	trainer = Trainer.objects.get(first = first)
	context = {
		'trainer': trainer
	}
	return render(request, 'Ekipet/trainers.html', context)