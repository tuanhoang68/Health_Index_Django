from django.db import models

# Create your models here.

class Input(models.Model):
    height = models.IntegerField()
    weight = models.IntegerField()
    eye_sight = models.IntegerField()
    tooth_decay = models.IntegerField()
    hearing_power = models.IntegerField()
    max_blood = models.IntegerField()
    size_skin = models.IntegerField()
    length_difference = models.IntegerField()
    
    # def __str__(self):
    #     return self.height