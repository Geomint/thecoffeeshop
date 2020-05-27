from django.contrib import admin
from .models import Order, OrderItem

# Register your models here.

class OrderItemAdminInline(admin.TabularInline):
    model = OrderItem

class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderItemAdminInline, )

admin.site.register(Order, OrderAdmin)