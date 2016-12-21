from braces.views import LoginRequiredMixin, StaffuserRequiredMixin
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView

from apps.adm.forms import AdminTagForm, AdminHubForm, AdminPostForm
from apps.hubsapp.models import Tag, Hub, Post


class AdminDashboard(LoginRequiredMixin, StaffuserRequiredMixin, TemplateView):
    template_name = 'adm/index_admin.html'


# ----------------------------------------
# Tags
# ----------------------------------------


class AdminTagListView(LoginRequiredMixin, StaffuserRequiredMixin, ListView):
    model = Tag
    template_name = "adm/admin_tag_list.html"


class AdminTagCreateView(LoginRequiredMixin, StaffuserRequiredMixin, CreateView):
    model = Tag
    form_class = AdminTagForm
    template_name = 'adm/admin_tag_edit.html'
    success_url = reverse_lazy('adm:tag_list_view')


class AdminTagEditView(LoginRequiredMixin, StaffuserRequiredMixin, UpdateView):
    model = Tag
    form_class = AdminTagForm
    template_name = 'adm/admin_tag_edit.html'
    success_url = reverse_lazy('adm:tag_list_view')


class AdminTagDeleteView(LoginRequiredMixin, StaffuserRequiredMixin, DeleteView):
    model = Tag
    template_name = 'adm/admin_tag_confirm_delete.html'
    success_url = reverse_lazy('adm:tag_list_view')


#####
# ----------------------------------------
# Hubs
# ----------------------------------------

class AdminHubListView(LoginRequiredMixin, StaffuserRequiredMixin, ListView):
    model = Hub
    template_name = "adm/admin_hub_list.html"


class AdminHubCreateView(LoginRequiredMixin, StaffuserRequiredMixin, CreateView):
    model = Hub
    form_class = AdminHubForm
    template_name = 'adm/admin_hub_edit.html'
    success_url = reverse_lazy('adm:hub_list_view')


class AdminHubEditView(LoginRequiredMixin, StaffuserRequiredMixin, UpdateView):
    model = Hub
    form_class = AdminHubForm
    template_name = 'adm/admin_hub_edit.html'
    success_url = reverse_lazy('adm:hub_list_view')


class AdminHubDeleteView(LoginRequiredMixin, StaffuserRequiredMixin, DeleteView):
    model = Hub
    template_name = 'adm/admin_hub_confirm_delete.html'
    success_url = reverse_lazy('adm:hub_list_view')



# ----------------------------------------
# Posts
# ----------------------------------------
class AdminPostListView(LoginRequiredMixin, StaffuserRequiredMixin, ListView):
    model = Post
    template_name = "adm/admin_post_list.html"


class AdminPostCreateView(LoginRequiredMixin, StaffuserRequiredMixin, CreateView):
    model = Post
    form_class = AdminPostForm
    template_name = 'adm/admin_post_edit.html'
    success_url = reverse_lazy('adm:post_list_view')


class AdminPostEditView(LoginRequiredMixin, StaffuserRequiredMixin, UpdateView):
    model = Post
    form_class = AdminPostForm
    template_name = 'adm/admin_post_edit.html'
    success_url = reverse_lazy('adm:post_list_view')


class AdminPostDeleteView(LoginRequiredMixin, StaffuserRequiredMixin, DeleteView):
    model = Post
    template_name = 'adm/admin_post_confirm_delete.html'
    success_url = reverse_lazy('adm:post_list_view')

#####
