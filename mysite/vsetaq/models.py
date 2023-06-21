from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.contrib.auth import authenticate, login


class Income(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE)
    income = models.DecimalField(decimal_places=2, max_digits=50)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.income}'


class Expenses(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE)
    expenses = models.DecimalField(decimal_places=2, max_digits=50)
    categories = models.CharField(max_length=100, null=False, blank=False, default='')
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.expenses} - {self.categories}'


class Goals(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE)
    save_money = models.DecimalField(decimal_places=2, max_digits=50)
    goal = models.CharField(max_length=200, null=False, blank=False, default='')
    finished = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.save_money} - {self.goal}'


class Side_income(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE)
    side_income = models.DecimalField(decimal_places=2, max_digits=50)
    category = models.CharField(max_length=100, null=False, blank=False, default='')
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.side_income} - {self.category}'