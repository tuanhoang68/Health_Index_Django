import random
import numpy as np
import skfuzzy as fuzz
import skfuzzy.membership as mf



# Các hàm khởi tạo bộ trọng số
def random_physical_weight(arr):
    print("CREATING_RANDOM_WEIGHT....")
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if j==0:
                arr[i][j] = random.randrange(14637, 15448, 1)
            else:
                tmp = random.randrange(14637, 15448, 1)
                if tmp < arr[i][j-1]:
                    while tmp < arr[i][j-1]:
                        tmp = random.randrange(14637, 15448, 1)
                        
                arr[i][j] = tmp
    return arr

def random_eye_weight(arr):
    print("CREATING_RANDOM_WEIGHT....")
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            # arr[i][j] = random.randrange(12, 19, 1)
            if j==0:
                arr[i][j] = random.randrange(12, 19, 1)
            else:
                tmp = random.randrange(12, 19, 1)
                if tmp < arr[i][j-1]:
                    while tmp < arr[i][j-1]:
                        tmp = random.randrange(12, 19, 1)
                        
                arr[i][j] = tmp
    return arr


def random_hearing_weight(arr):
    print("CREATING_RANDOM_WEIGHT....")
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            # arr[i][j] = random.randrange(3, 7, 1)
            if j==0:
                arr[i][j] = arr[i][j] = random.randrange(3, 7, 1)
            else:
                tmp = arr[i][j] = random.randrange(3, 7, 1)
                if tmp < arr[i][j-1]:
                    while tmp < arr[i][j-1]:
                        tmp = arr[i][j] = random.randrange(3, 7, 1)
                        
                arr[i][j] = tmp
    return arr


def random_tooth_weight(arr):
    print("CREATING_RANDOM_WEIGHT....")
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            # arr[i][j] = random.randrange(1, 10, 1)
            if j==0:
                arr[i][j] = random.randrange(1, 10, 1)
            else:
                tmp = random.randrange(1, 10, 1)
                if tmp < arr[i][j-1]:
                    while tmp < arr[i][j-1]:
                        tmp = random.randrange(1, 10, 1)
                        
                arr[i][j] = tmp
    return arr


def random_blood_weight(arr):
    print("CREATING_RANDOM_WEIGHT....")
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            # arr[i][j] = random.randrange(110, 160, 1)
            if j==0:
                arr[i][j] = random.randrange(110, 160, 1)
            else:
                tmp = random.randrange(110, 160, 1)
                if tmp < arr[i][j-1]:
                    while tmp < arr[i][j-1]:
                        tmp = random.randrange(110, 160, 1)
                        
                arr[i][j] = tmp
    return arr


def random_fungal_weight(arr):
    print("CREATING_RANDOM_WEIGHT....")
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            # arr[i][j] = random.randrange(50, 100, 1)
            if j==0:
                arr[i][j] = random.randrange(50, 100, 1)
            else:
                tmp = random.randrange(50, 100, 1)
                if tmp < arr[i][j-1]:
                    while tmp < arr[i][j-1]:
                        tmp = random.randrange(50, 100, 1)
                        
                arr[i][j] = tmp
    return arr

def random_length_weight(arr):
    print("CREATING_RANDOM_WEIGHT....")
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            # arr[i][j] = random.randrange(2, 5, 1)
            if j==0:
                arr[i][j] = random.randrange(2, 5, 1)
            else:
                tmp = random.randrange(2, 5, 1)
                if tmp < arr[i][j-1]:
                    while tmp < arr[i][j-1]:
                        tmp = random.randrange(2, 5, 1)
                        
                arr[i][j] = tmp
    return arr


def random_health_weight(arr):
    print("CREATING_RANDOM_WEIGHT....")
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            # arr[i][j] = random.randrange(4, 42, 1)
            if j==0:
                arr[i][j] = random.randrange(4, 42, 1)
            else:
                tmp = random.randrange(4, 42, 1)
                if tmp < arr[i][j-1]:
                    while tmp < arr[i][j-1]:
                        tmp = random.randrange(4, 42, 1)
                        
                arr[i][j] = tmp
    return arr











