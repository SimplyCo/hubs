from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.template import loader
from apps.accounts.models import REASON_CONFIRM, UserConfirmToken
# from apps.accounts.tasks import custom_send_email


def send_confirm_email(user, request):
    domain_override = request.get_host()
    if not domain_override:
        current_site = get_current_site(request)
        site_name = current_site.name
        domain = current_site.domain
    else:
        site_name = domain = domain_override

    token = UserConfirmToken.objects.create(
        user=user,
        reason=REASON_CONFIRM,
    )
    context = {
        'email': user.email,
        'protocol': 'https' if request.is_secure() else 'http',
        'site_name': site_name,
        'domain': domain,
        'uid': token.uid,
        'user': user,
        'token': token.token,
    }

    subject_path = 'accounts/confirm/confirm_subject.txt'
    email_template_name_path = 'accounts/confirm/generate_link.html'
    subject = loader.render_to_string(subject_path, context)
    subject = ''.join(subject.splitlines())
    body = loader.render_to_string(email_template_name_path, context)
    # TODO replace to send mails via mailgun
    # if settings.EMAIL_FAKE:
    #     # TODO => write in logger
    #     print('='*100)
    #     print('send email from {0} to {1}'.format(settings.DEFAULT_FROM_EMAIL, user.email))
    #     print(subject)
    #     print(body)
    #     print('='*100)
    # else:
    #     custom_send_email.apply_async(args=(
    #         subject,
    #         body,
    #         settings.DEFAULT_FROM_EMAIL,
    #         [user.email],
    #         context,
    #         None
    #     ))