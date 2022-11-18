from django.db import models
from django.contrib.auth.models import User
from PIL import Image

import datetime


# Create your models here.


class Event(models.Model):
    """model for each event"""
    category = [
        ('eating', 'Eating'),
        ('sport', 'Sport'),
        ('movie', 'Movie'),
        ('party', 'Party'),
        ('education', 'Education'),
    ]

    name = models.CharField("Name", max_length=20)
    place = models.CharField("Place", max_length=50)
    participant = models.PositiveIntegerField("Participant",
                                              default=1)
    joined = models.PositiveIntegerField(default=0)
    date = models.DateField("Date")
    time = models.TimeField("Time",
                            default=datetime.time(00, 00))
    type = models.CharField("Type", max_length=20,
                            null=True, blank=True, choices=category)
    image_upload = models.ImageField(null=True,
                                     blank=True, upload_to='event/images',
                                     default='event/images/default.jpg')

    def __str__(self):
        """Return a  string representation of the name event object."""
        return self.name

    def full(self):
        """ check that event full or not"""
        return self.participant == self.joined

    def status(self):
        """ host of event are not allow to join their own event"""
        return True


class HostOfEvent(models.Model):
    """model for record user with their own event"""
    user = models.ForeignKey('auth.user', on_delete=models.CASCADE, null=True)
    event = models.ForeignKey('Hello_Buddy.Event',
                              on_delete=models.CASCADE, null=True)


class ParticipantOfEvent(models.Model):
    """model for record user with joined event"""
    user = models.ForeignKey('auth.user',
                             on_delete=models.CASCADE, null=True)
    event = models.ForeignKey('Hello_Buddy.Event',
                              on_delete=models.CASCADE, null=True)

    def check_par(self):
        """ To check participant and use for create button. """
        return True


class Profile(models.Model):
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE)
    avatar = models.ImageField(default="profile/images/default.jpg",
                               upload_to="profile/images")
    bio = models.TextField(default='...', max_length=50)

    # resizing images
    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)
        img = Image.open(self.avatar.path)

        if img.height > 100 or img.width > 100:
            new_img = (100, 100)
            img.thumbnail(new_img)
            img.save(self.avatar.path)

    def __str__(self):
        return self.user.username
