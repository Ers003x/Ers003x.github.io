from Ekipet.models import Grupmoshat, Trainer
from blog.models import Category

def custom_processor(request):
	grmosha = Grupmoshat.objects.all()
	category = Category.objects.all()
	trainer = Trainer.objects.all()
	return {'grupmoshat': grmosha, 'kategori': category,'trajner': trainer }