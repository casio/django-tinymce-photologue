from django.shortcuts import render_to_response
from django.template import RequestContext
from tinymce_photologue.models import Template

def index(request):
    photo_templates = Template.objects.all()
    return render_to_response("tinymce_photologue/index.html", {'photo_templates': photo_templates}, context_instance=RequestContext(request))
