import numpy as np
import pandas as pd
import json
import random
from . import Fuzzy as fuzz


# KHOI TAO BO TRONG SO
# physical
physical_1 = np.array([0, 0, 0, 0])
physical_2 = np.array([0, 0, 0, 0])
physical_3 = np.array([0, 0, 0, 0])
physical_4 = np.array([0, 0, 0, 0])
physical_5 = np.array([0, 0, 0, 0])
physical_6 = np.array([0, 0, 0, 0])

physical_weight = [physical_1, physical_2,   
                   physical_3, physical_4,    
                   physical_5, physical_6]
# print("\nThe luc: \n", physical_weight)


# eye sight
eye_1 = np.array([0, 0, 0])
eye_2 = np.array([0, 0, 0])
eye_3 = np.array([0, 0, 0])
eye_4 = np.array([0, 0, 0])
eye_5 = np.array([0, 0, 0])
eye_6 = np.array([0, 0, 0])

eye_weight = [eye_1, eye_2, eye_3, eye_4, eye_5, eye_6]
# print("\nMat: \n", eye_weight)


# tooth decay
tooth_2 = np.array([0, 0, 0])
tooth_3 = np.array([0, 0, 0, 0])
tooth_4 = np.array([0, 0, 0])
tooth_5 = np.array([0, 0, 0])

tooth_weight = [tooth_2, tooth_3, tooth_4, tooth_5]
# print("\nRang: \n", tooth_weight)


# hearing power
hearing_1 = np.array([0, 0, 0, 0])
hearing_2 = np.array([0, 0, 0, 0])
hearing_3 = np.array([0, 0, 0, 0])
hearing_4 = np.array([0, 0, 0, 0])
hearing_5 = np.array([0, 0, 0, 0])
hearing_6 = np.array([0, 0, 0, 0])

hearing_weight = [hearing_1, hearing_2,
                  hearing_3, hearing_4,
                  hearing_5, hearing_6]
# print("\nTai: \n", hearing_weight)


# max blood
blood_1 = np.array([0, 0, 0, 0])
blood_2 = np.array([0, 0, 0, 0])
blood_3 = np.array([0, 0, 0, 0])
blood_4 = np.array([0, 0, 0, 0])
blood_5 = np.array([0, 0, 0, 0])
blood_6 = np.array([0, 0, 0, 0])

blood_weight = np.array([blood_1, blood_2, 
                         blood_3, blood_4, 
                         blood_5, blood_6], dtype = object)
# print("\nMau: \n", blood_weight)


# size Fungal
fungal_2 = np.array([0, 0, 0, 0])
fungal_3 = np.array([0, 0, 0, 0])
fungal_4 = np.array([0, 0, 0, 0])

fungal_weight = np.array([fungal_2, fungal_3, fungal_4], dtype = object)
# print("\nDa: \n", fungal_weight)


# length Difference
length_4 = np.array([0, 0, 0, 0])
length_5 = np.array([0, 0, 0, 0])
length_6 = np.array([0, 0, 0, 0])

length_weight = np.array([length_4, length_5, length_6], dtype = object)
# print("\nChan tay: \n", length_weight)


# health index
health_1 = np.array([0, 0, 0, 0])
health_2 = np.array([0, 0, 0])
health_3 = np.array([0, 0, 0])
health_4 = np.array([0, 0, 0])
health_5 = np.array([0, 0, 0])
health_6 = np.array([0, 0, 0, 0])

health_weight = [health_1, health_2, 
                 health_3, health_4, 
                 health_5, health_6]
# print("\nChi so SK: \n", health_weight)

###########################################################################################################################
###########################################################################################################################

# BO TRONG SO
set_of_weights = [physical_weight, eye_weight, tooth_weight, hearing_weight, blood_weight, fungal_weight, length_weight, health_weight]




















