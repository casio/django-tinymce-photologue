from django.db import models
from django.template import Template as HTMLTemplate, Context
from photologue.models import PhotoSize

class Template(models.Model):
    name = models.CharField(max_length=255)
    size = models.ForeignKey(PhotoSize)
    template = models.TextField()

    def __unicode__(self):
        return self.name

    def render_template(self, photo):
        t = HTMLTemplate(self.template)
        image = getattr(photo, "get_%s_url" % self.size.name)()
        c = Context({'photo': photo, 'image': image})
        return t.render(c)
