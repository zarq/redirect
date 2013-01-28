from django.shortcuts import render_to_response
from django.template import Context, loader, RequestContext
from django.http import HttpResponse, Http404, HttpResponseRedirect
from redirect.models import Redirect
from redirect.utils import encode_short_key

def index(request):
    all = Redirect.objects.all().order_by('created')
    t = loader.get_template('index.html')
    c = Context( {
        'all_redirects': all
    } )
    return HttpResponse(t.render(c))

def redirect(request, short_key):
    try:
        redirect = Redirect.objects.get(short_key=short_key)
    except Redirect.DoesNotExist:
        raise Http404
    return HttpResponseRedirect(redirect.url)

def add(request):
    if 'url' in request.POST:
        redirect = Redirect(url=request.POST['url'])
        redirect.save()
        short_key = encode_short_key(redirect.id)
        redirect.short_key = short_key
        redirect.save()
        return HttpResponseRedirect('/r/detail/' + redirect.short_key)
    else:
        return render_to_response('add.html', {},
                                  context_instance=RequestContext(request))

def detail(request, short_key):
    try:
        redirect = Redirect.objects.get(short_key=short_key)
    except Redirect.DoesNotExist:
        raise Http404
    t = loader.get_template('detail.html')
    c = Context({ 'redirect': redirect })
    return HttpResponse(t.render(c))

