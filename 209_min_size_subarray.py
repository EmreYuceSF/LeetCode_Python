def minSubArrayLen(target: int, nums: list[int]) -> int:
    """Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.
    Args:
        target (int): -
        nums (list[int]): random int list

    Returns:
        int: length of the smallest subarray!
    """

    left = 0  # will be index to track on the left end of the subarray
    right = 0  # will be index to track on the right end  of the subarray
    sumOfCurrentWindow = 0  # temp total of the selected subarray
    res = (
        10**9
    )  # res for result / start from max limit ( we are looking for the smallest one)

    for right in range(len(nums)):
        sumOfCurrentWindow += nums[right]

        while (
            sumOfCurrentWindow >= target
        ):  # while total is equal or greater then target
            res = min(
                res, right - left + 1
            )  # update the result with the smallest lenght of subarray
            sumOfCurrentWindow -= nums[
                left
            ]  # check if we remove from the beginning  of subarray if still ewual or greater then target
            left += 1

    return res if res != 10**9 else 0
