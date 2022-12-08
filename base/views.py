from django.shortcuts import render
from django.http import HttpResponse
from . import Genetic as gen
from . import Fuzzy as fz
from .forms import Form
from django.shortcuts import redirect


# Create your views here.


def getInput(request) :
    form = Form()
    
    print(form)
    if request.method == 'POST':
        
        print("POST: ", request.POST)
        form = Form(request.POST)
        
        if form.is_valid():
            input = (form.cleaned_data)
            
            
            height = input.get('height'),
            weight = input.get('weight'),
            
            
            physical = height + weight
            eye_sight = input.get('eye_sight'),
            tooth_decay = input.get('tooth_decay'),
            hearing_power = input.get('hearing_power'),
            max_blood  = input.get('max_blood'),
            size_skin = input.get('size_skin'),
            length_difference = input.get('length_difference')
            
            input = [physical, eye_sight, tooth_decay, hearing_power, max_blood, size_skin, length_difference]
            set_of_weights = request.session.get('perfect_individual')
            
            result = fz.fuzzy(set_of_weights, input) 
            # result=0
            context = {
                'health_index'      :  result['health_index'],
                'y_health_Index'    :  result['y_health_Index'],
                'generations'       :  request.session.get('generations')
            }
            
            context = {
                'height' : 14,
                'weight' : 48,
                'eye_sight' : 20,
                'tooth_decay' : 3,
                'hearing_power' : 11,
                'max_blood' : 112,
                'size_skin' : 0,
                'length_difference' : 0
            }
            
            return render(request, 'base/index.html', context)
            
    context = {
            'form' : form
        }
    
    print ('context:', context)
    return render(request, 'base/index.html', context)


def data(request):
    form = Form()
    
    if request.method == 'POST':
        
        perfect_set_of_weights = gen.genetic()
        
        perfect_individual = perfect_set_of_weights["perfect_individual"]
        generations = perfect_set_of_weights["generations"]
        
        print(perfect_set_of_weights)
        
        request.session['perfect_individual'] = perfect_individual
        request.session['generations'] = generations
        
        return redirect('get_input_url')
    context = {
        "form": form
    }
    return render(request, 'base/tables.html', context)