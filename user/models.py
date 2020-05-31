from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile", verbose_name="Kullanıcı Adı")
    credit = models.IntegerField("Kredi", null=True, blank=True)
    
    def __str__(self):
        return self.user.username

def create_user_profile(sender, instance, created, **kwargs):

    if created:
        UserProfile.objects.create(user=instance)


post_save.connect(create_user_profile, User)
