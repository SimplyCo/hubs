from django.http import HttpResponse
from django.template import Context, loader
from django.utils.translation import ugettext_lazy as _
from django.views.generic import ListView, TemplateView
from django.views.generic.detail import DetailView

from apps.hubsapp.models import Tag


class HomePage(TemplateView):
    # model = CourseRecord
    paginate_by = 20
    template_name = 'hubs/index.html'

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     return queryset.order_by('title')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        tags = Tag.objects.all()
        context['tags'] = tags

        return context



def rosetta_access_users(user):
    return user.is_authenticated() and user.is_staff


# Handle 403 Errors
def error403(request):
    template = loader.get_template('hubs/errors/403.html')
    context = Context({'message': _('Access denied'), })
    return HttpResponse(
        content=template.render(context),
        content_type='text/html; charset=utf-8',
        status=403
    )


# Handle 404 Errors
def error404(request):
    template = loader.get_template('hubs/errors/404.html')
    context = Context({'message': _('Page not found'), })
    return HttpResponse(
        content=template.render(context),
        content_type='text/html; charset=utf-8',
        status=404
    )


# Handle 500 Errors
def error500(request):
    template = loader.get_template('hubs/errors/500.html')
    context = Context({'message': _('Oops, something was broken'), })
    return HttpResponse(
        content=template.render(context),
        content_type='text/html; charset=utf-8',
        status=500
    )
