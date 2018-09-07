from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^news/$', views.news_view, name="NewsPage"),
    url(r'^$', views.main_page, name="MainPage"),
    url(r'^contacts/$', views.contacts_view, name="ContactsPage"),
    url(r'^activity/$', views.activity_view, name="ActivityPage"),
    url(r'^activity/(?P<activity_slug>[-\w]+)/$', views.activity_view, name="ActivityPageList"),
    # url(r'^expertise/$', views.expertise_view, name="ExpertisePage"),
    url(r'^contact-send/$', views.contact_send, name="ContactSend"),
]
