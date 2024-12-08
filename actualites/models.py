from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import pre_delete
import os

# Create your models here.
STATUS = ((0, "Draft"), (1,"Published"))

class Post(models.Model):
    titre = models.CharField(max_length=255, unique=True)
    titre_court = models.CharField(max_length=95, unique=True)
    slug = models.SlugField(max_length=200 , unique=True)
    auteur = models.ForeignKey(User , on_delete=models.CASCADE, related_name='blog_post')
    created_on = models.DateTimeField(auto_now_add=True)
    update_on = models.DateTimeField(auto_now=True)
    contenu = models.TextField()
    statut = models.IntegerField(choices=STATUS, default=0)
    image = models.ImageField(upload_to='article_images', null=True, blank=True)

    class  Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.titre_court
    
@receiver(pre_delete, sender=Post)
def _delete_post_image(sender, instance,**kwargs):
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)
    