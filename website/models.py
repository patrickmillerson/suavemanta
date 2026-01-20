from django.db import models
from django.utils.text import slugify



class AboutPage(models.Model):
    head_message_1 = models.TextField(blank=True)
    head_message_1_paragraph_1 = models.TextField(blank=True)
    head_message_1_message_1 = models.TextField(blank=True)
    head_message_1_message_2 = models.TextField(blank=True)
    head_message_1_message_3 = models.TextField(blank=True)
    head_message_1_message_4 = models.TextField(blank=True)
    head_message_1_paragraph_2 = models.TextField(blank=True)
    head_message_1_paragraph_3 = models.TextField(blank=True)
    head_message_1_paragraph_4 = models.TextField(blank=True)
    image_1 = models.ImageField(upload_to='about_images/', blank=True, null=True)
    video = models.FileField(upload_to='about_videos/', blank=True, null=True)

    vision_head_message = models.TextField(blank=True)
    vision_message_paragraph_1 = models.TextField(blank=True)
    vision_message_message_1 = models.TextField(blank=True)
    vision_message_message_2 = models.TextField(blank=True)
    vision_message_message_3 = models.TextField(blank=True)
    vision_message_message_4 = models.TextField(blank=True)
    vision_message_message_5 = models.TextField(blank=True)
    vision_message_message_6 = models.TextField(blank=True)
    vision_message_paragraph_2 = models.TextField(blank=True)
    
    image_2 = models.ImageField(upload_to='about_images/', blank=True, null=True)
    image_3 = models.ImageField(upload_to='about_images/', blank=True, null=True)
    image_4 = models.ImageField(upload_to='about_images/', blank=True, null=True)

    def __str__(self):
        return "About Page Content"
    

class Service(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    short_description = models.TextField()
    long_description = models.TextField()
    image = models.ImageField(upload_to="services/")
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title