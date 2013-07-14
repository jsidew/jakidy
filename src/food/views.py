from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext
# from django.utils.simplejson import dumps

from food.models import Food, FoodName

def index(request):
    fn = FoodName.objects.filter(lang='EN').order_by('name')
    c = {'foods':fn} 
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
        food = Food.objects.create(
            family = request.POST['family'],
            species = request.POST['species'],
            kcal = request.POST['kcal'],
            kcc = request.POST['kcc'],
            kcf = request.POST['kcf'],
            kcp = request.POST['kcp'],
            carbs = request.POST['carbs'],
            sugar = request.POST['sugar'],
            fiber = request.POST['fiber'],
            starch = request.POST['starch'],
            fats = request.POST['fats'],
            monounsat = request.POST['monounsat'],
            polyunsat = request.POST['polyunsat'],
            saturated = request.POST['saturated'],
            proteins = request.POST['proteins'],
            water = request.POST['water'],
            ash = request.POST['ash'],
            state = request.POST['state'],
        )
        food.save()
        foodname = FoodName.objects.create(
            name = request.POST['name'],
            food = food,
            notes = request.POST['notes'],
        )
        foodname.save()
        data = '{"message":"OK"}'
    except:
        data = '{"message":"KO"}'
    return HttpResponse(data, mimetype='application/json')
    
    