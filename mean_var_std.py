import numpy as np

def calculate(list):
    
    #make sure list only has integers and that accepted nums only from 0-9
    digits = [x for x in list if (x==int(x)) and (x in range(0,10))]

    ##check list length 
    if len(digits) != 9:
        raise ValueError("List must contain nine numbers.") 
    
    #convert list to array
    num_array = np.array(digits, dtype=int)

    #convert array to 3x3 numpy array
    matrix = np.reshape(num_array,(3, 3))

    ##get summary stats (of both axes and flattened matrix) 
    #mean
    m1 = np.array(matrix.mean(axis=0)).tolist()
    m2 = np.array(matrix.mean(axis=1) ).tolist()
    m3 = np.array(matrix.mean()).tolist()
    #variance
    v1 = np.array(matrix.var(axis=0)).tolist()
    v2 = np.array(matrix.var(axis=1)).tolist()
    v3 = np.array(matrix.var()).tolist()
    #standard deviation
    std1 = np.array(matrix.std(axis=0)).tolist()
    std2 = np.array(matrix.std(axis=1)).tolist()
    std3 = np.array(matrix.std()).tolist()
    #maximum
    mx1 = np.array(matrix.max(axis=0)).tolist()
    mx2 = np.array(matrix.max(axis=1)).tolist()
    mx3 = np.array(matrix.max()).tolist()
    #minimum
    mn1 = np.array(matrix.min(axis=0)).tolist()
    mn2 = np.array(matrix.min(axis=1)).tolist()
    mn3 = np.array(matrix.min()).tolist()
    #sum
    s1 = np.array(matrix.sum(axis=0)).tolist()
    s2 = np.array(matrix.sum(axis=1)).tolist()
    s3 = np.array(matrix.sum()).tolist()

    #create list of values for dictionary
    mean_vals = [m1, m2, m3]
    var_vals = [v1, v2, v3]
    std_vals = [std1, std2, std3]
    max_vals = [mx1, mx2, mx3]
    min_vals = [mn1, mn2, mn3]
    sum_vals = [s1, s2, s3]


    ###return stat dictionary w/ value lists
    return {
            'mean': mean_vals,
            'variance': var_vals,
            'standard deviation': std_vals,
            'max': max_vals,
            'min': min_vals,
            'sum': sum_vals
            }

