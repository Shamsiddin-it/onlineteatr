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

class Order(models.Model):
    show = models.ForeignKey(Show, on_delete=models.CASCADE)
    amount = models.IntegerField()
    PAY_TYPE = (
        ("CARD","card"),
        ("CASH","cash"),
    )
    payment = models.CharField(choices=PAY_TYPE,max_length=50)
    total = models.DecimalField( max_digits=10, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

