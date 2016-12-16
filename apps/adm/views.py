from braces.views import LoginRequiredMixin, StaffuserRequiredMixin
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView

from apps.adm.forms import AdminTagForm
from apps.hubsapp.models import Tag


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
