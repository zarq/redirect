from django.shortcuts import render_to_response
from django.template import Context, loader, RequestContext
from django.http import HttpResponse, Http404, HttpResponseRedirect
from redirect.models import Redirect
from redirect.utils import encode_short_key, encode_long_key

def index(request):
    all = Redirect.objects.all().order_by('created')
    return render_to_response(
        'index.html', {},
        context_instance=RequestContext(request))

def redirect_short(request, short_key):
    try:
        redirect = Redirect.objects.get(short_key=short_key)
    except Redirect.DoesNotExist:
        raise Http404
    return HttpResponseRedirect(redirect.url)

def redirect_long(request, long_key):
    try:
        redirect = Redirect.objects.get(long_key=long_key)
    except Redirect.DoesNotExist:
        raise Http404
    return HttpResponseRedirect(redirect.url)

def add(request):
    if 'url' in request.POST:
        redirect = Redirect(url=request.POST['url'])
        redirect.save()
        short_key = encode_short_key(redirect.id)
        redirect.short_key = short_key
        long_key = encode_long_key(redirect.id)
        redirect.long_key = long_key
        redirect.save()
        return HttpResponseRedirect('/r/_d/' + redirect.short_key)
    else:
        return render_to_response(
            'add.html', {},
            context_instance=RequestContext(request))

def detail(request, short_key):
    try:
        redirect = Redirect.objects.get(short_key=short_key)
    except Redirect.DoesNotExist:
        raise Http404
    return render_to_response(
        'detail.html', { 'redirect': redirect },
        context_instance=RequestContext(request))
