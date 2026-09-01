from django.urls import path
from .views import memo_list, memo_detail

urlpatterns = [
    path('memos/', memo_list),
    path('memos/<int:pk>/', memo_detail),
]
