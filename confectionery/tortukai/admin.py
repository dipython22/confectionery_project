from django.contrib import admin
from .models import Occasion, Client, Cake, Order, CakeReview

    
class ClientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email_name', 'phone_number',)
    



class CakeAdmin(admin.ModelAdmin):
    list_display = ('cake_name', 'description', 'occasion', 'price',)
    list_filter = ('occasion__title', )
    list_editable = ('price',)


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'display_cakes', 'deadline', 'status', 'notice', 'customer',)
    list_filter = ('status', 'deadline')
    search_fields = ('id', 'customer__username',)
    readonly_fields = ('id', )
    list_editable = ('deadline', 'status') 
    # list_display_links = ('deadline', 'status')

    fieldsets = (
        ('Pagrindinė Informacija', {'fields': (
                'id',
                'cake',
                'customer',
                # 'display_cakes', 

            )}),
        ('Užsakymo būsena', {'fields': (
                'status', 
                'deadline', 
                'notice',
            )}),
    )

    

# Register your models here.
admin.site.register(Occasion)
admin.site.register(Client, ClientAdmin)
admin.site.register(Cake, CakeAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(CakeReview)