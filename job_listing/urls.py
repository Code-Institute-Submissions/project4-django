from django.urls import path, include
from .views import show_listing, add_listing, edit_listing, confirm_delete, delete_job

urlpatterns = [
    path('', show_listing, name='show_listing'),
    path('add_listing/', add_listing, name='add_listing'),
    path('edit_listing/<id>', edit_listing, name='edit_listing'),
    path('confirm_delete/<id>', confirm_delete, name='confirm_delete'),
    path('delete_job/<id>', delete_job, name='delete_job'),
]
