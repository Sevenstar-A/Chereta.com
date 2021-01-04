from django.db import models

class Admin(models.Model):
    First_name=models.CharField(max_length=100)
    Last_name=models.CharField(max_length=100)
    User_name=models.CharField(max_length=100)
    Password =models.CharField(max_length=100)
    Emial =models.EmailField()
    Phone =models.CharField(max_length=20)
    City =models.CharField(max_length=100)
    Longitude = models.CharField(max_length=20)
    Latitude =models.CharField(max_length=20)
    Credit_card =models.CharField(max_length=20,default='')

class Client(models.Model):
    First_name=models.CharField(max_length=100)
    Last_name=models.CharField(max_length=100)
    User_name=models.CharField(max_length=100)
    Password =models.CharField(max_length=100)
    Emial =models.EmailField()
    Phone =models.CharField(max_length=20)
    City =models.CharField(max_length=100)
    Longitude = models.CharField(max_length=20)
    Latitude =models.CharField(max_length=20)
    Credit_card =models.CharField(max_length=20,default='')

    def __str__(self):
        return self.First_name+" "+self.Last_name


class  Bid(models.Model):
    Title = models.CharField(max_length=100)
    Description = models.TextField(max_length=100, null=True)
    Catagory = models.CharField(max_length=100)
    Base_cost =models.FloatField()
    Date_created=models.DateField(auto_now_add=True)
    Date_closing=models.DateField()
    Total_number_of_biders = models.IntegerField(default=0)
    Uploader= models.ForeignKey(Client, related_name='uploader',on_delete=models.CASCADE,default=1)
    
    def __str__(self):
        return self.Title



class Auction(models.Model):
    Bid_id = models.ForeignKey(Bid,related_name="bid", on_delete=models.CASCADE)
    Client_id = models.ForeignKey(Client,related_name="client", on_delete=models.CASCADE)
    Offered_price = models.FloatField()
    Notes = models.TextField(max_length=1000)

    

