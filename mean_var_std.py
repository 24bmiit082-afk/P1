import numpy as np

def calculate(input_list):
    """
    Calculate mean, variance, standard deviation, max, min, and sum of a 3x3 matrix.
    
    Args:
        input_list: A list containing 9 digits
        
    Returns:
        A dictionary with mean, variance, standard deviation, max, min, and sum
        along axis 0 (rows), axis 1 (columns), and flattened
        
    Raises:
        ValueError: If the list does not contain exactly 9 elements
    """
    # Validate input
    if len(input_list) != 9:
        raise ValueError("List must contain nine numbers.")
    
    # Convert list to 3x3 numpy array
    matrix = np.array(input_list).reshape(3, 3)
    
    # Calculate statistics
    result = {
        'mean': [np.mean(matrix, axis=0).tolist(), np.mean(matrix, axis=1).tolist(), float(np.mean(matrix))],
        'variance': [np.var(matrix, axis=0).tolist(), np.var(matrix, axis=1).tolist(), float(np.var(matrix))],
        'standard deviation': [np.std(matrix, axis=0).tolist(), np.std(matrix, axis=1).tolist(), float(np.std(matrix))],
        'max': [np.max(matrix, axis=0).tolist(), np.max(matrix, axis=1).tolist(), int(np.max(matrix))],
        'min': [np.min(matrix, axis=0).tolist(), np.min(matrix, axis=1).tolist(), int(np.min(matrix))],
        'sum': [np.sum(matrix, axis=0).tolist(), np.sum(matrix, axis=1).tolist(), int(np.sum(matrix))]
    }
    
    return result