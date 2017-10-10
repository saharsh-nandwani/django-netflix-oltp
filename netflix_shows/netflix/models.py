from django.db import models


class Netflix(models.Model):
    """
    Puppy Model
    Defines the attributes of a puppy
    """
    name = models.CharField(max_length=255)
    rating = models.IntegerField()
    castName = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



    def __repr__(self):
        return self.name + ' is added.'
