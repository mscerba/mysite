from django.urls import path
from . import views

urlpatterns = [
	path("", views.index, name="index"),
	path("priklad_1/", views.recept, name="priklad_1"),
	path("priklad_2/", views.lekce_10,name="priklad_2"),
	path("priklad_3/", views.lekce_16,name="priklad_3"),
	path("priklad_4/", views.priklad_4, name="priklad_4"),
	path("priklad_5/", views.priklad_5, name="priklad_5"),
	path("priklad_6/", views.priklad_6, name="priklad_6"),
	path("priklad_7/", views.priklad_7, name="priklad_7"),
	path("priklad_8", views.priklad_8, name="priklad_8"),
	path("priklad_9", views.priklad_9, name="priklad_9"),
	path("priklad_10", views.priklad_10, name="priklad_10"),
	path("priklad_11", views.priklad_11, name="priklad_11"),
	path("priklad_12", views.priklad_12, name="priklad_12"),
]
