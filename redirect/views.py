from django.http import HttpResponse, Http404, HttpResponseRedirect
from redirect.models import Redirect

def index(request):
    return HttpResponse("Hello, list of redirections")

def redirect(requset, short_key):
    try:
        redirect = Redirect.objects.get(short_key=short_key)
    except Redirect.DoesNotExist:
        raise Http404
    return HttpResponseRedirect(redirect.url)
