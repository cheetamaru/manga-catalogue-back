from django.db import models
from django.utils.translation import gettext_lazy as _

class MangaAuthor(models.Model):
    firstName = models.CharField(max_length=100, default="")
    surname = models.CharField(max_length=100, default="")

    def __str__(self):
        return str(self.id)

class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class MangaTitle(models.Model):
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    chapterCount = models.PositiveSmallIntegerField(default=1)
    volumeCount = models.PositiveSmallIntegerField(default=0)
    startDate = models.DateField(null=True)
    endDate = models.DateField(null=True, blank=True)
    firstCoverImage = models.ImageField(upload_to='base/uploads/covers', null=True, blank=True)

    authors = models.ManyToManyField(MangaAuthor, related_name="authors", blank=True)
    genres = models.ManyToManyField(Genre, related_name="genres", blank=True)

    class Status(models.TextChoices):
        FINISHED = 'finished', _('Finished')
        ONGOING = 'ongoing', _('Publishing')
        HIATUS = 'hiatus', _('On Hiatus')
        CANCELED = 'canceled', _('Discontinued')
        NOT_STARTED = 'notstarted', _('Not Yet Published')

    status = models.CharField(max_length=12, null=True, choices=Status.choices)

    def __str__(self):
        return self.title
