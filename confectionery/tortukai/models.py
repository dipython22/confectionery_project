# from msilib.schema import Property
from http import client
from django.db import models
from django.contrib.auth.models import User
import uuid
from tinymce.models import HTMLField
from datetime import date



class Occasion(models.Model):
    title = models.CharField('progos pavadinimas', max_length=100, )

    def __str__(self):
        return f'{str(self.title)}'

    class Meta:
        ordering = ['title']
        verbose_name = 'proga'
        verbose_name_plural = 'progos'


class Client(models.Model):
    first_name = models.CharField('vardas', max_length=100)
    last_name = models.CharField('pavardė', max_length=100)
    email_name = models.EmailField('el.paštas', max_length = 250, default='@')
    phone_number = models.CharField('tel.nr.:', default = '+370', max_length = 12)
    # phone_number= models.PositiveIntegerField('nr',)


    def __str__(self):
        return f'{self.first_name} {self.last_name}'


    class Meta:
        ordering = ['first_name']
        verbose_name = 'duomenys apie klientą'
        verbose_name_plural = 'duomenys apie klientus'

class Cake(models.Model):
    cake_name = models.CharField('torto pavadinimas', max_length=156)
    description = HTMLField('trumas aprašymas', default='Aprašymas ruošiamas', null=True, blank=True)
    occasion = models.ForeignKey(Occasion, on_delete=models.PROTECT, null=True, related_name='cakes', verbose_name='tinka progai')
    price = models.DecimalField('kaina',max_digits=5, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f'{str(self.cake_name)}'

    class Meta:
        ordering = ['cake_name']
        verbose_name = 'tortas'
        verbose_name_plural = 'tortai'


class Order(models.Model):
    id = models.UUIDField('užsakymo numeris', primary_key=True, default=uuid.uuid4, editable=False)
    client = models.ForeignKey(Client, on_delete=models.PROTECT, null=False, related_name='orders', verbose_name='klientas')
    cake = models.ManyToManyField(Cake, verbose_name='tortas', related_name='orders')
    deadline = models.DateField('pagaminti datai: ', null=False, blank=True, db_index=True)
    notice = models.CharField(('pastabos'), max_length=500, null=True, default='')
    total_price = models.DecimalField('Užsakymo suma: ',max_digits=6, decimal_places=2, null=True, blank=True)
    customer = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True, related_name='orders', verbose_name='užsakovas')


    def display_cakes(self):
        return ', '.join(cake.cake_name for cake in self.cake.all()[:7])
    display_cakes.short_description = 'torto pavadinimas'

    STAGE = (
        ('p', 'patvirtintas'),
        ('g', 'gaminamas'),
        ('a', 'paruoštas atsiemimui'),
        ('u', 'užsakyta')
    )

    status = models.CharField('užsakymo būsena', max_length=1, choices=STAGE, blank=True, default='p', db_index=True)
    
    def __str__(self):
        return f'{str(self.deadline)} {str(self.status)} {str(self.id)}'


    class Meta:
        ordering = ['deadline']
        verbose_name = 'užakymą'
        verbose_name_plural = 'užsakymai'

class CakeReview(models.Model):
    cake = models.ForeignKey(
        Cake, 
        on_delete=models.CASCADE, 
        related_name='cake_reviews', 
        verbose_name='tortas',
        null=True,
        blank=True,
    )
    client = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name='cake_reviews',
        verbose_name='Klientas',
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    content = HTMLField('atsiliepimas')

    def __str__(self):
        return f'{self.cake} - {self.client} - {self.created_at}'


    class Meta:
        verbose_name = 'kliento atsiliepimas'
        verbose_name_plural = 'klientų atsiliepimai'
