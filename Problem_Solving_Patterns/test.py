freq_counter_s = {}
freq_counter_t = {}
s = 'title'
t = 'paper'
yes = {(freq_counter_s[val] += 1 if val in freq_counter_s else freq_counter_s[val] = 1):  for val in s}
for val in s:
    if val in freq_counter_s:
        freq_counter_s[val] += 1
    else:
        freq_counter_s[val] = 1

for val in t:
    if val in freq_counter_t:
        freq_counter_t[val] += 1
    else:
        freq_counter_t[val] = 1
print(freq_counter_s)
print(freq_counter_t)

# # check if individual occurances is same
# # s_nums = []
# # for key in freq_counter_s:
# #     s_nums.append(freq_counter_s[key])

# # t_nums = []
# # for key in freq_counter_t:
# #     t_nums.append(freq_counter_t[key])

# # s_nums.sort()
# # t_nums.sort()
# # if s_nums == t_nums:
# #     return True
# # else:
# #     return False
# some_string = 'hello'
# result = map(some_string.count, some_string)
# print(list(result))

# some_dict = dict(zip(some_string, some_string))
# print(some_dict)

# nums = [1,2,3]
# result = map(lambda x: x * 2, nums)
# print(list(result))

# map(function, list) --> NEW LIST

# nums = [1,2,3]

# result = map(lambda val: val*2 , nums)

# print(list(result))