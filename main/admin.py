from django.contrib import admin
from main.models import Restaurant, Table, Seat, Reservation


admin.site.register(Restaurant)
admin.site.register(Table)
admin.site.register(Seat)
admin.site.register(Reservation)
