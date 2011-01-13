from django.conf.urls.defaults import *
from piston.resource import Resource
from tinymce_photologue.api.handlers import PhotologueHandler, PhotologueTemplatesHandler

photologue_handler = Resource(PhotologueHandler)
photologue_templates_handler = Resource(PhotologueTemplatesHandler)

urlpatterns = patterns('',
    url(r'^$', photologue_handler, name="tinymce_photologue_api"),
    url(r'^templates/$', photologue_templates_handler, name="tinymce_photologue_templates"),
    url(r'^templates/(?P<id>\d+)/$', photologue_templates_handler, name="tinymce_photologue_template"),
)
