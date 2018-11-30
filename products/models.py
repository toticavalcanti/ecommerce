import random
import os
from django.db import models

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    new_filename = random.randint(1, 3910209312)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename = new_filename, ext = ext) #old format
    #final_filename = f"{new_filename}{ext}" #syntax to python 3.6 and up

    return "products/{new_filename}/{final_filename}".format(
            new_filename = new_filename, 
            final_filename = final_filename
            )
    #return f"products/{new_filename}/{new_filename}" #syntax to python 3.6 and up

class ProductManager(models.Manager):
    def featured(self):
        return self.get_queryset().filter(featured = True)

    def get_by_id(self, id):
        qs = self.get_queryset().filter(id = id)
        if qs.count() == 1:
            return qs.first()
        return None


# Create your models here.
class Product(models.Model): #product_category
    title       = models.CharField(max_length=120)
    description = models.TextField()
    price       = models.DecimalField(decimal_places=2, max_digits=20, default=39.99)
    image       = models.ImageField(upload_to = upload_image_path, null = True, blank = True)
    feature     = models.BooleanField(default = False)

    objects     = ProductManager()

    def __str__(self):
        return self.title
    
    def __unicode__(self):
        return self.title
