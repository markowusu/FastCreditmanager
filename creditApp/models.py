from django.db import models
from datetime import datetime

# Create your models here.


class User_table(models.Model):

    username = models.CharField(max_length=200)
    email = models.EmailField()
    currentCredit = models.IntegerField()
    date_added = models.DateTimeField(default=datetime.now , blank= True)
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to="photos/%Y/%m/%d")

    def __str__(self):
        return self.username
    

class Transaction_table(models.Model):
    Transfer_from = models.ForeignKey(User_table, on_delete=models.CASCADE, related_name='from_user')
    Transfer_to = models.ForeignKey(User_table, on_delete = models.CASCADE , related_name='to_user')
    date = models.DateField(default=datetime.now , blank=True)
    credit= models.PositiveIntegerField()

    

    def __str__(self):
        return str(self.Transfer_from)