def fuzzy(set_of_weights, sample_data): 
    
    x_physical = np.arange(0, 20000, 1) # Khoảng hơi rộng???
    x_eye_Sight = np.arange(0, 25, 1)
    x_tooth_Decay = np.arange(0, 8, 1)
    x_hearing = np.arange(0, 11, 1)
    x_max_Blood_Pressure = np.arange(100, 161, 1)
    x_size_Fungal_Skin = np.arange(1, 101, 1)
    x_length_Difference = np.arange(1, 10, 1)
    
    y_health_Index = np.arange(6, 43, 1)
    
    #Khởi tạo đầu vào
    input_physical              = sample_data[0]
    input_eye_Sight             = sample_data[1]
    input_tooth_Decay           = sample_data[2]
    input_hearing               = sample_data[3]
    input_max_Blood_Pressure    = sample_data[4]
    input_size_Fungal_Skin      = sample_data[5]
    input_length_Difference     = sample_data[6]
    
    
    

    
    physical_point1_num1 = set_of_weights[0][0][0]
    physical_point1_num2 = set_of_weights[0][0][1]
    physical_point1_num3 = set_of_weights[0][0][2]
    physical_point1_num4 = set_of_weights[0][0][3]

    physical_point2_num1 = set_of_weights[0][1][0]
    physical_point2_num2 = set_of_weights[0][1][1]
    physical_point2_num3 = set_of_weights[0][1][2]
    physical_point2_num4 = set_of_weights[0][1][3]

    physical_point3_num1 = set_of_weights[0][2][0]
    physical_point3_num2 = set_of_weights[0][2][1]
    physical_point3_num3 = set_of_weights[0][2][2]
    physical_point3_num4 = set_of_weights[0][2][3]

    physical_point4_num1 = set_of_weights[0][3][0]
    physical_point4_num2 = set_of_weights[0][3][1]
    physical_point4_num3 = set_of_weights[0][3][2]
    physical_point4_num4 = set_of_weights[0][3][3]

    physical_point5_num1 = set_of_weights[0][4][0]
    physical_point5_num2 = set_of_weights[0][4][1]
    physical_point5_num3 = set_of_weights[0][4][2]
    physical_point5_num4 = set_of_weights[0][4][3]

    physical_point6_num1 = set_of_weights[0][5][0]
    physical_point6_num2 = set_of_weights[0][5][1]
    physical_point6_num3 = set_of_weights[0][5][2]
    physical_point6_num4 = set_of_weights[0][5][3]


    #BTS cua Eye Sight - Trimp
    eyeSight_point1_num1 = set_of_weights[1][0][0]
    eyeSight_point1_num2 = set_of_weights[1][0][1]
    eyeSight_point1_num3 = set_of_weights[1][0][2]

    eyeSight_point2_num1 = set_of_weights[1][1][0]
    eyeSight_point2_num2 = set_of_weights[1][1][1]
    eyeSight_point2_num3 = set_of_weights[1][1][2]

    eyeSight_point3_num1 = set_of_weights[1][2][0]
    eyeSight_point3_num2 = set_of_weights[1][2][1]
    eyeSight_point3_num3 = set_of_weights[1][2][2]

    eyeSight_point4_num1 = set_of_weights[1][3][0]
    eyeSight_point4_num2 = set_of_weights[1][3][1]
    eyeSight_point4_num3 = set_of_weights[1][3][2]

    eyeSight_point5_num1 = set_of_weights[1][4][0]
    eyeSight_point5_num2 = set_of_weights[1][4][1]
    eyeSight_point5_num3 = set_of_weights[1][4][2]

    eyeSight_point6_num1 = set_of_weights[1][5][0]
    eyeSight_point6_num2 = set_of_weights[1][5][1]
    eyeSight_point6_num3 = set_of_weights[1][5][2]


    #BTS cua Moderate Tooth Decay - Trimp & Trap
    toothDecay_point2_num1 = set_of_weights[2][0][0]
    toothDecay_point2_num2 = set_of_weights[2][0][1]
    toothDecay_point2_num3 = set_of_weights[2][0][2]

    toothDecay_point3_num1 = set_of_weights[2][1][0]
    toothDecay_point3_num2 = set_of_weights[2][1][1]
    toothDecay_point3_num3 = set_of_weights[2][1][2]
    toothDecay_point3_num4 = set_of_weights[2][1][3]

    toothDecay_point4_num1 = set_of_weights[2][2][0]
    toothDecay_point4_num2 = set_of_weights[2][2][1]
    toothDecay_point4_num3 = set_of_weights[2][2][2]

    toothDecay_point5_num1 = set_of_weights[2][3][0]
    toothDecay_point5_num2 = set_of_weights[2][3][1]
    toothDecay_point5_num3 = set_of_weights[2][3][2]


    #BTS cua Hearing Power - Tramp
    hearingPower_point1_num1 = set_of_weights[3][0][0]
    hearingPower_point1_num2 = set_of_weights[3][0][1]
    hearingPower_point1_num3 = set_of_weights[3][0][2]
    hearingPower_point1_num4 = set_of_weights[3][0][3]

    hearingPower_point2_num1 = set_of_weights[3][1][0]
    hearingPower_point2_num2 = set_of_weights[3][1][1]
    hearingPower_point2_num3 = set_of_weights[3][1][2]
    hearingPower_point2_num4 = set_of_weights[3][1][3]

    hearingPower_point3_num1 = set_of_weights[3][2][0]
    hearingPower_point3_num2 = set_of_weights[3][2][1]
    hearingPower_point3_num3 = set_of_weights[3][2][2]
    hearingPower_point3_num4 = set_of_weights[3][2][3]

    hearingPower_point4_num1 = set_of_weights[3][3][0]
    hearingPower_point4_num2 = set_of_weights[3][3][1]
    hearingPower_point4_num3 = set_of_weights[3][3][2]
    hearingPower_point4_num4 = set_of_weights[3][3][3]

    hearingPower_point5_num1 = set_of_weights[3][4][0]
    hearingPower_point5_num2 = set_of_weights[3][4][1]
    hearingPower_point5_num3 = set_of_weights[3][4][2]
    hearingPower_point5_num4 = set_of_weights[3][4][3]

    hearingPower_point6_num1 = set_of_weights[3][5][0]
    hearingPower_point6_num2 = set_of_weights[3][5][1]
    hearingPower_point6_num3 = set_of_weights[3][5][2]
    hearingPower_point6_num4 = set_of_weights[3][5][3]


    #BTS cua Max Blood Pressure - Tramp
    maxBlood_point1_num1 = set_of_weights[4][0][0]
    maxBlood_point1_num2 = set_of_weights[4][0][1]
    maxBlood_point1_num3 = set_of_weights[4][0][2]
    maxBlood_point1_num4 = set_of_weights[4][0][3]

    maxBlood_point2_num1 = set_of_weights[4][1][0]
    maxBlood_point2_num2 = set_of_weights[4][1][1]
    maxBlood_point2_num3 = set_of_weights[4][1][2]
    maxBlood_point2_num4 = set_of_weights[4][1][3]

    maxBlood_point3_num1 = set_of_weights[4][2][0]
    maxBlood_point3_num2 = set_of_weights[4][2][1]
    maxBlood_point3_num3 = set_of_weights[4][2][2]
    maxBlood_point3_num4 = set_of_weights[4][2][3]

    maxBlood_point4_num1 = set_of_weights[4][3][0]
    maxBlood_point4_num2 = set_of_weights[4][3][1]
    maxBlood_point4_num3 = set_of_weights[4][3][2]
    maxBlood_point4_num4 = set_of_weights[4][3][3]

    maxBlood_point5_num1 = set_of_weights[4][4][0]
    maxBlood_point5_num2 = set_of_weights[4][4][1]
    maxBlood_point5_num3 = set_of_weights[4][4][2]
    maxBlood_point5_num4 = set_of_weights[4][4][3]

    maxBlood_point6_num1 = set_of_weights[4][5][0]
    maxBlood_point6_num2 = set_of_weights[4][5][1]
    maxBlood_point6_num3 = set_of_weights[4][5][2]
    maxBlood_point6_num4 = set_of_weights[4][5][3]


    #BTS cua Size of the Fungal Skin Area - Tramp
    sizeFungal_point2_num1 = set_of_weights[5][0][0]
    sizeFungal_point2_num2 = set_of_weights[5][0][1]
    sizeFungal_point2_num3 = set_of_weights[5][0][2]
    sizeFungal_point2_num4 = set_of_weights[5][0][3]

    sizeFungal_point3_num1 = set_of_weights[5][1][0]
    sizeFungal_point3_num2 = set_of_weights[5][1][1]
    sizeFungal_point3_num3 = set_of_weights[5][1][2]
    sizeFungal_point3_num4 = set_of_weights[5][1][3]

    sizeFungal_point4_num1 = set_of_weights[5][2][0]
    sizeFungal_point4_num2 = set_of_weights[5][2][1]
    sizeFungal_point4_num3 = set_of_weights[5][2][2]
    sizeFungal_point4_num4 = set_of_weights[5][2][3]



    #BTS cua Amount of Length Difference - Tramp
    lenghtDifference_point4_num1 =  set_of_weights[6][0][0]    
    lenghtDifference_point4_num2 =  set_of_weights[6][0][1]
    lenghtDifference_point4_num3 =  set_of_weights[6][0][2]
    lenghtDifference_point4_num4 =  set_of_weights[6][0][3]

    lenghtDifference_point5_num1 =  set_of_weights[6][1][0]    
    lenghtDifference_point5_num2 =  set_of_weights[6][1][1]
    lenghtDifference_point5_num3 =  set_of_weights[6][1][2]
    lenghtDifference_point5_num4 =  set_of_weights[6][1][3]

    lenghtDifference_point6_num1 =  set_of_weights[6][2][0]    
    lenghtDifference_point6_num2 =  set_of_weights[6][2][1]
    lenghtDifference_point6_num3 =  set_of_weights[6][2][2]
    lenghtDifference_point6_num4 =  set_of_weights[6][2][3]


    #BTS cua Health Index - Tramp
    healthIndex_point1_num1 = set_of_weights[7][0][0]   
    healthIndex_point1_num2 = set_of_weights[7][0][1]   
    healthIndex_point1_num3 = set_of_weights[7][0][2]   
    healthIndex_point1_num4 = set_of_weights[7][0][3]   


    healthIndex_point2_num1 = set_of_weights[7][1][0]       
    healthIndex_point2_num2 = set_of_weights[7][1][1]   
    healthIndex_point2_num3 = set_of_weights[7][1][2]   

    healthIndex_point3_num1 = set_of_weights[7][2][0]       
    healthIndex_point3_num2 = set_of_weights[7][2][1]   
    healthIndex_point3_num3 = set_of_weights[7][2][2]   

    healthIndex_point4_num1 = set_of_weights[7][3][0]       
    healthIndex_point4_num2 = set_of_weights[7][3][1]   
    healthIndex_point4_num3 = set_of_weights[7][3][2]   

    healthIndex_point5_num1 = set_of_weights[7][4][0]       
    healthIndex_point5_num2 = set_of_weights[7][4][1]   
    healthIndex_point5_num3 = set_of_weights[7][4][2]   

    healthIndex_point6_num1 = set_of_weights[7][5][0]       
    healthIndex_point6_num2 = set_of_weights[7][5][1]   
    healthIndex_point6_num3 = set_of_weights[7][5][2]   
    healthIndex_point6_num4 = set_of_weights[7][5][3]  






    ###########################################################################################################################
    ###########################################################################################################################

    #Khoi tao ham thanh vien
    physical_point1 = mf.trapmf(x_physical, [physical_point1_num1, physical_point1_num2, physical_point1_num3, physical_point1_num4])
    physical_point2 = mf.trapmf(x_physical, [physical_point2_num1, physical_point2_num2, physical_point2_num3, physical_point2_num4])
    physical_point3 = mf.trapmf(x_physical, [physical_point3_num1, physical_point3_num2, physical_point3_num3, physical_point3_num4])
    physical_point4 = mf.trapmf(x_physical, [physical_point4_num1, physical_point4_num2, physical_point4_num3, physical_point4_num4])
    physical_point5 = mf.trapmf(x_physical, [physical_point5_num1, physical_point5_num2, physical_point5_num3, physical_point5_num4])
    physical_point6 = mf.trapmf(x_physical, [physical_point6_num1, physical_point6_num2, physical_point6_num3, physical_point6_num4])

    eyeSight_point1 = mf.trimf(x_eye_Sight, [eyeSight_point1_num1, eyeSight_point1_num2, eyeSight_point1_num3])
    eyeSight_point2 = mf.trimf(x_eye_Sight, [eyeSight_point2_num1, eyeSight_point2_num2, eyeSight_point2_num3])
    eyeSight_point3 = mf.trimf(x_eye_Sight, [eyeSight_point3_num1, eyeSight_point3_num2, eyeSight_point3_num3])
    eyeSight_point4 = mf.trimf(x_eye_Sight, [eyeSight_point4_num1, eyeSight_point4_num2, eyeSight_point4_num3])
    eyeSight_point5 = mf.trimf(x_eye_Sight, [eyeSight_point5_num1, eyeSight_point5_num2, eyeSight_point5_num3])
    eyeSight_point6 = mf.trimf(x_eye_Sight, [eyeSight_point6_num1, eyeSight_point6_num2, eyeSight_point6_num3])

    toothDecay_point2 = mf.trimf(x_tooth_Decay, [toothDecay_point2_num1, toothDecay_point2_num2, toothDecay_point2_num3])
    toothDecay_point3 = mf.trapmf(x_tooth_Decay, [toothDecay_point3_num1, toothDecay_point3_num2, toothDecay_point3_num3, toothDecay_point3_num4])
    toothDecay_point4 = mf.trimf(x_tooth_Decay, [toothDecay_point4_num1, toothDecay_point4_num2, toothDecay_point4_num3])
    toothDecay_point5 = mf.trimf(x_tooth_Decay, [toothDecay_point5_num1, toothDecay_point5_num2, toothDecay_point5_num3])

    hearingPower_point1 = mf.trapmf(x_hearing, [hearingPower_point1_num1, hearingPower_point1_num2, hearingPower_point1_num3, hearingPower_point1_num4])
    hearingPower_point2 = mf.trapmf(x_hearing, [hearingPower_point2_num1, hearingPower_point2_num2, hearingPower_point2_num3, hearingPower_point2_num4])
    hearingPower_point3 = mf.trapmf(x_hearing, [hearingPower_point3_num1, hearingPower_point3_num2, hearingPower_point3_num3, hearingPower_point3_num4])
    hearingPower_point4 = mf.trapmf(x_hearing, [hearingPower_point4_num1, hearingPower_point4_num2, hearingPower_point4_num3, hearingPower_point4_num4])
    hearingPower_point5 = mf.trapmf(x_hearing, [hearingPower_point5_num1, hearingPower_point5_num2, hearingPower_point5_num3, hearingPower_point5_num4])
    hearingPower_point6 = mf.trapmf(x_hearing, [hearingPower_point6_num1, hearingPower_point6_num2, hearingPower_point6_num3, hearingPower_point6_num4])

    maxBlood_point1 = mf.trapmf(x_max_Blood_Pressure, [maxBlood_point1_num1, maxBlood_point1_num2, maxBlood_point1_num3, maxBlood_point1_num4])
    maxBlood_point2 = mf.trapmf(x_max_Blood_Pressure, [maxBlood_point2_num1, maxBlood_point2_num2, maxBlood_point2_num3, maxBlood_point2_num4])
    maxBlood_point3 = mf.trapmf(x_max_Blood_Pressure, [maxBlood_point3_num1, maxBlood_point3_num2, maxBlood_point3_num3, maxBlood_point3_num4])
    maxBlood_point4 = mf.trapmf(x_max_Blood_Pressure, [maxBlood_point4_num1, maxBlood_point4_num2, maxBlood_point4_num3, maxBlood_point4_num4])
    maxBlood_point5 = mf.trapmf(x_max_Blood_Pressure, [maxBlood_point5_num1, maxBlood_point5_num2, maxBlood_point5_num3, maxBlood_point5_num4])
    maxBlood_point6 = mf.trapmf(x_max_Blood_Pressure, [maxBlood_point6_num1, maxBlood_point6_num2, maxBlood_point6_num3, maxBlood_point6_num4])

    sizeFungal_point2 = mf.trapmf(x_size_Fungal_Skin, [sizeFungal_point2_num1, sizeFungal_point2_num2, sizeFungal_point2_num3, sizeFungal_point2_num4])
    sizeFungal_point3 = mf.trapmf(x_size_Fungal_Skin, [sizeFungal_point3_num1, sizeFungal_point3_num2, sizeFungal_point3_num3, sizeFungal_point3_num4])
    sizeFungal_point4 = mf.trapmf(x_size_Fungal_Skin, [sizeFungal_point4_num1, sizeFungal_point4_num2, sizeFungal_point4_num3, sizeFungal_point4_num4])

    lenghtDifference_point4 = mf.trapmf(x_length_Difference, [lenghtDifference_point4_num1, lenghtDifference_point4_num2, lenghtDifference_point4_num3, lenghtDifference_point4_num4])
    lenghtDifference_point5 = mf.trapmf(x_length_Difference, [lenghtDifference_point5_num1, lenghtDifference_point5_num2, lenghtDifference_point5_num3, lenghtDifference_point5_num4])
    lenghtDifference_point6 = mf.trapmf(x_length_Difference, [lenghtDifference_point6_num1, lenghtDifference_point6_num2, lenghtDifference_point6_num3, lenghtDifference_point6_num4])


    healthIndex_point1 = mf.trapmf(y_health_Index, [healthIndex_point1_num1, healthIndex_point1_num2, healthIndex_point1_num3, healthIndex_point1_num4])
    healthIndex_point2 = mf.trimf(y_health_Index, [healthIndex_point2_num1, healthIndex_point2_num2, healthIndex_point2_num3])
    healthIndex_point3 = mf.trimf(y_health_Index, [healthIndex_point3_num1, healthIndex_point3_num2, healthIndex_point3_num3])
    healthIndex_point4 = mf.trimf(y_health_Index, [healthIndex_point4_num1, healthIndex_point4_num2, healthIndex_point4_num3])
    healthIndex_point5 = mf.trimf(y_health_Index, [healthIndex_point5_num1, healthIndex_point5_num2, healthIndex_point5_num3])
    healthIndex_point6 = mf.trapmf(y_health_Index, [healthIndex_point6_num1, healthIndex_point6_num2, healthIndex_point6_num3, healthIndex_point6_num4])







    ###########################################################################################################################
    ###########################################################################################################################

    # MO HOA
    print("MO HOA....")
    
    physical_fit_point1 = fuzz.interp_membership(x_physical, physical_point1, input_physical)
    physical_fit_point2 = fuzz.interp_membership(x_physical, physical_point2, input_physical)
    physical_fit_point3 = fuzz.interp_membership(x_physical, physical_point3, input_physical)
    physical_fit_point4 = fuzz.interp_membership(x_physical, physical_point4, input_physical)
    physical_fit_point5 = fuzz.interp_membership(x_physical, physical_point5, input_physical)
    physical_fit_point6 = fuzz.interp_membership(x_physical, physical_point6, input_physical)

    eyeSight_fit_point1 = fuzz.interp_membership(x_eye_Sight, eyeSight_point1, input_eye_Sight)
    eyeSight_fit_point2 = fuzz.interp_membership(x_eye_Sight, eyeSight_point2, input_eye_Sight)
    eyeSight_fit_point3 = fuzz.interp_membership(x_eye_Sight, eyeSight_point3, input_eye_Sight)
    eyeSight_fit_point4 = fuzz.interp_membership(x_eye_Sight, eyeSight_point4, input_eye_Sight)
    eyeSight_fit_point5 = fuzz.interp_membership(x_eye_Sight, eyeSight_point5, input_eye_Sight)
    eyeSight_fit_point6 = fuzz.interp_membership(x_eye_Sight, eyeSight_point6, input_eye_Sight)

    toothDecay_fit_point2 = fuzz.interp_membership(x_tooth_Decay, toothDecay_point2, input_tooth_Decay)
    toothDecay_fit_point3 = fuzz.interp_membership(x_tooth_Decay, toothDecay_point3, input_tooth_Decay)
    toothDecay_fit_point4 = fuzz.interp_membership(x_tooth_Decay, toothDecay_point4, input_tooth_Decay)
    toothDecay_fit_point5 = fuzz.interp_membership(x_tooth_Decay, toothDecay_point5, input_tooth_Decay)

    hearingPower_fit_point1 = fuzz.interp_membership(x_hearing, hearingPower_point1, input_hearing)
    hearingPower_fit_point2 = fuzz.interp_membership(x_hearing, hearingPower_point2, input_hearing)
    hearingPower_fit_point3 = fuzz.interp_membership(x_hearing, hearingPower_point3, input_hearing)
    hearingPower_fit_point4 = fuzz.interp_membership(x_hearing, hearingPower_point4, input_hearing)
    hearingPower_fit_point5 = fuzz.interp_membership(x_hearing, hearingPower_point5, input_hearing)
    hearingPower_fit_point6 = fuzz.interp_membership(x_hearing, hearingPower_point6, input_hearing)

    maxBlood_fit_point1 = fuzz.interp_membership(x_max_Blood_Pressure, maxBlood_point1, input_max_Blood_Pressure)
    maxBlood_fit_point2 = fuzz.interp_membership(x_max_Blood_Pressure, maxBlood_point2, input_max_Blood_Pressure)
    maxBlood_fit_point3 = fuzz.interp_membership(x_max_Blood_Pressure, maxBlood_point3, input_max_Blood_Pressure)
    maxBlood_fit_point4 = fuzz.interp_membership(x_max_Blood_Pressure, maxBlood_point4, input_max_Blood_Pressure)
    maxBlood_fit_point5 = fuzz.interp_membership(x_max_Blood_Pressure, maxBlood_point5, input_max_Blood_Pressure)
    maxBlood_fit_point6 = fuzz.interp_membership(x_max_Blood_Pressure, maxBlood_point6, input_max_Blood_Pressure)

    sizeFungal_fit_point2 = fuzz.interp_membership(x_size_Fungal_Skin, sizeFungal_point2, input_size_Fungal_Skin)
    sizeFungal_fit_point3 = fuzz.interp_membership(x_size_Fungal_Skin, sizeFungal_point3, input_size_Fungal_Skin)
    sizeFungal_fit_point4 = fuzz.interp_membership(x_size_Fungal_Skin, sizeFungal_point4, input_size_Fungal_Skin)

    lenghtDifference_fit_point4 = fuzz.interp_membership(x_length_Difference, lenghtDifference_point4, input_length_Difference)
    lenghtDifference_fit_point5 = fuzz.interp_membership(x_length_Difference, lenghtDifference_point5, input_length_Difference)
    lenghtDifference_fit_point6 = fuzz.interp_membership(x_length_Difference, lenghtDifference_point6, input_length_Difference)






    ###########################################################################################################################
    ###########################################################################################################################

    # RULE BASE
    rule1 = np.fmin(np.fmin(np.fmin(np.fmin(physical_fit_point1, eyeSight_fit_point1), hearingPower_fit_point1), maxBlood_fit_point1), healthIndex_point1)
    rule2 = np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(physical_fit_point2, eyeSight_fit_point2), toothDecay_fit_point2), hearingPower_fit_point2), maxBlood_fit_point2), sizeFungal_fit_point2), healthIndex_point2)
    rule3 = np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(physical_fit_point1, eyeSight_fit_point2), hearingPower_fit_point1), maxBlood_fit_point1), sizeFungal_fit_point2), healthIndex_point2)
    rule4 = np.fmin(np.fmin(np.fmin(np.fmin(physical_fit_point2 ,eyeSight_fit_point1),hearingPower_fit_point1), maxBlood_fit_point1), healthIndex_point2)
    rule5 = np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(physical_fit_point3 ,eyeSight_fit_point3),toothDecay_fit_point3), hearingPower_fit_point3), maxBlood_fit_point3), sizeFungal_fit_point3), healthIndex_point3)

    rule6 = np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(physical_fit_point1 ,eyeSight_fit_point1), toothDecay_fit_point2),hearingPower_fit_point1), maxBlood_fit_point1), sizeFungal_fit_point3), healthIndex_point3)
    rule7 = np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(physical_fit_point2 ,eyeSight_fit_point3),hearingPower_fit_point2), maxBlood_fit_point2), sizeFungal_fit_point2), healthIndex_point3)
    rule8 = np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(physical_fit_point4 ,eyeSight_fit_point4), toothDecay_fit_point4),hearingPower_fit_point4), maxBlood_fit_point4), sizeFungal_fit_point4), lenghtDifference_fit_point4), healthIndex_point4)
    rule9 = np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(physical_fit_point1 ,eyeSight_fit_point1),hearingPower_fit_point1), maxBlood_fit_point1), sizeFungal_fit_point2), lenghtDifference_fit_point4), healthIndex_point4)
    rule10 = np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(physical_fit_point3 ,eyeSight_fit_point2),hearingPower_fit_point3), maxBlood_fit_point3), sizeFungal_fit_point3), lenghtDifference_fit_point4), healthIndex_point4)

    rule11 = np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(physical_fit_point2 ,eyeSight_fit_point3), toothDecay_fit_point4), hearingPower_fit_point2), maxBlood_fit_point4), healthIndex_point4)
    rule12 = np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(physical_fit_point5, eyeSight_fit_point5), toothDecay_fit_point5), hearingPower_fit_point5), maxBlood_fit_point5), lenghtDifference_fit_point5), healthIndex_point5)
    rule13 = np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(physical_fit_point4, eyeSight_fit_point1),toothDecay_fit_point5), hearingPower_fit_point4), maxBlood_fit_point1), sizeFungal_fit_point2), lenghtDifference_fit_point5), healthIndex_point5)
    rule14 = np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(physical_fit_point1, eyeSight_fit_point2),toothDecay_fit_point2), hearingPower_fit_point1), maxBlood_fit_point2), lenghtDifference_fit_point5), healthIndex_point5)
    rule15 = np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(physical_fit_point1, eyeSight_fit_point1), hearingPower_fit_point1), maxBlood_fit_point1), sizeFungal_fit_point2), lenghtDifference_fit_point5), healthIndex_point5)

    rule16 = np.fmin(np.fmin(np.fmin(np.fmin(physical_fit_point3, eyeSight_fit_point4), hearingPower_fit_point3), maxBlood_fit_point5), healthIndex_point5)
    rule17 = np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(physical_fit_point6, eyeSight_fit_point6), hearingPower_fit_point6), maxBlood_fit_point6), lenghtDifference_fit_point6), healthIndex_point6)
    rule18 = np.fmin(np.fmin(np.fmin(np.fmin(physical_fit_point6, eyeSight_fit_point1), hearingPower_fit_point1), maxBlood_fit_point1), healthIndex_point6)
    rule19 = np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(physical_fit_point2, eyeSight_fit_point3),toothDecay_fit_point4), hearingPower_fit_point5), maxBlood_fit_point3), sizeFungal_fit_point4), lenghtDifference_fit_point6), healthIndex_point6)






    ###########################################################################################################################
    ###########################################################################################################################

    # SUY DIỄN - Kết hợp các luật - sử dụng OR (Chọn cái lớn hơn)
    out_healthIndex_point1 = rule1
    out_healthIndex_point2 = np.fmax(np.fmax(rule2,rule3),rule4)
    out_healthIndex_point3 = np.fmax(np.fmax(rule5,rule6),rule7)
    out_healthIndex_point4 = np.fmax(np.fmax(np.fmax(rule8,rule9),rule10),rule11)
    out_healthIndex_point5 = np.fmax(np.fmax(np.fmax(np.fmax(rule12,rule13),rule14),rule15),rule16)
    out_healthIndex_point6 = np.fmax(np.fmax(rule17,rule18),rule19)





    ###########################################################################################################################
    ###########################################################################################################################

    #GIAI MO
    out_healthIndex = np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(out_healthIndex_point1, out_healthIndex_point2), out_healthIndex_point3), out_healthIndex_point4), out_healthIndex_point5), out_healthIndex_point6)

    # Giải mờ theo phương pháp 
    defuzzified  = fuzz.defuzz(y_health_Index, out_healthIndex, 'lom')

    result = fuzz.interp_membership(y_health_Index, out_healthIndex, defuzzified)

    # print("Chi so suc khoe:", defuzzified)
    print("GIAI MO....")
    
    # y_health_Index = np.arange(6, 43, 1)
    
    y_health_Index_point1 = fuzz.interp_membership(y_health_Index, out_healthIndex_point1, defuzzified)
    y_health_Index_point2 = fuzz.interp_membership(y_health_Index, out_healthIndex_point2, defuzzified)
    y_health_Index_point3 = fuzz.interp_membership(y_health_Index, out_healthIndex_point3, defuzzified)
    y_health_Index_point4 = fuzz.interp_membership(y_health_Index, out_healthIndex_point4, defuzzified)
    y_health_Index_point5 = fuzz.interp_membership(y_health_Index, out_healthIndex_point5, defuzzified)
    y_health_Index_point6 = fuzz.interp_membership(y_health_Index, out_healthIndex_point6, defuzzified)
    
    
    y_health_Index = [y_health_Index_point1, 
                      y_health_Index_point2, 
                      y_health_Index_point3, 
                      y_health_Index_point4, 
                      y_health_Index_point5, 
                      y_health_Index_point6]
    
    
    
    data = {
        "health_index"      : result,
        "y_health_Index"    : y_health_Index
    }
    
    return data





