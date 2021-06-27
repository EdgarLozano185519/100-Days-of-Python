from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class Book(models.Model):
    """Model definition for MODELNAME."""
    # TODO: Define fields here
    title = models.CharField(max_length=50)
    rating = models.IntegerField(
        validators=[MaxValueValidator(5), MinValueValidator(1)])
    author = models.CharField(max_length=100, null=False)
    is_best_seller = models.BooleanField(default=False)

    def __str__(self):
        """Unicode representation of MODELNAME."""
        return f"{self.title} ({self.rating})"
