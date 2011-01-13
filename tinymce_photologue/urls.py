from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^$', 'tinymce_photologue.views.index', name="tinymce_photologue"),
    (r'^api/', include('tinymce_photologue.api.urls')),
)
