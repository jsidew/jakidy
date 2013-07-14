from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext
# from django.utils.simplejson import dumps

from food.models import Food

def index(request):
    f = Food.objects.all().order_by('name')
    c = {'foods' : f} 
    c.update(csrf(request))
    return render_to_response('index.html', c,
                              context_instance=RequestContext(request))

def manifest(request):
    import md5
    import os
    from jakidy.settings import STATIC_URL
    path = os.path.join(os.path.dirname(__file__), 'static')
    filters = ['.js', '.css', '.gif', '.jpg', '.png']
    hashes = []
    files = []
    data = "CACHE MANIFEST\n"
    for root, _, fnames in os.walk(path):
        for fn in fnames:
            if fn[fn.rfind('.'):] not in filters:
                continue
            with open(os.path.join(root, fn), 'rb') as f:
                hashes.append(md5.new(f.read()).hexdigest())
            files.append('{}{}'.format(STATIC_URL, fn))
    # index.html / homepage
    with open(
        os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            'templates', 'index.html'), 'rb') as f:
        hashes.append(md5.new(f.read()).hexdigest())
    
    data = "{}{}\n# hash: {}\n".format(
        data, "\n".join(files), md5.new(''.join(hashes)).hexdigest())
            
    return HttpResponse(data, mimetype='text/cache-manifest')

def save(request):
    data = ''
    try:
        rid = request.POST['id']
        if rid:
            food = Food.objects.get(pk=int(rid))
            food.name = request.POST['name']
            food.protein = request.POST['protein']
            food.carbs = request.POST['carbs']
            food.fat = request.POST['fat']
        else:
            food = Food.objects.create(
                name = request.POST['name'],
                protein = request.POST['protein'],
                carbs = request.POST['carbs'],
                fat = request.POST['fat']
            )
        food.save()
        data = '{"message":"OK"}'
    except:
        data = '{"message":"KO"}'
    return HttpResponse(data, mimetype='application/json')
    
    
