from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Movie,Person,ProductionCompany,Roles,Reviewer,Review,MovieReviews
from .forms import ResultForm
from datetime import timedelta
# Create your views here.

def homePage(request):
	if request.method == 'POST':
		form = ResultForm(request.POST)
		if form.is_valid():
			search_input = form.cleaned_data['search_input']
			search_type = form.cleaned_data['search_type']
			context = {'search_input':search_input,
					'search_type':search_type}
			return HttpResponseRedirect('/searchresults/' + search_type + '/' + search_input)
	else:
		form = ResultForm()

	return render(request, 'home.html', {'form': form})

def moviePage(request,id):
   	movie = Movie.objects.raw('SELECT * FROM dbim_movie WHERE id = ' + str(id))
   	a = 'Actor'
   	d = 'Director'
   	w = 'Writer'
   	actor = Person.objects.raw('SELECT p.id, p.first_name, p.last_name FROM dbim_person p,dbim_roles r WHERE r.movie_id_id = ' + str(id) + ' and r.person_id_id = p.id and r.role = %s',[a])
   	director = Person.objects.raw('SELECT p.id, p.first_name, p.last_name FROM dbim_person p,dbim_roles r WHERE r.movie_id_id = ' + str(id) + ' and r.person_id_id = p.id and r.role = %s',[d])
   	writer = Person.objects.raw('SELECT p.id, p.first_name, p.last_name FROM dbim_person p,dbim_roles r WHERE r.movie_id_id = ' + str(id) + ' and r.person_id_id = p.id and r.role = %s',[w])
   	production = ProductionCompany.objects.raw('SELECT pc.id, pc.name FROM dbim_productioncompany pc,dbim_movie m WHERE m.id = ' + str(id) + ' and m.prod_id_id = pc.id')
   	rating = Review.objects.raw('SELECT r.id,r.title, r.content, r.rating FROM dbim_review r, dbim_moviereviews mr WHERE mr.movie_id_id = ' + str(id) + ' and mr.review_id_id = r.id')
   	username = Reviewer.objects.raw('SELECT rer.id,rer.username FROM dbim_review r,dbim_reviewer rer,dbim_moviereviews mr WHERE mr.movie_id_id = ' + str(id) + ' and r.reviewer_id_id = rer.id and mr.review_id_id = r.id')
   	
   	context = {'movies':movie,
   				'actors':actor,
   				'directors':director,
   				'writers':writer,
   				'productions':production,
   				'ratings':rating,
   				'username':username
   				}


   	return render(request,'movie.html',context)

def personPage(request,id):
	persons = Person.objects.raw('SELECT * FROM dbim_person WHERE id = ' + str(id))
	movieRole = Roles.objects.raw('SELECT r.person_id_id, r.movie_id_id, r.role, m.id, m.name FROM dbim_movie m,dbim_roles r WHERE r.person_id_id = ' + str(id) + ' and r.movie_id_id = m.id ')
	context = {'persons':persons,
				'movieRoles':movieRole
				}

	return render(request,'person.html',context)

def productionPage(request,id):
	productions = ProductionCompany.objects.raw('SELECT * FROM dbim_productioncompany WHERE id = ' + str(id))
	context = {'productions':productions}
	return render(request,'production.html',context)

def searchPage(request,search_type,search_input):
	searchy = []
	#if search_type == title, person,year
	if(search_type == 'title'):
		movie_title = search_input + '%'
		searchy = Movie.objects.raw('SELECT * FROM dbim_movie WHERE name LIKE %s',[movie_title])
		
	elif(search_type == 'person'):

		if ' ' in search_input:
			name = search_input.split()
		
			first = name[0]
			second = name[1] + '%'

			
			#if there is a name[1] then name[0],name[1]%
			searchy = Person.objects.raw("SELECT * FROM dbim_person dp WHERE dp.first_name = %s and dp.last_name LIKE %s",[str(first),str(second)])
		
		#if there is no name[1] then name[0]%
		else:
			first = search_input + '%'
			searchy = Person.objects.raw('SELECT * FROM dbim_person WHERE first_name LIKE %s',[first])

	elif(search_type == 'year'):
		searchy = Movie.objects.raw('SELECT * FROM dbim_movie WHERE release_date = ' + search_input)
	

	context = {'search_input':search_input,
				'search_type':search_type,
				'searchy':searchy}
	return render(request,'searchresults.html',context)

# def resultsPage(request):
# 	movies = Movie.objects
