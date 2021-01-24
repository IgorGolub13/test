

from django.urls import path, include
from . import views

urlpatterns = [
    path('category', views.view_categories, name='view_categories'),
    path('category/create', views.add_category, name='add_category'),
    path('category/<int:id>/update', views.edit_category, name='edit_category'),
    path('category/<int:id>/delete', views.delete_category, name='delete_category'),

    path('transaction', views.view_transaction, name='view_transaction'),
    path('transaction/create', views.add_transaction, name='add_transaction'),
    path('transaction/<int:id>/update', views.edit_transaction, name='edit_transaction'),
    path('transaction/<int:id>/delete', views.delete_transaction, name='delete_transaction'),

]