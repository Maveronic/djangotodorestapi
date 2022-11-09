from django.urls import path
from todos.views import TodosAPIView, TodoDetail

urlpatterns = [
    path('', TodosAPIView.as_view(), name='todos'),
    path('<int:id>', TodoDetail.as_view(), name='todo'),
]
