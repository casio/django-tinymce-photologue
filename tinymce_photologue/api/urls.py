from django.conf.urls.defaults import *
from piston.resource import Resource
from tinymce_photologue.api.handlers import PhotologueHandler

photologue_handler = Resource(PhotologueHandler)

urlpatterns = patterns('',
    url(r'^$', photologue_handler, name="tinymce_photologue_api"),
)
