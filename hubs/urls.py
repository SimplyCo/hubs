from django.conf import settings
from django.conf.urls import url, include

from . import views

# urlpatterns = [
#     url(r'^i18n/', include('django.conf.urls.i18n')),
# ]
#
# urlpatterns += i18n_patterns(
#     # url(r'^admin/', admin.site.urls),
#     url(r'^$', views.HomePage.as_view(), name='home'),
#     url(r'^accounts/', include('apps.accounts.urls', namespace='accounts')),
#     url(r'^adm/', include('apps.adm.urls', namespace='adm')),
# )

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^adm/', include('apps.adm.urls', namespace='adm')),
    url(r'^accounts/', include('apps.accounts.urls', namespace='accounts')),


    url(r'^$', views.HomePage.as_view(), name='home'),

]

# media files
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if 'rosetta' in settings.INSTALLED_APPS:
#     urlpatterns += [
#         url(r'^rosetta/', include('rosetta.urls')),
#     ]

handler403 = views.error403
handler404 = views.error404
handler500 = views.error500


urlpatterns += (
    url(r'^redactor/', include('redactor.urls')),
)
