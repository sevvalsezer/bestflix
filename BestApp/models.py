from django.db import models
from enum import Enum
from django.utils import timezone


class MediaType(Enum):
    MOVIE = "Movie"
    TV_SHOW = "Tv Show"


class Media(models.Model):
    title = models.CharField(max_length=255, unique=False)
    year = models.DateField()
    rating = models.IntegerField()
    poster = models.URLField(unique=True, null=True)
    description = models.CharField(max_length=800, unique=False)
    mediaType = models.CharField(
        max_length=255,
        choices=[(type.name, type.value) for type in MediaType]
    )

    def __str__(self):
        return self.title + " " + self.year.year.__str__()


class MostPopular(models.Model):
    media = models.ForeignKey(
        Media,
        unique=True,
    )

    def __str__(self):
        return self.media.title + " " + self.media.year.year.__str__()


class Recent(models.Model):
    media = models.ForeignKey(
        Media,
        unique=True
    )

    def __str__(self):
        return self.media.title + " " + self.media.year.year.__str__()


class Cast(models.Model):
    name = models.CharField(max_length=255, unique=False)
    photo = models.URLField(unique=True, null=True)
    knownFor = models.CharField(max_length=255, unique=False)

    def __str__(self):
        return self.name


class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30, unique=True)


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    image = models.URLField(unique=True, null=True)
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class MovieDetail(models.Model):
    NOT_RATED = 0
    RATED_G = 1
    RATED_PG = 2
    RATED_R = 3
    RATINGS = (
        (NOT_RATED, 'NR - Not Rated'),
        (RATED_G,
         'G - General Audiences'),
        (RATED_PG,
         'PG - Parental Guidance '
         'Suggested'),
        (RATED_R, 'R - Restricted'),
    )

    title = models.CharField(
        max_length=140)
    plot = models.TextField()
    year = models.PositiveIntegerField()
    rating = models.IntegerField(
        choices=RATINGS,
        default=NOT_RATED)
    runtime = \
        models.PositiveIntegerField()
    website = models.URLField(
        blank=True)

    def __str__(self):
        return '{} ({})'.format(
            self.title, self.year)