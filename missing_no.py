nums = list(map(int, input("Enter no. (eg. 1 2 3 .....): ").split()))
seen = set()
i = 1
while i <= max(nums) + 1:
    if i not in seen:
        seen.add(i) if i in nums else None
    if i not in nums or (nums.count(i) == 0):
        pass
    i += 1
found = None
all_nums = set(nums)
check = 1
while check <= max(nums) + 1:
    if check not in all_nums:
        found = check
        break
    check += 1
if found is None:
    found = max(nums) + 1
print("Missing no. in the given no.:", found)