#Nạp dữ liệu mẫu từ Excel
def nap_du_lieu_mau():
    list = pd.read_excel('../mysite/static/data/dulieumau.xlsx', index_col=0, skiprows=1)
    print(list)
    print("-------------------------------------------------------------------------\n\n")
    mylist = list.to_json()
    print(mylist)


    print("-------------------------------------------------------------------------\n\n")
    data = json.loads(mylist)

    count_row = len(data["The_luc"])
    print("count_row        : ", count_row)

    thuoc_tinh = []
    for key, value in data.items():
        data_thuoc_tinh = []
        for index in value:
            data_thuoc_tinh.append(value[index])
        thuoc_tinh.append(data_thuoc_tinh)


    count_column = len(thuoc_tinh)
    print("count_column     : ", count_column)
    print("-------------------------------------------------------------------------\n\n")

        
    sample_datasets = []
    for i in range(count_row):
        tmp = []
        for j in range(count_column):
            tmp.append(thuoc_tinh[j][i])
        sample_datasets.append(tmp)
        
    #Dữ liệu mẫu    
    print(sample_datasets) 
    
    return sample_datasets




def initialize_population(population, popmax):
    print("KHOI TAO GTDT....")
    for count in range(popmax):
        weights = []
        
        a = fuzz.random_physical_weight(physical_weight)
        b = fuzz.random_eye_weight(eye_weight)
        c = fuzz.random_tooth_weight(tooth_weight)
        d = fuzz.random_hearing_weight(hearing_weight)
        e = fuzz.random_blood_weight(blood_weight)
        f = fuzz.random_fungal_weight(fungal_weight)
        g = fuzz.random_length_weight(length_weight)
        h = fuzz.random_health_weight(health_weight)
        
        weights = [a, b, c, d, e, f, g, h]
        population.append(weights)
        print("+++++++++++++++++++++++++\n")
        
    return population



class Individual_eval:
    def __init__(self, individual, fitness_rate):
        self.individual = individual
        self.fitness_rate = fitness_rate



def calculate_fitness (population, sample_datasets):
    print("CACULATE FITNESS....")
    individuals_evaluated = []
    
    for individual in population:
        
        count = 0
        
        for sample_data in sample_datasets:
            output_fuzzy = fuzz.fuzzy(individual, sample_data)
            
            output_fuzzy_result = output_fuzzy['health_index']
            lower_limit_value = sample_data[7] - 1
            upper_limit_value = sample_data[7] + 1
            
            if (output_fuzzy_result >= lower_limit_value) and (output_fuzzy_result <= upper_limit_value):
                count = count + 1
        
        fitness_rate = count * 0.01
        individuals_evaluated.append(Individual_eval(individual, fitness_rate))
    
    return individuals_evaluated
        
    
def selection(individuals, count):
    print("SELECTION....")
        
    rank = sorted(individuals, key=lambda man: man.fitness_rate, reverse=True)
    
    ranked_selection = []
    
    # Lấy 'count' phần từ đầu tiên của tập rank
    for individual in rank:
        
        ranked_selection.append(individual.individual)
        
        count = count - 1
        if count == 0:
            break
    
    return ranked_selection
        
        

def crossover(father, mother):
    print("CROSSOVER....")
    midpoint = random.randrange(0, 7, 1)
    
    child = father
    
    for i in range(len(child)):
        if i > midpoint: 
            child[i] = mother[i]
            
    return child     
    
    

def multation(individual, index):
    print("MUTATION....")
    print("//////////////////////////: ", individual)
    if index == 0:
        individual[0] = fuzz.random_physical_weight(individual[0])
    elif index == 1:
        individual[1] = fuzz.random_eye_weight(individual[1])
    elif index == 2:
        individual[2] = fuzz.random_tooth_weight(individual[2])
    elif index == 3:
        individual[3] = fuzz.random_hearing_weight(individual[3])
    elif index == 4:
        individual[4] = fuzz.random_blood_weight(individual[4])
    elif index == 5:
        individual[5] = fuzz.random_fungal_weight(individual[5])
    elif index == 6:
        individual[6] = fuzz.random_length_weight(individual[6])
    else:
        individual[7] = fuzz.random_health_weight(individual[7])
    
    return  individual   


