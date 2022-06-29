from django.contrib import admin
from .models import Occasion, Cake, Order, CakeReview, OrderLine
    

class CakeAdmin(admin.ModelAdmin):
    list_display = ('cake_name', 'description', 'occasion', 'price',)
    list_filter = ('occasion__title', )
    list_editable = ('price',)

class OrderLineInline(admin.StackedInline): 
    model = OrderLine
    can_delete = False
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'deadline', 'status', 'customer', 'order_total_price', 'notice',) 
    inlines = (OrderLineInline, ) 
    list_filter = ('status', 'deadline',)
    search_fields = ('id', 'customer__username',)
    readonly_fields = ('id', )
    list_editable = ('deadline', 'status','customer',) 

    fieldsets = (
        ('Pagrindinė Informacija', {'fields': (
                'id',
                'customer',
                'order_total_price', 

            )}),
        ('Užsakymo būsena', {'fields': (
                ('status', 'deadline'),
                'notice',
            )}),
    )


class OrderLineAdmin(admin.ModelAdmin):
    list_display = ('order', 'cake', 'quantity', 'discount', 'summ_per_line', 'remark', ) 
    list_filter = ('cake', 'order__deadline', )
    search_fields = ('order__username', )
    readonly_fields = ('line_created', )
    list_editable = ('cake', 'quantity', 'discount', )

admin.site.register(Occasion)
admin.site.register(Cake, CakeAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderLine, OrderLineAdmin)
admin.site.register(CakeReview)