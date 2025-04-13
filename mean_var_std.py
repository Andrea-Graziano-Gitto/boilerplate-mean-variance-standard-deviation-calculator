import numpy as np

def calculate(input_list):
    if len(input_list) != 9:
        raise ValueError("List must contain nine numbers.")

    mat = np.array([input_list[:3], input_list[3:6], input_list[6:9]])

    calculations = {
        "mean": [np.mean(mat, axis=0).tolist(), np.mean(mat, axis=1).tolist(), np.mean(mat).tolist()],
        "variance": [np.var(mat, axis=0).tolist(), np.var(mat, axis=1).tolist(), np.var(mat).tolist()],
        "standard deviation": [np.std(mat, axis=0).tolist(), np.std(mat, axis=1).tolist(), np.std(mat).tolist()],
        "min": [np.min(mat, axis=0).tolist(), np.min(mat, axis=1).tolist(), np.min(mat).tolist()],
        "max": [np.max(mat, axis=0).tolist(), np.max(mat, axis=1).tolist(), np.max(mat).tolist()],
        "sum": [np.sum(mat, axis=0).tolist(), np.sum(mat, axis=1).tolist(), np.sum(mat).tolist()]
    }

    return calculations
