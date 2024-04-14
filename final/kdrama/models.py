from django.db import models

# Create your models here.
class kdrama(models.Model):
    kdrama_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500, blank=True)
    release_year = models.CharField(max_length=50, blank=True)
    duration = models.CharField(max_length=50, blank=True)

    
    def __str__(self):
        return self.title

class character(models.Model):
    character_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=True)
    kdrama = models.ForeignKey(kdrama, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class actor(models.Model):
    actor_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=25, blank=True)
    last_name = models.CharField(max_length=25, blank=True)
    birth_date = models.DateField(blank=True, null=True)
    character = models.ForeignKey(character, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name, self.last_name

class director (models.Model):
    director_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=25, blank=True)
    last_name = models.CharField(max_length=25, blank=True)
    kdrama = models.ForeignKey(kdrama, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name, self.last_name

class prod_company(models.Model):
    prod_company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True)
    year_founded = models.CharField(max_length=50, blank=True)
    kdrama = models.ForeignKey(kdrama, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class award(models.Model):
    award_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True)
    type = models.CharField(max_length=100, blank=True)
    kdrama = models.ForeignKey(kdrama, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=255)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.username
    

class Purchase(models.Model):
    purchase_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    kdrama = models.ForeignKey(kdrama, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits = 20, decimal_places = 2)