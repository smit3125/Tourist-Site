from django.db import models 
from django.utils import timezone

# Create your models here.
class place_type(models.Model):
    place_type_id = models.AutoField(primary_key=True)
    place_type = models.CharField(max_length=100)
    description = models.TextField(max_length=700)
    create_ts = models.DateTimeField(default=timezone.now) 
    update_ts = models.DateTimeField(auto_now=True)


class place(models.Model):
    PLACE_TYPE = (
        ('Historical Places', 'Historical_places'),
        ('Museum', 'Museum'),
        ('Temple', 'Temple'),
        ('Lake', 'Lake'),
        ('Garden', 'Garden'),
        ('Market', 'Market'),
    )
    place_pid = models.AutoField(primary_key=True)
    place_type = models.ForeignKey(place_type,on_delete=models.CASCADE,choices=PLACE_TYPE, verbose_name="Place_type")
    place_name = models.CharField(max_length=100)
    address = models.CharField(max_length=200,null=True)
    pin_code = models.IntegerField()
    official_site_link = models.CharField(max_length=500)
    ticket_price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(max_length=700)
    open_time = models.TimeField(auto_now_add=True)
    close_time = models.TimeField(auto_now=True)
    image = models.ImageField(upload_to="img",null=True)

class user(models.Model):
    user_pid = models.AutoField(primary_key=True,default=False)
    firstname = models.CharField(max_length=100,default=False)
    lastname = models.CharField(max_length=100,default=False)
    email = models.EmailField(null=True)
    mobile_NO = models.CharField(max_length=20,default=False)
    address = models.CharField(max_length=200,default=True)
    username = models.CharField(max_length=100,default=False)
    password = models.CharField(max_length=50,default=False)
    create_ts = models.DateTimeField(default=timezone.now) 
    update_ts = models.DateTimeField(auto_now=True)

class Cart(models.Model):
     cart_id= models.AutoField(primary_key=True,default=True)
     places = models.ForeignKey(place, on_delete=models.CASCADE)
    
