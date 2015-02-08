from django.conf.urls import patterns, include, url
from django.contrib import admin
from recommender import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'movieRecommender.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
     url(r'^$','recommender.views.index',name='index'),
      url(r'^suggestmovie/(?P<query>[\w|\W.@+-,\' \'\';\'%{}\[\]]+)/?$','recommender.views.suggestmovie',name='suggestmovie'),
)
