from django.conf.urls import patterns, url

urlpatterns = patterns('apps.adm.redactor_admin.views',
                       url(
                           r'^upload/image/$', 'upload_image', name="admin_redactor_upload_image"
                       ),
                       )
