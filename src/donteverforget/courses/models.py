from django.db import models
from django.db.models.signals import pre_save
from .utils import unique_slug_generator
from django.core.urlresolvers import reverse
from django.conf import settings

User = settings.AUTH_USER_MODEL

# Course for the term, can input "other" if not school related

class Course(models.Model):
    owner           = models.ForeignKey(User)
    course          = models.CharField(max_length = 100)
    subject         = models.CharField(max_length = 100)
    term            = models.CharField(max_length = 100)
    description     = models.TextField()
    slug            = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.course

    # Gives course a property of title which returns the name of course

    @property
    def title(self):
        return self.course

    def get_absolute_url(self):
        return reverse('courses:detail', kwargs={'slug': self.slug})

# automatically saves a unique slug for a model entry

def entry_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(entry_pre_save_receiver, sender=Course)