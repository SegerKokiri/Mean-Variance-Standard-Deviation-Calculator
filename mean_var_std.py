import numpy as np

def calculate(list):
    if len(list) == 9:
        array_3x3 = np.array(list).reshape(3,3)
        
        oprations = {
            'mean': np.mean,
            'variance': np.var,
            'standard deviation': np.std,
            'max': np.max,
            'min': np.min,
            'sum': np.sum
        }
        calculations = {}
        
        for name, func in oprations.items():
            calculations[name] = [func(array_3x3, axis=0).tolist(), func(array_3x3, axis=1).tolist(), float(func(array_3x3))]
        
        return calculations
    else:
        raise ValueError('List must contain nine numbers.')





