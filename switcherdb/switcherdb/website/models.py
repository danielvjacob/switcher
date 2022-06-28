from django.db import models

class User(models.Model):
    username = models.EmailField(max_length=200)
    password = models.CharField(max_length=200)
    credit_num = models.IntegerField(default=0)
    expiration = models.IntegerField(default=0000)
    cvc = models.IntegerField(default=000)
    card_type = models.CharField(max_length=200, default="None")

    def __str__(self):
        return self.username

class Service(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.CharField(max_length=200)
    cost = models.IntegerField()

    def __str__(self):
        return str(self.user) + ' ' + self.company

