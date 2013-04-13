from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from django.http import HttpResponse
# from django.utils.simplejson import dumps

from food.models import Food, FoodName


def index(request):
    fn = FoodName.objects.filter(lang='EN').order_by('name')
    c = {'foods':fn} 
    c.update(csrf(request))
    return render_to_response('index.html', c)

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
    
    