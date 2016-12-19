from django.conf.urls import url, include

from apps.adm import views


urlpatterns = [

    url(r'^$', views.AdminDashboard.as_view(), name='dashboard'),

    url(r'^tags/$', views.AdminTagListView.as_view(), name='tag_list_view'),
    url(r'^tags/new/$', views.AdminTagCreateView.as_view(), name='tag_create_view'),
    url(r'^tags/(?P<pk>\d+)/edit/$', views.AdminTagEditView.as_view(), name='tag_edit_view'),
    url(r'^tags/(?P<pk>\d+)/delete$', views.AdminTagDeleteView.as_view(), name='tag_delete_view'),

    url(r'^hubs/$', views.AdminHubListView.as_view(), name='hub_list_view'),
    url(r'^hubs/new/$', views.AdminHubCreateView.as_view(), name='hub_create_view'),
    url(r'^hubs/(?P<pk>\d+)/edit/$', views.AdminHubEditView.as_view(), name='hub_edit_view'),
    url(r'^hubs/(?P<pk>\d+)/delete$', views.AdminHubDeleteView.as_view(), name='hub_delete_view'),




    url(r'^redactor/', include('apps.adm.redactor_admin.urls')),

]
