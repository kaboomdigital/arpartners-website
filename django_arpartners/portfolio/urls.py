from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^organisatie/$', views.organisatie, name='organisatie'),
    url(r'^directie/$', views.directie, name='directie'),
    url(r'^projecten/$', views.projecten, name='projecten'),
    url(r'^projecten/$', views.projecten, name='projecten'),
    url(r'^projecten/(?P<project_url>\D+)$', views.projecten_details, name='projecten_details'),
    url(r'^investeren/$', views.investeren, name='investeren'),
    # url(r'^partners/$', views.partners, name='partners'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^disclaimer/$', views.disclaimer, name='disclaimer'),
    # commented url
    # page not secured
    # url(r'^new-project-form/$', views.new_project_form, name='new_project_form'),
    url(r'^new-project/$', views.new_project, name='new project'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
