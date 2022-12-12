from django.shortcuts import render
from . import Genetic as gen
from . import Fuzzy as fz
from .forms import Form
from django.shortcuts import redirect


# Create your views here.


def getInput(request) :
    form = Form()
    set_of_weights = request.session.get('perfect_set_of_weights')
    generations = request.session.get('generations')
    
    
    # TÁI TẠO LẠI MẢNG TỪ STRING
    print("-------------------TAI TAO BTS-------------------\n")
    # Bộ trọng số tối ưu
    perfect_set_of_weights = []
    
    # Mảng các tiêu chí được cắt ra từ String BTS tối ưu
    tieu_chi = set_of_weights.split("d0")
    
    for i in range(len(tieu_chi) - 1):
        
        # Mảng tiêu chí i
        khoang_tieu_chi = []
        
        # Chia khoảng điểm của tiêu chí i
        cac_diem = tieu_chi[i].split("d1")
        
        for j in range(len(cac_diem) - 1):
            # Khoảng chặn của điểm j
            khoang_diem=[]
            
            # Mảng các giá trị trọng số của điểm j
            gioi_han_diem = cac_diem[j].split(" ")
            
            for z in gioi_han_diem:
                if len(z) != 0:
                    
                    # Chuyển từ string -> int
                    value_weight = int(z)
                    
                    khoang_diem.append(value_weight)
                    
            khoang_tieu_chi.append(khoang_diem)
            
        perfect_set_of_weights.append(khoang_tieu_chi)
                
    print(perfect_set_of_weights)
    
    # Khởi tạo bộ trọng số
    # Phòng trường hợp Submit khi chưa chạy thuật toán Genetic-Fuzzy
    set_of_weights = {'health_index': 0.0, 'y_health_Index': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]}
    

    context = {
        'form' : form
    }
    
    if request.method == 'POST':
        form = Form(request.POST)
        
        if form.is_valid():
            
            input = (form.cleaned_data)
            
            height = input.get('height')
            weight = input.get('weight')
            
            physical = height + weight
            print(type(physical))
            
            eye_sight = input.get('eye_sight')
            tooth_decay = input.get('tooth_decay')
            hearing_power = input.get('hearing_power')
            max_blood  = input.get('max_blood')
            size_skin = input.get('size_skin')
            length_difference = input.get('length_difference')
            
            input = [physical, eye_sight, tooth_decay, hearing_power, max_blood, size_skin, length_difference]
            set_of_weights = request.session.get('perfect_set_of_weights')
            
            print("------------------- BO TRONG SO TOI UU -------------------")
            print(set_of_weights)
            
            result = fz.fuzzy(perfect_set_of_weights, input) 
            
            context = {
                'health_index'      :  result['health_index'],
                'y_health_Index'    :  result['y_health_Index'],
                # 'generations'       :  request.session.get('generations')
            }
            print("-------------------LOG CONTEXT-------------------\n", context)
            
            return render(request, 'base/index.html', context)
    
    # print ('context:', context)
    return render(request, 'base/index.html', context)


def data(request):
    print("-------------------TIM BO TRONG SO TOI UU-------------------\n")
    
    perfect_individual = gen.genetic()
    
    perfect_set_of_weights = perfect_individual["perfect_set_of_weights"]
    count_generations = perfect_individual["generations"]
    
    
    print(perfect_set_of_weights)
    print(type(count_generations))
    
    # # print(perfect_individual)
    # # print(type(perfect_individual))
    
    
    # Đưa BTS tối ưu thành string để đưa vào trong session
    # Lưu ý: Không thể đưa mảng nhiều chiều vào trong session
    
    # Nếu cố đưa vào, sẽ gặp lỗi: "Object of type ndarray is 
    # not JSON serializable" 
    stri = ""
    for tieu_chi in range(len(perfect_set_of_weights)):
        for diem in range(len(perfect_set_of_weights[tieu_chi])):
            for trong_so in range(len(perfect_set_of_weights[tieu_chi][diem])):
                a = perfect_set_of_weights[tieu_chi][diem][trong_so]
                stri += str(a)
                stri += " "
            stri += "d1"
        stri += "d0"
    
    request.session['perfect_set_of_weights'] = stri
    request.session['generations'] = count_generations
    print(type(perfect_set_of_weights))
    print(type(count_generations))
    
    return redirect('http://localhost:8000/')




def dataPage(request):
    data_sample = gen.nap_du_lieu_mau()
    print(data_sample)
    
    context = {
        'data_sample': data_sample
    }
    return render(request, 'base/tables.html', context)