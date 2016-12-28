from django import forms
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.forms import SetPasswordForm, PasswordResetForm
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.template import loader

# from .tasks import custom_send_email
from .models import CustomUser, UserConfirmToken, REASON_RESET
from apps.hubsapp.models import Post


class RegistrationForm(forms.Form):

    email = forms.EmailField(required=True, label=_('E-mail'),
                             widget=forms.TextInput(attrs={'placeholder': 'Your@email.com'}))
    user_name = forms.CharField(max_length=30, label=_('Name'),
                                widget=forms.TextInput(attrs={'placeholder': 'Full name'}))
    password = forms.CharField(min_length=6, max_length=30, required=True, label=_('Password'),
                               widget=forms.PasswordInput(attrs={'placeholder': 'Please enter password'}))
    password_again = forms.CharField(min_length=6, max_length=30, required=True, label=_('Re-enter password'),
                                     widget=forms.PasswordInput(attrs={'placeholder': 'Please re-enter password'}))

    def clean_email(self):
        if CustomUser.objects.filter(email=self.cleaned_data.get('email')).exists():
            raise forms.ValidationError(_("User with such email already exists!"))
        return self.cleaned_data.get('email')

    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        if cleaned_data.get('password') is None or cleaned_data.get('password') != cleaned_data.get('password_again'):
            self.add_error('password', _('Password mismatch.'))
        return cleaned_data

    def save(self):
        new_user = CustomUser.objects.create_user(
            email=self.cleaned_data.get('email'),
            password=self.cleaned_data.get('password'),
            user_name=self.cleaned_data.get('user_name'),
        )
        return new_user.email, self.cleaned_data.get('password')


class ResetPassword(SetPasswordForm):
    new_password1 = forms.CharField(label=_("New password"),
                                    widget=forms.PasswordInput, min_length=6, max_length=30)
    new_password2 = forms.CharField(label=_("New password confirmation"),
                                    widget=forms.PasswordInput, min_length=6, max_length=30)


class CustomPasswordResetForm(PasswordResetForm):

    def send_mail(self, subject_template_name, email_template_name,
                  context, from_email, to_email, html_email_template_name=None):
        """
        Sends a django.core.mail.EmailMultiAlternatives to `to_email`.
        """
        subject = loader.render_to_string(subject_template_name, context)
        # Email subject *must not* contain newlines
        subject = ''.join(subject.splitlines())
        body = loader.render_to_string(email_template_name, context)
        # TODO change to send mails via mailgun
        # Print email in console or send by celery
        # if settings.EMAIL_FAKE:
        #     # TODO => write in logger
        #     print('='*100)
        #     print('send email from {0} to {1}'.format(from_email, to_email))
        #     print(subject)
        #     print(body)
        #     print('='*100)
        # else:
        #     custom_send_email.apply_async(args=(
        #         subject,
        #         body,
        #         from_email,
        #         [to_email],
        #         context,
        #         html_email_template_name
        #     ))

    def save(self, domain_override=None,
             subject_template_name='registration/password_reset_subject.txt',
             email_template_name='registration/password_reset_email.html',
             use_https=False, token_generator=default_token_generator,
             from_email=None, request=None, html_email_template_name=None,
             extra_email_context=None):
        """
        Generates a one-use only link for resetting password and sends to the
        user.
        """
        email = self.cleaned_data["email"]
        for user in self.get_users(email):
            if not domain_override:
                current_site = get_current_site(request)
                site_name = current_site.name
                domain = current_site.domain
            else:
                site_name = domain = domain_override
            # Create token for user and generate some uid
            token = UserConfirmToken.objects.create(
                user=user,
                reason=REASON_RESET,
            )
            context = {
                'email': user.email,
                'domain': domain,
                'site_name': site_name,
                'uid': token.uid,
                'user': user,
                'token': token.token,
                'protocol': 'https' if use_https else 'http',
            }
            if extra_email_context is not None:
                context.update(extra_email_context)
            self.send_mail(subject_template_name, email_template_name,
                           context, from_email, user.email,
                           html_email_template_name=html_email_template_name)


#####
class BlogerPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['author', 'title', 'slug', 'leading_image', 'short_text', 'full_text', 'status', 'placement', 'hub']

#####
