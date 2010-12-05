from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django import forms
from piston.handler import BaseHandler
from piston.utils import rc
from photologue.models import Photo

class PhotologueHandler(BaseHandler):
    allowed_methods = ('GET',)
    fields = ('id', 'title', 'thumb', 'photo')
    model = Photo

    @classmethod
    def thumb(cls, model):
        return model.get_admin_thumbnail_url()

    @classmethod
    def photo(cls, model):
        return model.get_page_url()
