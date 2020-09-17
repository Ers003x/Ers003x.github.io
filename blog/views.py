from django.shortcuts import render, get_object_or_404
from django import template
from django.views.generic import ListView, DetailView


from .models import *
from Ekipet.models import *




register = template.Library()


trajneret = Trainer.objects.all()
teams = Ekipet.objects.all()


category = Category.objects.all()






def index(request):
	Hyrje = Entry.objects.get()
	fron = FrontSlider.objects.all().order_by('rendesia')
	context = {
		'slider': fron,
		'hyrje': Hyrje
	}
	return render(request, 'blog/index.html', context)


def kushtet(request):
	return render(request, 'blog/kushtet.html')


def news(request):
	post = Post.objects.all().order_by('-date_posted')
	Image = Images.objects.all()
	context = {
		'posts': post,

	}
	return render(request, 'blog/news.html', context)


class news_by_category(ListView):
	model = Post
	template_name = 'blog/news_by_category.html'
	context_object_name = 'posts'
	ordering = ['date_posted']

	def get_queryset(self):
		kategoria = get_object_or_404(Category, type = self.kwargs.get('category'))
		return Post.objects.filter(category = kategoria)



class PostDetailView(DetailView):
	model = Post
	template_name = 'blog/detail.html'
	context_object_name = 'post'

