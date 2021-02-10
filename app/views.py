from django.db.models import Sum
from django.db.models.functions import Lower
from django.shortcuts import render, redirect
from slick_reporting.fields import SlickReportField
from slick_reporting.views import SlickReportView

from .models import Category, Transaction
from .forms import AddCategoryForm, AddTransactionForm
from django.template.loader import render_to_string
from django.http import JsonResponse


# Create your views here.

def view_categories(request):
    context = {}
    url_parameter = request.GET.get("q")

    if url_parameter:
        category = Category.objects.filter(name__icontains=url_parameter)
    else:
        category = Category.objects.all()

    context["category"] = category

    if request.is_ajax():
        html = render_to_string(
            template_name="app/category/category-results-partial.html",
            context={"category": category}
        )

        data_dict = {"html_from_view": html}

        return JsonResponse(data=data_dict, safe=False)

    return render(request, 'app/category/list.html', context=context)


def view_transaction(request):
    context = {}
    url_parameter = request.GET.get("q")

    if url_parameter:
        transactions = Transaction.objects.filter(category__name__icontains=url_parameter)
    else:
        transactions = Transaction.objects.all()

    context["transactions"] = transactions
    context["categories"] = [category.name for category in Category.objects.all()]

    if request.is_ajax():
        html = render_to_string(
            template_name="app/transaction/transaction-results-partial.html",
            context={"transactions": transactions}
        )

        data_dict = {"html_from_view": html}

        return JsonResponse(data=data_dict, safe=False)

    return render(request, 'app/transaction/list.html', context=context)


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


class SimpleListReport(SlickReportView):
    report_model = Transaction
    report_title = 'Report'
    date_field = 'date'
    template_name = 'app/report/report_select.html'

    group_by = 'category__name'
    columns = ['category__name', SlickReportField.create(Sum, 'value', name='value__sum', verbose_name='Price'),]

    # crosstab_model = 'client'
    # crosstab_columns = [SlickReportField.create(Sum, 'value', name='value__sum', verbose_name=_('Sales'))]
    # crosstab_compute_reminder = True  # if False the "Reminder" Column will not be computed

    chart_settings = [
        {
            'type': 'pie',
            'data_source': ['value__sum'],
            'plot_total': True,  # Plot total works here too
            'title_source': ['category__name'],
            'title': 'Per categories pie',

        },
        {
            'type': 'bar',
            'data_source': ['value__sum'],
            'title_source': ['category__name'],
            'title': 'Per categories bar',

        },
    ]
