from msilib.schema import Property
from django.db import models
import uuid

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
    # phone_number = models.CharField('tel.nr.:', default = '+370', max_length = 20)
    phone_number= models.PositiveIntegerField('nr',)


    def __str__(self):
        return f'{self.first_name} {self.last_name}'


    class Meta:
        ordering = ['first_name']
        verbose_name = 'duomenys apie klientą'
        verbose_name_plural = 'duomenys apie klientus'

class Cake(models.Model):
    cake_name = models.CharField('torto pavadinimas', max_length=156)
    description = models.TextField('trumas aprašymas', max_length=1000, default='Aprašymas ruošiamas')
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


    STAGE = (
        ('p', 'patvirtintas'),
        ('g', 'gaminamas'),
        ('a', 'paruoštas atsiemimui')
    )
    

    status = models.CharField('užsakymo būsena', max_length=1, choices=STAGE, blank=True, default='p', db_index=True)
    
    def __str__(self):
        return f'{str(self.deadline)} {str(self.status)} {str(self.id)}'


    class Meta:
        ordering = ['deadline']
        verbose_name = 'užakymą'
        verbose_name_plural = 'užsakymai'