# Core Django imports.
from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Form(models.Model):

    name = models.CharField(max_length=100, null=False, blank=False)
    slug = models.SlugField()
    image = models.ImageField(default='mortified-default.jpg',
                              upload_to='form_images')
    form_url= models.URLField(max_length=250, default = "")
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('name',)
        verbose_name = 'form'
        verbose_name_plural = 'forms'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name, allow_unicode=True)
        super(Form, self).save(*args, **kwargs)
