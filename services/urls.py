from django.urls import path
from .views import JobListView, JobDetailView, JobCreateView, JobUpdateView, JobDeleteView, UserJobListView
from . import views

urlpatterns = [
    path('', JobListView.as_view(), name='services-home'),
    path('technician/<str:username>', UserJobListView.as_view(), name='technician-jobs'),
    path('job/<int:pk>/', JobDetailView.as_view(), name='job-detail'),
    path('job/new/', JobCreateView.as_view(), name='job-create'),
    path('job/<int:pk>/update/', JobUpdateView.as_view(), name='job-update'),
    path('job/<int:pk>/delete/', JobDeleteView.as_view(), name='job-delete'),
    path('about/', views.about, name='services-about'),
]
