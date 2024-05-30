from django.urls import path
from .views import StudentsCreateView, StudentsDetailView, StudentsUpdateView, StudentsDeleteView, StudentsListView

urlpatterns = [
    path('', StudentsListView.as_view(), name='post_list'),
    path('create/', StudentsCreateView.as_view(), name='post_create'), 
    path('<int:pk>/', StudentsDetailView.as_view(), name='post_detail'), 
    path('<int:pk>/update/', StudentsUpdateView.as_view(), name='post_update'), 
    path('<int:pk>/delete/', StudentsDeleteView.as_view(), name='post_delete'),  
] 