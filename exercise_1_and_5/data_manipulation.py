from typing import List


def calculate_average(lst: List[int]) -> float: 
    """
        Calculates the avarage of list of integers.
        Returns 0 for empty lists and for None.

    Args:
        lst (List[int]): a list of integers

    Returns:
        float: simple average of the listed integers
    """
    
    if not lst:
        return 0
    
    total = sum(lst)
    
    average = total / len(lst)
    
    return average