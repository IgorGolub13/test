from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Category, Transaction
from .forms import AddCategoryForm, AddTransactionForm


# Create your views here.

def view_categories(request):
    c = Category.objects.all()
    return render(request, 'app/category/list.html', {'category': c})


def view_transaction(request):

    t = Transaction.objects.all()
    return render(request, 'app/transaction/list.html', {'transaction': t})


def add_category(request):
    if request.method == 'POST':
        form = AddCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_categories')
    else:
        form = AddCategoryForm()
    return render(request, 'app/category/add_category.html', {'form': form})


def add_transaction(request):
    if request.method == 'POST':
        form = AddTransactionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_transaction')
            # print(form.fields['date'])
    else:
        form = AddTransactionForm()
    return render(request, 'app/transaction/add_transaction.html', {'form': form})


def delete_category(request, id):
    to_delete = Category.objects.get(id=id)
    to_delete.delete()
    return redirect("view_categories")


def edit_category(request, id):
    instance = Category.objects.get(id=id)
    is_update = None
    if request.method == 'POST':
        form = AddCategoryForm(request.POST, instance=instance)
        if form.is_valid():
            instance.save()
            return redirect('view_categories')
    else:
        form = AddCategoryForm(instance=instance)
        is_update = True
    return render(request, 'app/category/add_category.html', {'form': form, 'is_update': is_update, 'id': id})


def delete_transaction(request, id):
    to_delete = Transaction.objects.get(id=id)
    to_delete.delete()
    return redirect("view_transaction")


def edit_transaction(request, id):
    instance = Transaction.objects.get(id=id)
    is_update = None
    if request.method == 'POST':
        form = AddTransactionForm(request.POST, instance=instance)
        if form.is_valid():
            instance.save()
            return redirect('view_transaction')
    else:
        form = AddTransactionForm(instance=instance)
        is_update = True
    return render(request, 'app/transaction/add_transaction.html', {'form': form, 'is_update': is_update, 'id': id})
