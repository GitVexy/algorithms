def merge_sort(nums: list[int]):
    return merge(
        merge_sort(nums.copy()[:len(nums)//2]),
        merge_sort(nums.copy()[len(nums)//2:])
    ) if len(nums) >= 2 else nums

def merge(A, B):
    final = []
    i, j = 0, 0
    while i < len(A) and j < len(B):
        if A[i] <= B[j]:
            final.append(A[i])
            i += 1
        else:
            final.append(B[j])
            j += 1
        if i == len(A):
            while j < len(B):
                final.append(B[j])
                j += 1
        elif j == len(B):
            while i < len(A):
                final.append(A[i])
                i += 1
    return final

