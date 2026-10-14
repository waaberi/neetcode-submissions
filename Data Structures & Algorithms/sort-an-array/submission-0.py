def merge(first: list[int], second: list[int]) -> list[int]:
    final: list[int] = []
    pf = 0
    ps = 0
    while pf < len(first) and ps < len(second):
        if first[pf] < second[ps]:
            final.append(first[pf])
            pf += 1
        else:
            final.append(second[ps])
            ps += 1

    while pf < len(first):
        final.append(first[pf])
        pf += 1

    while ps < len(second):
        final.append(second[ps])
        ps += 1

    return final

def sort(nums: list[int]):
    if len(nums) < 2:
        return nums
    first = nums[:len(nums)//2]
    second = nums[len(nums)//2:]
    return merge(sort(first), sort(second))


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return sort(nums)
        