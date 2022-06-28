from django.contrib import admin
from .models import Occasion, Cake, Order, CakeReview, OrderLine

    
# class ClientAdmin(admin.ModelAdmin):
#     list_display = ('first_name', 'last_name', 'email_name', 'phone_number',)
    



class CakeAdmin(admin.ModelAdmin):
    list_display = ('cake_name', 'description', 'occasion', 'price',)
    list_filter = ('occasion__title', )
    list_editable = ('price',)

class OrderLineInline(admin.StackedInline): ## Padaryti, kad užsakymo formoje būtų matomos ir užsakymo eilutės (į jas galima būtų įrašyti informaciją)
    model = OrderLine
    can_delete = False
    extra = 0
# class OrderAdmin(admin.ModelAdmin):
#     list_display = ('order_date', 'total_price', 'client_car', 'status'  )
#     inlines = (OrderLineInline, ) ## Padaryti, kad užsakymo formoje būtų matomos ir užsakymo eilutės (į jas galima būtų įrašyti informaciją)
#     list_editable = ('status',)


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'deadline', 'status', 'notice', 'customer', ) #'display_cakes'
    inlines = (OrderLineInline, ) ## Padaryti, kad užsakymo formoje būtų matomos ir užsakymo eilutės (į jas galima būtų įrašyti informaciją)
    list_filter = ('status', 'deadline')
    search_fields = ('id', 'customer__username',)
    readonly_fields = ('id', )
    list_editable = ('deadline', 'status','customer',) 
    # list_display_links = ('deadline', 'status')

    fieldsets = (
        ('Pagrindinė Informacija', {'fields': (
                'id',
                # 'cake',
                'customer',
                # 'display_cakes', 

            )}),
        ('Užsakymo būsena', {'fields': (
                'status', 
                'deadline', 
                'notice',
            )}),
    )

class OrderLineAdmin(admin.ModelAdmin):
    list_display = ('order', 'cake', 'quantity', 'price', 'remark', ) 
    list_filter = ('cake', 'order__deadline', )
    search_fields = ('order__username', )
    readonly_fields = ('line_created', )
    list_editable = ('quantity', 'price', 'cake', ) #,'customer',) 

# Register your models here.
admin.site.register(Occasion)
# admin.site.register(Client, ClientAdmin)
admin.site.register(Cake, CakeAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderLine, OrderLineAdmin)
admin.site.register(CakeReview)