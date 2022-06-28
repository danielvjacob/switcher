from django.db import models
from multipage_form.models import MultipageModel

class User(MultipageModel):
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
    cost = models.IntegerField()

    def __str__(self):
        return str(self.user) + ' ' + self.company

