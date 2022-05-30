from django.db import models
from django.urls import reverse
from accounts.models import CustomUser

class Category(models.Model):
    
    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    name = models.CharField(max_length=200, blank=False)
    slug = models.SlugField(max_length=200, unique=True)


    def __str__(self):
        return self.name
    

    def get_absolute_url(self):
        return reverse('home:category_list', args=[self.slug])



    # we have a 4 category 
    """ 
     фильмы/сериалы/мультфильмы/мультсериалы
     
     films/serials/cartoons/cartoonSerials

    """

class Videos(models.Model):
    category = models.ForeignKey(Category, related_name='videos', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    descrition = models.CharField(max_length=400,db_index=True)
    videofile = models.FileField(upload_to='videos/', null=True)

    seasons = models.PositiveIntegerField(blank=True, null=True)  # сезон 1, 2-fasl
    part = models.PositiveIntegerField(blank=True, null=True) # серия 2, 35-qism 

    def __str__(self):
        return self.name 
    
    def get_absolute_url(self):
        return reverse('home:detail', args=[str(self.id)])

"""     
    --------------------------------
    --------------------------------
            Description our "Videos" model.
            
            1. category -> our Videos category
            2. name -> videos or film name
            3. description -> descrition video
            4. videofile -> videofile  file (.mp4 )
            5. seasons -> season of film (Сезон филма)
            6. part -> part of film (Серия, Раздел )

    --------------------------------
    --------------------------------
"""
class Subcribe(models.Model):
    name = models.CharField(max_length=200) #Subcribe name -> Total, medium ...
    price = models.IntegerField() # 15$
    month = models.IntegerField() # 3 month


    def __str__(self):
        return self.name

class SubscribeHistory(models.Model):
   
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  # user data for subribe
    active_started_date = models.DateTimeField() # started of the subcribe
    active_finished_date = models.DateTimeField() #finish of the subcriobe 
    subcribe = models.ForeignKey(Subcribe, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user) + " " + str(self.active_finished_date)


class PaymentSystem(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return str(self.name)


class BalanceHistory(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    cost = models.DecimalField(max_digits=4, decimal_places=1)
    created_at = models.DateTimeField()

    def __str__(self):
        return self.cost


class TopUpBalance(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    cost = models.DecimalField(max_digits=4, decimal_places=1)
    payment_system = models.ForeignKey(PaymentSystem, on_delete=models.CASCADE)
    created_at = models.DateTimeField()

    def __str__(self):
        return str(self.cost)


    

