from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^tinymce-photologue/$', 'tinymce_photologue.views.index', name="tinymce_photologue"),
)
