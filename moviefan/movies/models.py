from django.utils import timezone
from django.db import models
from django.utils.translation import ugettext as _
from django.urls import reverse


# Create your models here.

class Category(models.Model):
    """Категории"""
    name = models.CharField(verbose_name=_('Называние'), max_length=255)
    description = models.TextField(verbose_name=_('Описание'))
    slug = models.SlugField(max_length=150, unique=True, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'


class Actor(models.Model):
    """Актеры и режисеры"""
    name = models.CharField(verbose_name=_("Имя"), max_length=255)
    description = models.TextField(verbose_name=_('Описание'))
    age = models.PositiveIntegerField(verbose_name=_("Возраст"), blank=True, null=True)

    def __str__(self):
        return self.name


class Movie(models.Model):
    """Фильмы"""
    name = models.CharField(verbose_name=_("Называние"), max_length=255)
    category = models.ForeignKey(
        Category, verbose_name=_('Категория'), on_delete=models.SET_NULL, null=True
    )
    tagline = models.CharField(verbose_name=_('Слоган'), default='', max_length=255)
    description = models.TextField(verbose_name=_('Описание'))
    poster = models.ImageField(verbose_name=_('Постер'), upload_to='actors/')
    year = models.DateField(verbose_name=_('год выпуска'), default=2000)
    directors = models.ManyToManyField(
        Actor, verbose_name=_('Режиссер'), related_name='directors'
    )
    actors = models.ManyToManyField(
        Actor, verbose_name=_("Актеры"), related_name='actors'
    )
    genre = models.ManyToManyField("Genre", verbose_name=_('жанр'))
    premier = models.DateField(
        verbose_name=_('Премьера'), default=timezone.now
    )
    budget = models.PositiveIntegerField(
        default=0, help_text='Сумму указать в долларах', verbose_name=_("Бюджет")
    )
    fees = models.PositiveIntegerField(default=0, verbose_name=_('Сборы с фильма'))
    slug = models.SlugField(unique=True, max_length=255, blank=True, null=True)
    draft = models.BooleanField(default=False, verbose_name=_('Черновик'))

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('movie', args=[str(self.id)])


class Genre(models.Model):
    """Жанры"""
    name = models.CharField(max_length=255, verbose_name=_("Называние"))
    description = models.TextField(verbose_name=_("Описание"))
    slug = models.SlugField(unique=True, max_length=255)

    def __str__(self):
        return self.name


class MovieShots(models.Model):
    """Кадры из фильма"""
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name=_('Заголовок'))
    description = models.TextField(verbose_name=_('Описание'))
    image = models.ImageField(upload_to='movie_shots/', verbose_name=_('Изображение'))

    def __str__(self):
        return self.title


class RatingStar(models.Model):
    """Звезды рейтинга"""
    value = models.PositiveIntegerField(default=0, verbose_name=_('Количество звезд'))

    def __str__(self):
        return self.value


class Rating(models.Model):
    """Рейтинг фильма"""
    ip = models.CharField(verbose_name=_('IP адрес'), max_length=255)
    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE, verbose_name=_('Звездочки'))
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name=_('Кино'))

    def __str__(self):
        return f"{self.star} - {self.movie}"


class Comment(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=255)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name=_("фильм"))
    text = models.TextField(verbose_name=_('Комментарий'), max_length=5000)
    parent = models.ForeignKey(
        'self', null=True, blank=True, verbose_name=_("Ответ комменту"), on_delete=models.SET_NULL
    )

    def __str__(self):
        if self.parent:
            return f"{self.comment[:10]} --> {self.parent[:10]} --> {self.movie}"
        return f"{self.comment[:10]}-->{self.movie}"
