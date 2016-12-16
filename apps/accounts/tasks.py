# from django.core.mail.message import EmailMultiAlternatives
# from django.template import loader
#
# from celery.task import task
#
#
# # Task for send mail
# @task(ignore_result=True, name='custom_send_email')
# def custom_send_email(subject, body, from_email, recipients, context, html_email_template_name):
#     email_message = EmailMultiAlternatives(subject, body, from_email, recipients)
#     if html_email_template_name is not None:
#         html_email = loader.render_to_string(html_email_template_name, context)
#         email_message.attach_alternative(html_email, 'text/html')
#     print('send email from {0} to {1}'.format(from_email, recipients))
#     email_message.send()
