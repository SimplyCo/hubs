# from datetime import datetime

# from django.conf import settings
# from django.contrib.auth.views import deprecate_current_app
# from django.contrib.auth import REDIRECT_FIELD_NAME, login as auth_login
# from django.contrib.auth.forms import SetPasswordForm, AuthenticationForm
# from django.contrib.auth.tokens import default_token_generator
# from django.contrib.sites.shortcuts import get_current_site
# from django.core.urlresolvers import reverse
# from django.http import HttpResponseRedirect
# from django.shortcuts import resolve_url, get_object_or_404
# from django.template.response import TemplateResponse
# from django.utils.http import is_safe_url
# from django.utils.translation import ugettext as _
# from django.utils.timezone import utc
# from django.views.decorators.csrf import csrf_protect
# from django.views.decorators.cache import never_cache
# from django.views.decorators.debug import sensitive_post_parameters

# from apps.accounts.models import UserConfirmToken


# @deprecate_current_app
# @sensitive_post_parameters()
# @csrf_protect
# @never_cache
# def login(request, template_name='registration/login.html',
#           redirect_field_name=REDIRECT_FIELD_NAME,
#           redirect_admin_field_name=REDIRECT_FIELD_NAME,
#           authentication_form=AuthenticationForm,
#           extra_context=None):
#     """
#     Displays the login form and handles the login action.
#     """
#     redirect_to = request.POST.get(redirect_field_name,
#                                    request.GET.get(redirect_field_name, ''))
#     next_url = request.GET.get('next')
#     if request.method == "POST":
#         form = authentication_form(request, data=request.POST)
#         if form.is_valid():

#             # Ensure the user-originating redirection url is safe.
#             if not is_safe_url(url=redirect_to, host=request.get_host()):
#                 redirect_to = resolve_url(settings.LOGIN_REDIRECT_URL)

#             # Okay, security check complete. Log the user in.
#             user = form.get_user()
#             auth_login(request, user)
#             # If user is staff - redirect to admin dashboard

#             if next_url:
#                 redirect_to = next_url
#             else:
#                 redirect_to = redirect_admin_field_name if user.is_staff else redirect_to
#             return HttpResponseRedirect(redirect_to)
#     else:
#         form = authentication_form(request)

#     current_site = get_current_site(request)

#     context = {
#         'form': form,
#         redirect_field_name: redirect_to,
#         'site': current_site,
#         'site_name': current_site.name,
#         'next_url': next_url
#     }
#     if extra_context is not None:
#         context.update(extra_context)

#     return TemplateResponse(request, template_name, context)


# # Doesn't need csrf_protect since no-one can guess the URL
# @sensitive_post_parameters()
# @never_cache
# @deprecate_current_app
# def password_reset_confirm(request, uidb64=None, token=None,
#                            template_name='registration/password_reset_confirm.html',
#                            token_generator=default_token_generator,
#                            set_password_form=SetPasswordForm,
#                            post_reset_redirect=None,
#                            extra_context=None):
#     """
#     View that checks the hash in a password reset link and presents a
#     form for entering a new password.
#     """
#     assert uidb64 is not None and token is not None  # checked by URLconf
#     if post_reset_redirect is None:
#         post_reset_redirect = reverse('accounts:password_reset_complete')
#     else:
#         post_reset_redirect = resolve_url(post_reset_redirect)
#     try:
#         # urlsafe_base64_decode() decodes to bytestring on Python 3
#         token = get_object_or_404(UserConfirmToken, uid=uidb64, token=token)
#         user = token.user
#         token_days = (datetime.utcnow().replace(tzinfo=utc) - token.created).days
#     except Exception:
#         user = None
#         token_days = 0
#     # If we have some user and token not old
#     if user is not None and token_days <= settings.TOKEN_LIFE_DAYS and not token.used:
#         validlink = True
#         title = _('Enter new password')
#         if request.method == 'POST':
#             form = set_password_form(user, request.POST)
#             if form.is_valid():
#                 form.save()
#                 # Mark token as used
#                 token.used = True
#                 token.save()
#                 return HttpResponseRedirect(post_reset_redirect)
#         else:
#             form = set_password_form(user)
#     else:
#         validlink = False
#         form = None
#         title = _('Password reset unsuccessful')
#     context = {
#         'form': form,
#         'title': title,
#         'validlink': validlink,
#     }
#     if extra_context is not None:
#         context.update(extra_context)

#     return TemplateResponse(request, template_name, context)
