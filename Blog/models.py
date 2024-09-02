from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models
from django.contrib.auth.models import User

class VocabularyList(models.Model):
    name = models.CharField(max_length=100)  # This field exists
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # This field exists

    def __str__(self):
        return self.name

class VocabularyWord(models.Model):
    vocab_list = models.ForeignKey(VocabularyList, related_name='words', on_delete=models.CASCADE)
    japanese_word = models.CharField(max_length=100)
    english_translation = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.japanese_word} - {self.english_translation}"




class Cities(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image_url = models.URLField(max_length=200)
    image_url2 = models.URLField(default="LoremIpsum")
    image_url3 = models.URLField(default="LoremIpsum")
    alt = models.TextField(default="LoremIpsum")
    parag2 = models.TextField(default="LoremIpsum")
    parag3 = models.TextField(default="LoremIpsum")

    def __str__(self):
        return self.name

class Comment(models.Model):
    city = models.ForeignKey(Cities, related_name='comments', on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.author} on {self.city.name}'

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=100, blank=True)
    

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()