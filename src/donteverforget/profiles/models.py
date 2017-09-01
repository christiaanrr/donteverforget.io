from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from .utils import code_generator

User = settings.AUTH_USER_MODEL

# profiles
class Profile(models.Model):
    user            = models.OneToOneField(User)
    activation_key  = models.CharField(max_length=120, blank=True, null=True)
    activated       = models.BooleanField(default=False)
    timestamp       = models.DateTimeField(auto_now_add=True)
    updated         = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

    def send_activation_email(self):
        if not self.activated:
            self.activation_key = code_generator()  # key generator
            self.save()
            path_ = reverse('activate', kwargs={"code": self.activation_key})
            full_path = "https://donteverforget.herokuapp.com/" + path_
            subject = 'Activate Account'
            from_email = settings.DEFAULT_FROM_EMAIL
            message = 'Activate your account here: {}'.format(full_path)
            recipient_list = [self.user.email]
            html_message = '<h1>Thank you for joining dontforget.io!</h1>' \
                           '<p>I hope you never forget to do something that you were supposed to do!' \
                           'Please remember to activate your account in order to use the website!</p>' \
                           '<p>Activate your account here: {}</p>'.format(full_path)
            print(html_message)
            sent_mail = send_mail(
                subject,
                message,
                from_email,
                recipient_list,
                fail_silently=False,
                html_message=html_message)
            sent_mail = False
            return sent_mail

def post_save_user_receiver(sender, instance, created, *args, **kwargs):
    if created:
        profile, is_created = Profile.objects.get_or_create(user=instance)

post_save.connect(post_save_user_receiver, sender=User)