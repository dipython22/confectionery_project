from django.contrib import admin
from .models import Occasion, Client, Cake, Order

    
class ClientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email_name', 'phone_number')



class CakeAdmin(admin.ModelAdmin):
    list_display = ('cake_name', 'description', 'occasion')


class OrderAdmin(admin.ModelAdmin):
    list_display = ('deadline', 'status', 'notice', 'id', 'client') # 'cake'
    

# Register your models here.
admin.site.register(Occasion)
admin.site.register(Client, ClientAdmin)
admin.site.register(Cake, CakeAdmin)
admin.site.register(Order, OrderAdmin)
