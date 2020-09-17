from django.urls import path 

from . import views


urlpatterns = [
	path('<int:mbarim>/', views.index.as_view(), name = 'ekipi'),
	path('trainer/<str:first>/', views.trainerView, name = 'trainer'),
]