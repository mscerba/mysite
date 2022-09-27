from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
	return render(request, "html_kurz/index.html")
	#return HttpResponse("Toto je první stránky kurzu HTML")

def recept(request):
	return render(request, "html_kurz/priklad_1.html")

def lekce_10(request):
	return render(request, "html_kurz/priklad_2.html")

def lekce_16(request):
	return render(request, "html_kurz/priklad_3.html")

def priklad_4(request):
	return render(request, "html_kurz/priklad_4.html")

def priklad_5(request):
	return render(request, "html_kurz/priklad_5.html")

def priklad_6(request):
	return render(request, "html_kurz/priklad_6.html")

def priklad_7(request):
	return render(request, "html_kurz/priklad_7.html")

def priklad_8(request):
	return render(request, "html_kurz/priklad_8.html")

def priklad_9(request):
	return render(request, "html_kurz/priklad_9.html")

def priklad_10(request):
	return render(request, "html_kurz/priklad_10.html")

def priklad_11(request):
	return render(request, "html_kurz/priklad_11.html")

def priklad_12(request):
	return render(request, "html_kurz/priklad_12.html")
