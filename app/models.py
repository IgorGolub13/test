from django.db import models
from django.utils.translation import ugettext_lazy as _
from datetime import date

# Create your models here.

CHOICE_TYPE = (
    ('Дохід', 'Дохід'),
    ('Витрата', 'Витрата'),)


class Category(models.Model):
    name = models.CharField(_('Ім\'я'), max_length=40, unique=True,
                            error_messages={
                                'unique': 'Category with this name is already created. Please enter unique name.',
                                'required': 'Please enter the name in the textarea. '})

    description = models.TextField(_('Опис'), max_length=500, blank=True, null=True)

    def __str__(self):
        return f'{self.id} {self.name}'


class Transaction(models.Model):
    category = models.ForeignKey(Category, related_name="category", on_delete=models.CASCADE)
    operation_type = models.CharField(_('Тип oперації'), max_length=10, choices=CHOICE_TYPE, default="Витрата")
    value = models.FloatField(_('Сума'), default=100)
    short_description = models.TextField(_('Короткий опис'), max_length=100, blank=True, null=True)
    date = models.DateField(_('Дата виконання транзакції'), default=date.today)

    def __str__(self):
        return f'{self.value} + {self.short_description}'
