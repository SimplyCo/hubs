from datetime import datetime

from django.conf import settings
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import authenticate, login as auth_login
from django.http import HttpResponseRedirect
from django.utils.timezone import utc
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView

from apps.accounts.forms import RegistrationForm
from apps.accounts.models import CustomUser, UserConfirmToken
from apps.accounts.utils import send_confirm_email

from braces.views import AnonymousRequiredMixin, LoginRequiredMixin


class ClientRegistration(AnonymousRequiredMixin, FormView):
    template_name = 'accounts/registration.html'
    authenticated_redirect_url = reverse_lazy('home')
    form_class = RegistrationForm

    def get_success_url(self):
        if self.request.GET.get('next'):
            return self.request.GET.get('next')
        return reverse_lazy('home')

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            email, password = form.save()
            user = authenticate(username=email, password=password)
            if user is not None and user.is_active:
                # Send confirm email to user
                send_confirm_email(user=user, request=request)
                auth_login(request, user)
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.form_invalid(form)


class ConfirmEmail(TemplateView):
    template_name = 'accounts/confirm/already_confirm.html'

    def get(self, request, *args, **kwargs):
        uidb64 = kwargs.get('uidb64')
        token = kwargs.get('token')
        try:
            token = UserConfirmToken.objects.get(uid=uidb64, token=token)
        except UserConfirmToken.DoesNotExist:
            pass
        else:
            token_days = (datetime.utcnow().replace(tzinfo=utc) - token.created).days
            if token_days <= settings.TOKEN_LIFE_DAYS and not token.used:
                token.used = True
                token.save()
                token.user.email_confirmed = True
                token.user.save()
                context = self.get_context_data(**kwargs)
                return self.render_to_response(context)
        return HttpResponseRedirect(reverse_lazy('accounts:confirm_failed'))


class ConfirmEmailFailed(TemplateView):
    template_name = 'accounts/confirm/confirm_failed.html'


class PersonalRoom(LoginRequiredMixin, TemplateView):
    model = CustomUser
    template_name = 'accounts/personal_room.html'