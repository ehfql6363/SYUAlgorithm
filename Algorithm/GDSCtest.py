# def solution(s):
#     answer = ''
#     num_dic = {'zero': '0', 'one': '1', 'two': '2', 'three': '3',
#                'four': '4', 'five': '5', 'six': '6', 'seven': '7',
#                'eight': '8', 'nine': '9'}
#
#     num_s = ''
#     for char in s:
#         if char.isdigit():
#             answer += char
#         else:
#             num_s += char
#             if num_s in num_dic:
#                 answer += num_dic[num_s]
#                 num_s = ''
#
#     return int(answer)
#print(solution("one4seveneight"))
n = {"zero": "0", "one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7",
     "eight": "8", "nine": "9"}


def solution(s):
    ans = s

    for k, v in n.items():
        ans = ans.replace(k, v)
    return int(ans)

print(solution("23four5six7"))

