from django.db import models


class User(models.Model):
    username = models.EmailField(max_length=200, blank=True)
    password = models.CharField(max_length=200, blank=True)
    credit_num = models.IntegerField(default=0, blank=True)
    expiration = models.IntegerField(default=0000, blank=True)
    cvc = models.IntegerField(default=000, blank=True)
    card_type = models.CharField(max_length=200, default="None", blank=True)

    def __str__(self):
        return self.username

class Service(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200, default="None", blank=True)
    last_name = models.CharField(max_length=200, default="None", blank=True)
    gender = models.CharField(max_length=200, default="None", blank=True)
    birthday_month = models.CharField(max_length=200, default="January", blank=True)
    birthday_day = models.IntegerField(default=1, blank=True)
    birthday_year = models.IntegerField(default=2000, blank=True)
    zipcode = models.IntegerField(default=00000, blank=True)
    cost = models.IntegerField()

    def __str__(self):
        return str(self.user) + ' ' + self.company

