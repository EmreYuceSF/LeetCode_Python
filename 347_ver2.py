from typing import List
import heapq as hp

def topKFrequent(nums: List[int], k: int) -> List[int]:
    """
    Finds the top k frequent elements in the given list of integers and returns them.

    Parameters:
        nums (List[int]): A list of integers.
        k (int): The number of top frequent elements to return.

    Returns:
        List[int]: A list containing the top k frequent elements from the input list.

    Algorithm:
        1. Create a dictionary 'mydict' to store the frequency count of each element.
        2. Initialize an empty list 'res' to store the result.
        3. Iterate through each element 'num' in the input 'nums' list.
        4. If 'num' is not in 'mydict', add it to 'mydict' with a frequency count of 1.
           Otherwise, increment its frequency count by 1.
        5. Use a min-heap to maintain the k most frequent elements.
        6. Iterate through the items of 'mydict'.
        7. Push the (frequency, element) pair into the min-heap.
        8. If the min-heap size exceeds k, pop the smallest element.
        9. After iterating through all items, the min-heap contains the k most frequent elements.
        10. Extract the elements from the min-heap and append them to the 'res' list.
        11. Return the 'res' list containing the top k frequent elements.

    Complexity Analysis:
        - Time Complexity: O(n + k log k), where 'n' is the number of elements in the 'nums' list.
          The initial loop to count the frequency takes O(n), and the heap operations take O(k log k).
        - Space Complexity: O(n + k), where 'n' is the number of elements in the 'nums' list.
          The space complexity is used to store the 'mydict' dictionary and the min-heap.
    """

    mydict = {}
    res = []

    for num in nums:
        if num not in mydict:
            mydict[num] = 1
        else:
            mydict[num] += 1
    mylist = list(mydict.items())
    klargest = hp.nlargest(k, mylist, key = lambda x: x[1])
    return ([largest[0] for largest in klargest])


print(topKFrequent([3,5,7,55,3,5,7,565,3,3,4,3,44,5,6,76,767,7,7,7,77,8,8,8], 6))            
