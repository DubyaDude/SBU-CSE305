from django.db import models

# Create your models here.



class ProductionCompany(models.Model):
	name = models.CharField(max_length = 500)
	phone_number = models.CharField(max_length = 20)
	email = models.CharField(max_length = 50)
	address = models.CharField(max_length = 200)

class Movie(models.Model):
    name = models.CharField(max_length = 200)
    genre = models.CharField(max_length = 500)
    description = models.TextField(default = 'Best movie ever')
    duration = models.TimeField()
    release_date = models.IntegerField()
    prod_id = models.ForeignKey(ProductionCompany, on_delete = models.CASCADE)



class Person(models.Model):
    first_name = models.CharField(max_length = 125)
    last_name = models.CharField(max_length = 125)
    dob = models.DateField()
    #age = models.PositiveIntegerField()


class Roles(models.Model):
	movie_id = models.ForeignKey(Movie, on_delete = models.CASCADE)
	person_id = models.ForeignKey(Person, on_delete = models.CASCADE)
	role = models.CharField(max_length = 100)

	class Meta:
		unique_together = (("movie_id", "person_id"),)

class Reviewer(models.Model):
	username = models.CharField(max_length = 125)

class Review(models.Model):
	reviewer_id = models.ForeignKey(Reviewer, on_delete = models.CASCADE)
	date = models.CharField(max_length = 125)
	title = models.CharField(max_length = 125)
	content = models.TextField()
	rating = models.IntegerField(default = 0);


class MovieReviews(models.Model):
	movie_id = models.ForeignKey(Movie, on_delete = models.CASCADE)
	review_id = models.ForeignKey(Review, on_delete = models.CASCADE)

	class Meta:
		unique_together = (("movie_id", "review_id"),)

'''
complex query in moviePage to query name of director and writer (use Roles Table)
complex query in personPage to query Movie and Role (use Roles Table)



You have a text box on some page and when you click it, it sends a post request. 
Then in that method for that path in views.py you do an if check to see if request was a post, 
and if it was you can extract their input and perform query and the  redirect to a results page


user will type in a string to the search bar, store that string, use that 
string for the sql which selects things in the database, then somehow display
it correctly

Specific movie from search bar
SELECT *
FROM Movie 
WHERE input_string = Movie.name

All movies in the year search bar
SELECT *
FROM Movie
WHERE Movie.release_date LIKE '%input_string'

Show all the movie reviews for a certain movie
SELECT * 
FROM Movie,MovieReviews,Review
WHERE MovieReviews.movie_id = Movie

SELECT *
FROM Movie
WHERE id = (SELECT id
			FROM MovieReviews, Review
			WHERE )

Movie pages also shows the average rating for that movie

ProductionCompany will show all the productioncompany info

'''



