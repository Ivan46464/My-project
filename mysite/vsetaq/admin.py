from django.contrib import admin
from .models import Income, Expenses, Goals, Side_income
# Register your models here.
admin.site.register(Income)
admin.site.register(Expenses)
admin.site.register(Goals)
admin.site.register(Side_income)