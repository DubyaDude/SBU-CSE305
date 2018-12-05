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
    description = models.TextField()
    duration = models.CharField(max_length = 10)
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

