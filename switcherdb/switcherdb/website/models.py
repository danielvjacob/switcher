from django.db import models

class User(models.Model):
    username = models.EmailField(max_length=200)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.username

class Service(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.CharField(max_length=200)
    cost = models.IntegerField()

    def __str__(self):
        return str(self.user) + ' ' + self.company

class Billing_info(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    credit_num = models.IntegerField()
    expiration = models.IntegerField()
    cvc = models.IntegerField()
    card_type = models.CharField(max_length=200)

    def __str__(self):
        return self.user.username
    
