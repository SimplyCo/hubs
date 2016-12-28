from django.conf import settings
from django.conf.urls import url
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import views as auth_views

from . import views
from .forms import ResetPassword, CustomPasswordResetForm


urlpatterns = [
    url(r'^registration/$', views.ClientRegistration.as_view(), name='registration'),
    url(r'^email/confirm/(?P<uidb64>[A-Za-z]+)-(?P<token>.+)/$',
        views.ConfirmEmail.as_view(), name='email_confirm'),
    url(r'^email/confirm_failed/$', views.ConfirmEmailFailed.as_view(), name='confirm_failed'),

    url(r'^dashboard/$', views.PersonalRoom.as_view(), name='dashboard'),
    #####
    url(r'^bloger_posts/$', views.BlogerPostListView.as_view(), name='bloger_post_list_view'),
    url(r'^bloger_posts/new/$', views.BlogerPostCreateView.as_view(), name='bloger_post_create_view'),
    url(r'^bloger_posts/(?P<pk>\d+)/edit/$', views.BlogerPostEditView.as_view(), name='bloger_post_edit_view'),
    url(r'^bloger_posts/(?P<pk>\d+)/delete$', views.BlogerPostDeleteView.as_view(), name='bloger_post_delete_view'),
    #####

    url(r'^login/$', views.login,
        {
            # 'redirect_field_name': settings.LOGIN_REDIRECT_URL,
            'redirect_admin_field_name': settings.LOGIN_ADMIN_REDIRECT_URL,
            'template_name': 'accounts/login.html',
        }, name="login"),

    url(r'^logout/$', auth_views.logout,
        {'next_page': settings.LOGOUT_URL},
        name="logout"
    ),

    # 1 input email for reset
    url(r'^reset/$', auth_views.password_reset,
        {
            'template_name': 'accounts/forget/forget_password.html',
            'email_template_name': 'accounts/forget/generate_link.html',
            'password_reset_form': CustomPasswordResetForm,
            'subject_template_name': 'accounts/forget/reset_subject.txt',
            'post_reset_redirect': reverse_lazy('accounts:email_sent'),
            'from_email': settings.DEFAULT_FROM_EMAIL
        },
        name='reset'),

    # 2 email sent
    url(r'^reset/success/$', auth_views.password_reset_done,
        {'template_name': 'accounts/forget/send_link.html'},
        name='email_sent'),

    # 3 reset password
    url(r'^reset/confirm/(?P<uidb64>[A-Za-z]+)-(?P<token>.+)/$',
        views.password_reset_confirm,
        {
            'template_name': 'accounts/forget/input_new_password.html',
            'set_password_form': ResetPassword,
            'post_reset_redirect': reverse_lazy('accounts:reset_password_complete')
        },
        name='reset_password'),

    # 4 already reset
    url(r'^reset/done/$', auth_views.password_reset_complete,
        {'template_name': 'accounts/forget/already_reset.html'},
        name='reset_password_complete'),



]
