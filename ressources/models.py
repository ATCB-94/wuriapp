from django.db import models
from tinymce import models as tinymce_models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import pre_delete
import os

# Create your models here.

class Activite(models.Model):
    libele = models.CharField(max_length=255)
    date = models.DateField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    update_on = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='ressources/images', null=True, blank=True)
   
    class  Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.libele

class Image(models.Model):
    activite = models.ForeignKey(Activite, on_delete=models.CASCADE, related_name='activite_image')
    created_on = models.DateTimeField(auto_now_add=True)
    update_on = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='ressources/images', null=True, blank=True)
    
    class  Meta:
        ordering = ['-created_on']

class Video(models.Model):
    activite = models.ForeignKey(Activite, on_delete=models.CASCADE, related_name='activite_video')
    created_on = models.DateTimeField(auto_now_add=True)
    update_on = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='ressources/videos', null=True, blank=True) 
    video = models.FileField(upload_to='ressources/videos', null=True, blank=True) 
    libele = models.CharField(max_length=255, blank=True)
    #description = tinymce_models.HTMLField(null=True) 
    
    class  Meta:
        ordering = ['-created_on']


class Document(models.Model):
    libele = models.CharField(max_length=255)
    activite = models.ForeignKey(Activite, on_delete=models.CASCADE, related_name='activite_document')
    created_on = models.DateTimeField(auto_now_add=True)
    update_on = models.DateTimeField(auto_now=True)
    document = models.FileField(upload_to='ressources/documents', null=True, blank=True)
    
    class  Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.libele


class Publication_media(models.Model):
    libele = models.CharField(max_length=255)
    url_media = models.CharField(max_length=255)
    media = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
    update_on = models.DateTimeField(auto_now=True)


@receiver(pre_delete, sender=Image)
def _delete_image_image(sender, instance,**kwargs):
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)


@receiver(pre_delete, sender=Video)
def _delete_video_video(sender, instance,**kwargs):
    if instance.video:
        if os.path.isfile(instance.video.path):
            os.remove(instance.video.path)


