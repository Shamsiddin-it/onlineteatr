from django.db import models

class User(models.Model):
    full_name = models.CharField( max_length=150)
    phone = models.CharField(max_length=13)

    def __str__(self):
        return self.full_name

class Janre(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
    

class Teatr(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    image = models.ImageField(upload_to="static/images/teatr", null=True, blank=True)
    def __str__(self):
        return self.name
      
class Film(models.Model):
    name = models.CharField(max_length=50)
    janre = models.ForeignKey(Janre, on_delete=models.CASCADE)
    created_on = models.DateField( auto_now=False, auto_now_add=False)
    image = models.ImageField(upload_to="static/image/film", height_field=None, width_field=None, max_length=None)
    trailer = models.FileField( upload_to="static/trailer", max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

class Show(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    date = models.DateField(auto_now=False, auto_now_add=False)
    time = models.DateTimeField()
    teatr =  models.ForeignKey(Teatr, on_delete=models.CASCADE)
    price_bil = models.DecimalField(max_digits=6, decimal_places=2)
    def __str__(self):
        return f"{self.film}"

class Order(models.Model):
    amount = models.IntegerField()
    name = models.CharField( max_length=50)
    phone = models.CharField(max_length=50)


class Payment(models.Model):
    TYPE = (
        ("CARD", "card"),
        ("CASH", "cash"),
    )
    type = models.CharField(choices=TYPE ,max_length=50)
