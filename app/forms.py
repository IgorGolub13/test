from django import forms

from .models import Category, Transaction, CHOICE_TYPE


class AddCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']


class AddTransactionForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = None

    class Meta:
        model = Transaction
        fields = ['category', 'value', 'short_description', 'operation_type', 'date']


class SelectCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
