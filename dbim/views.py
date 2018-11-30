from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie,Person,ProductionCompany
# Create your views here.

def homePage(request):
	return render(request,'home.html')

def moviePage(request,id):
   	movies = Movie.objects.raw('SELECT * FROM dbim_movie WHERE id = ' + str(id))
   	context = {'movies':movies} 
   	return render(request,'movie.html',context)

def personPage(request,id):
	persons = Person.objects.raw('SELECT * FROM dbim_person WHERE id = ' + str(id))
	context = {'persons':persons}
	return render(request,'person.html',context)

def productionPage(request,id):
	productions = ProductionCompany.objects.raw('SELECT * FROM dbim_productioncompany WHERE id = ' + str(id))
	context = {'productions':productions}
	return render(request,'production.html',context)

def yearPage(request,year):
	movies = Movie.objects.raw('SELECT * FROM dbim_movie WHERE year = ' + str(year))
	context = {'movies':movies}
	return render(request,'movie.html',context)