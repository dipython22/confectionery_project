from django.contrib import admin

# from confectionery.tortukai.models import Occasion
from .models import Occasion, Client, Cake, Order

    
class ClientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email_name', 'phone_number')



class CakeAdmin(admin.ModelAdmin):
    list_display = ('cake_name', 'description', 'occasion')
    list_filter = ('occasion__title', )
    list_editable: Sequence[str]

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'deadline', 'status', 'notice', 'client') # 'cake'
    list_filter = ('status', 'cake__cake_name', 'deadline')
    search_fields = ('id', 'client__last_name')
    readonly_fields = ('id', )
    list_editable = ('deadline', 'status') 
    # list_display_links = ('deadline', 'status')


    fieldsets = (
        ('Pagrindinė Informacija', {'fields': (
                'id', 
                'client', 

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
