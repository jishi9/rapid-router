from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'game.views.game'),
    url(r'^submit_commands$', 'game.views.submit_commands'),
    url(r'^submit_reply$', 'game.views.submit_reply'),
)
