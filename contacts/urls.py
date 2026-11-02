from django.urls import path
from . import views

app_name = 'contacts'

urlpatterns = [
    path('', views.contact_list, name='contact_list'),
    path('add/', views.add_contact, name='add_contact'),
    path('search/', views.contact_search, name='contact_search'),

    path('delete/<int:contact_id>/', views.delete_contact, name='delete_contact'),

    path('edit/<int:contact_id>/', views.contact_edit, name='contact_edit'),
    path('row/<int:contact_id>/', views.contact_row, name='contact_row'),
    path('update/<int:contact_id>/', views.contact_update, name='contact_update'),
]