# Binary Search Algorithm
# By Michael Morales

def binary_search(arr, target):
    """
    Performs a binary search on a sorted list to find the target element.
    
    Parameters:
        arr (list): A sorted list of elements.
        target (int or float): The element to search for in the list.

    Returns:
        int: The index of the target element in the list, or -1 if the element is not found.
    """
    left, right = 0, len(arr) - 1  # Set the initial search boundaries

    while left <= right:
        mid = (left + right) // 2  # Find the middle element
        
        # Check if the target is at the mid position
        if arr[mid] == target:
            return mid  # Target found, return its index
        
        # If the target is smaller than the middle element, search in the left half
        elif arr[mid] > target:
            right = mid - 1
        
        # If the target is larger than the middle element, search in the right half
        else:
            left = mid + 1
    
    return -1  # Target not found in the list

# Example usage:
if __name__ == "__main__":
    # Sorted list for binary search
    nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]

    # Test binary search for a number in the list
    target = 13
    result = binary_search(nums, target)

    if result != -1:
        print(f"Element {target} found at index {result}.")
    else:
        print(f"Element {target} not found in the list.")
