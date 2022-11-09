from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from todos.serializers import TodoSerializer
from rest_framework.permissions import IsAuthenticated
from todos.models import Todo
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from todos.pagination import CustomPageNumberPagination


class TodosAPIView(ListCreateAPIView):
    serializer_class = TodoSerializer
    pagination_class = CustomPageNumberPagination
    permission_classes = (IsAuthenticated,)
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    filterset_fields = ['id', 'title', 'description', 'is_complete']
    search_fields = ['id', 'title', 'description', 'is_complete']
    ordering_fields = ['id', 'title', 'description', 'is_complete']

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def get_queryset(self):
        return Todo.objects.filter(owner=self.request.user)


class TodoDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = TodoSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = 'id'

    def get_queryset(self):
        return Todo.objects.filter(owner=self.request.user)
