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


class Cake(models.Model):
    cake_name = models.CharField('torto pavadinimas', max_length=156)
    description = models.TextField('trumas aprašymas', max_length=1000, default='Aprašymas ruošiamas', null=True, blank=True)
    occasion = models.ForeignKey(Occasion, on_delete=models.PROTECT, null=True, related_name='cakes', verbose_name='tinka progai')
    price = models.DecimalField('kaina',max_digits=5, decimal_places=2, null=True, blank=True)
    pic = models.ImageField('nuotrauka', upload_to='tortukai/pics', null=True, blank=True)

    def __str__(self):
        return f'{str(self.cake_name)} / Kaina: {str(self.price)}'

    class Meta:
        ordering = ['cake_name']
        verbose_name = 'tortas'
        verbose_name_plural = 'tortai'


class Order(models.Model):
    id = models.UUIDField('užsakymo numeris', primary_key=True, default=uuid.uuid4, editable=False)
    order_total_price = models.DecimalField('Užsakymo suma: ',max_digits=6, decimal_places=2, null=True, blank=True, default=0)
    order_date = models.DateField('Užsakymo data', default=date.today)
    deadline = models.DateField('pagaminti datai: ', null=False, db_index=True)
    notice = models.CharField('pastabos', max_length=300, null=True, default='-')
    customer = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True, related_name='orders', verbose_name='užsakovas')

    STAGE = (
        ('p', 'patvirtintas'),
        ('g', 'gaminamas'),
        ('a', 'paruoštas atsiemimui'),
        ('u', 'uždarytas/atšauktas')
    )

    status = models.CharField('užsakymo būsena', max_length=1, choices=STAGE, blank=True, default='p', db_index=True)
    
    def __str__(self):
        return f'{str(self.deadline)} / {str(self.status)} / {str(self.id)} / {str(self.order_total_price)}'

    class Meta:
        ordering = ['deadline']
        verbose_name = 'užakymą'
        verbose_name_plural = 'užsakymai'


class OrderLine(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, blank=True, related_name='order_lines', verbose_name='užsakymas')
    cake = models.ForeignKey(Cake, on_delete=models.SET_NULL, null=True, blank=True, related_name='order_lines', verbose_name='tortukas')
    quantity = models.DecimalField('kiekis', max_digits=6, decimal_places=2, default=1)
    price_per_item = models.DecimalField('Kaina už vnt.', null=True, blank=True, max_digits=6, decimal_places=2)
    summ_per_line = models.DecimalField('Suma', null=True, blank=True, max_digits=10, decimal_places=2, default=0)
    discount = models.DecimalField('nuolaida užsakymui, proc.', null=True, blank=True, max_digits=4, decimal_places=2, default=0)
    line_created = models.DateTimeField(auto_now_add=True, auto_now=False)
    remark = models.CharField('pastabos', max_length=300, null=True, default='-')

    def __str__(self):
        return f' Tortukas: {str(self.cake)} / kiekis: {str(self.quantity)} / Eilutės suma: {str(self.summ_per_line)}'

    def save(self, *args, **kwargs):
        price_per_item = self.cake.price
        self.price_per_item = price_per_item
        print (self.quantity)

        self.summ_per_line = (round((self.quantity), 2) * round((price_per_item), 2)) * ((100-self.discount)/100)

        super(OrderLine, self).save(*args, **kwargs)

    class Meta:
        ordering = ['order']
        verbose_name = 'užsakymo eilutė'
        verbose_name_plural = 'užsakymų eilutės'


class CakeReview(models.Model):
    cake = models.ForeignKey(
        Cake, 
        on_delete=models.CASCADE, 
        related_name='cake_reviews', 
        verbose_name='tortas',
        null=True,
        blank=True,
    )
    subscriber = models.ForeignKey(
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
        return f'{self.cake} - {self.subscriber} - {self.created_at}'

    class Meta:
        ordering = ['created_at']
        verbose_name = 'kliento atsiliepimas'
        verbose_name_plural = 'klientų atsiliepimai'