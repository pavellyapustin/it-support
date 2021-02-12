from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Job


def home(request):
    context = { 'jobs': Job.objects.all() }
    return render(request, 'services/home.html', context)

class JobListView(ListView):
    model = Job
    template_name = 'services/home.html'
    context_object_name = 'jobs'
    ordering = ['-date_posted']
    paginate_by = 5


class UserJobListView(ListView):
    model = Job
    template_name = 'services/user_jobs.html'
    context_object_name = 'jobs'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Job.objects.filter(technician=user).order_by('-date_posted')


class JobDetailView(DetailView):
    model = Job


class JobCreateView(LoginRequiredMixin, CreateView):
    model = Job
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.technician = self.request.user
        return super().form_valid(form)


class JobUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Job
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.technician = self.request.user
        return super().form_valid(form)

    def test_func(self):
        job = self.get_object()
        if self.request.user == job.technician:
            return True
        return False


class JobDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Job
    success_url = '/'

    def test_func(self):
        job = self.get_object()
        if self.request.user == job.technician:
            return True
        return False


def about(request):
    return render(request, 'services/about.html', {'title': 'About'})
