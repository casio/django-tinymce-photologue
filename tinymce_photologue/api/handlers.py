from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django import forms
from piston.handler import BaseHandler
from piston.utils import rc
from photologue.models import Photo, PhotoSize
from tinymce_photologue.models import Template

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

class PhotologueTemplatesHandler(BaseHandler):
    allowed_methods = ('GET',)
    fields = ('id', 'name')
    model = Template

    def read(self, request, id=None):
        if id != None:
            photo = Photo.objects.get(pk=int(request.GET.get('photo_id')))
            m = Template.objects.get(pk=id)
            return m.render_template(photo)

        return self.model.objects.all()
