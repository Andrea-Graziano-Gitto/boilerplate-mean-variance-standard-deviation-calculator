import numpy as np

def calculate(list):
    calculations = {"mean": [], "variance": [], "standard deviation": [], "min": [], "max": [], "sum": []}
    error =  "List must contain nine numbers."
    try:
        a=list[9]
    except  ValueError:
        print(error)

    mat = np.array [[list[:3]],[list[3:6]],[list[6:9]]]
    
    calculations["mean"] = [np.mean(mat, axis=0).tolist(), np.mean(mat, axis=1).tolist(), np.mean(mat).tolist()]
    calculations["variance"] = [np.var(mat, axis=0).tolist(), np.var(mat, axis=1).tolist(), np.var(mat).tolist()]
    calculations["standard deviation"] = [np.std(mat, axis=0).tolist(), np.std(mat, axis=1).tolist(), np.std(mat).tolist()]
    calculations["min"] = [np.min(mat, axis=0).tolist(), np.min(mat, axis=1).tolist(), np.min(mat.flatten()).tolist()]
    calculations["max"] = [np.max(mat, axis=0).tolist(), np.max(mat, axis=1).tolist(), np.max(mat.flatten()).tolist()]
    calculations["sum"] = [np.sum(mat, axis=0).tolist(), np.sum(mat, axis=1).tolist(), np.sum(mat.flatten()).tolist()]
    



    return calculations