def review (population, sample_datasets):
    print("REVIEW....")
    individuals_evaluated = []
    
    for individual in population:
        
        count = 0
        
        for sample_data in sample_datasets:
            output_fuzzy = fuzz.fuzzy(individual, sample_data)
            
            output_fuzzy_result = output_fuzzy['health_index']
            lower_limit_value = sample_data[7] - 1
            upper_limit_value = sample_data[7] + 1
            
            if (output_fuzzy_result >= lower_limit_value) and (output_fuzzy_result <= upper_limit_value):
                count = count + 1
        
        fitness_rate = count * 0.01 # Chuyển thành các giá trị
        
        individuals_evaluated.append(Individual_eval(individual, fitness_rate))
        
        
    rank = sorted(individuals_evaluated, key=lambda individual: individual.fitness_rate, reverse=True)
    
    best_individual = {
        "individual": rank[0].individual,
        "fitness_rate": fitness_rate
    }
    
    return best_individual



































#################################################################
#################################################################

def genetic ():
    
    ## KHỞI TẠO
    population = []
    popmax = 3
    selectMax = 2
    multation_rate = 0.9
    termination_criteria = 0
    generations = 0
    
    # Tạo ra Quần thể gồm 200 cá thể:
    population = initialize_population(population, popmax)

    print("------------------------------------------")
    print("POPULATION: ", population)
    print("------------------------------------------")
    
    #################################################################
    #################################################################



    
    while(True):
        
        generations = generations + 1
        
        #Tính toán Fitness 
            # Input : Tập các BTS, bộ dữ liệu mẫu (Gồm N BTS)
            # Output: Tập các (BTS, Eval).
            # Fuzzy ở đây
        sample_data = nap_du_lieu_mau()
        individuals_evaluated = calculate_fitness(population, sample_data)

            
            
            
        #Lựa chọn các cá thể để Giao phối
            # Input : Tập các (BTS, Eval).
            # Output: Tập gồm n BTS có eval cao nhất (n = 20)    
        list_individuals_selected = selection (individuals_evaluated, selectMax)
            
            
            
            
        #Lai ghép chéo
            # Input : Tập các BTS đã được Lựa chọn.
            # Output: Tập các BTS đã được Lai ghép.
            # Solution: 
                # Lai ghép chéo các chỉ tiêu trong BTS luôn.
                # Tức là giữa A và B sẽ đổi nửa chỉ tiêu lai ghép cho nhau.
                
        for i in range(len(list_individuals_selected)):
            father_index = random.randrange(1, selectMax, 1)  
            mother_index = random.randrange(1, selectMax, 1)
            
            father = list_individuals_selected[father_index]
            mother = list_individuals_selected[mother_index]
            
            child = crossover(father, mother)
            
            list_individuals_selected[i] = child
            
                    
        
                
        #Đột biến
            # Input : Tập các BTS đã được Lai ghép.
            # Output: Tập các BTS đã được Đột biến.
            # Solution: 
                # Bước 1: Chọn random một Chỉ Tiêu để đột biến
                    # Đột biến như thế nào:
                        # Trong một Chỉ Tiêu sẽ có các Điểm
                        # Trong một Điểm lại có các phần tử Number của hàm thành viên.
                        # Sẽ đột biến các giá trị này bằng cách random giá trị trong giới hạn của chúng
                        
                # Bước 2: Duyệt qua các phần tử, phần tử nào có mutation_rate cao thì bị đột biến
                
        for i in range(len(list_individuals_selected)):
            if(random.random() > multation_rate):
                list_individuals_selected[i] = multation(list_individuals_selected[i], i)
        
        list_individuals_mutation = list_individuals_selected
        
        
        
        
        #Kiểm tra BTS
            # Input : Tập các BTS đã được Đột biến --OR-- Tập BTS khởi tạo ban đầu
            # Output: Object {
                        # result : int (1|0)    #(1 là đạt mục tiêu, 0 là không đạt mục tiêu)
                        # BTS    : BTS có tỉ lệ chính xác (correct_rate) đối với Bộ dữ liệu mẫu là cao nhất;
                        #}
            # Fuzzy ở đây
        best_individual = review (list_individuals_mutation, sample_data)
        
        
        # Nếu đạt chỉ tiêu => 
        if best_individual["fitness_rate"] >= termination_criteria:
            perfect_individual = best_individual["individual"]
            break
        else:
            for i in range(popmax):
                population[i] = best_individual["individual"]
    
    form = {
        "perfect_set_of_weights": perfect_individual,
        "generations" : generations
    }
    
    return form