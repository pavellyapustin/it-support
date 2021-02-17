from django.urls import path
from . import views

urlpatterns = [
    path('', views.JobListView.as_view(), name='services-home'),
    path('technician/<str:username>', views.UserJobListView.as_view(), name='technician-jobs'),
    path('job/by_title/', views.TitleJobListView.as_view(), name='title-jobs'),
    path('job/by_period/', views.PeriodJobListView.as_view(), name='title-jobs'),
    path('job/<int:pk>/', views.JobDetailView.as_view(), name='job-detail'),
    path('job/new/', views.JobCreateView.as_view(), name='job-create'),
    path('job/<int:pk>/update/', views.JobUpdateView.as_view(), name='job-update'),
    path('job/<int:pk>/delete/', views.JobDeleteView.as_view(), name='job-delete'),
    path('about/', views.about, name='services-about'),
]
