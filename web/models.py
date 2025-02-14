from django.db import models

# Create your models here.
class AdminUser(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=500)
    password = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_blocked = models.BooleanField(default=False)
    
    class Meta:
        db_table = 'admins'
    
    def __str__(self):
        return self.email

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=500)
    password = models.TextField()
    phone_number = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    is_blocked = models.BooleanField(default=False)
    
    class Meta:
        db_table = 'users'
    
    def __str__(self):
        return self.first_name + " " + self.last_name

class Service(models.Model):
    name_ar = models.CharField(max_length=100)
    name_en = models.CharField(max_length=100)
    status = models.BooleanField(default=False)
    logo = models.ImageField(upload_to='services/')
    
    class Meta:
        db_table = 'services'
    
    def __str__(self):
        return self.name_en