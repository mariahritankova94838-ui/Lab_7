def find_min_max(nums, left, right):
    # Базовый случай 1: один элемент в подмассиве
    if left == right:
        return nums[left], nums[left]

    if right == left + 1:
        if nums[left] < nums[right]:
            return nums[left], nums[right]
        else:
            return nums[right], nums[left]

    mid = (left + right) // 2

    left_min, left_max = find_min_max(nums, left, mid)
    right_min, right_max = find_min_max(nums, mid + 1, right)

    final_min = left_min if left_min < right_min else right_min
    final_max = left_max if left_max > right_max else right_max

    return final_min, final_max

    array = [5, 7, 2, 4, 9, 6]
    minimum, maximum = find_min_max(array, 0, len(array) - 1)
    print(f"min: {minimum}, max: {maximum}")