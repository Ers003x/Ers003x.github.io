from django.urls import path 

from . import views

from .views import PostDetailView


urlpatterns = [
	path('', views.index, name = 'index'),
	path('kushtet/', views.kushtet, name = 'kushtet'),
	path('news/', views.news, name = 'news'),
	path('news/<str:category>/', views.news_by_category.as_view(), name = 'by-category'),
	path('detail/<int:pk>/', PostDetailView.as_view(), name = 'post-detail')
]