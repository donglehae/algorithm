# [1차] 다트게임

def solution(dartResult):
  answer = ''
  temp = []
  for val in dartResult:
    if val.isdigit():
      answer += str(val)
    elif val.isalpha():
      if val == 'S':
        answer = int(answer) ** 1
      elif val == 'D':
        answer = int(answer) ** 2
      elif val == 'T':
        answer = int(answer) ** 3
      temp.append(answer)
      answer = ''
    else:
      if val == '*':
        if len(temp) > 1:
          temp[-1] = temp[-1] * 2
          temp[-2] = temp[-2] * 2
        else:
          temp[-1] = temp[-1] * 2
      if val == '#':
        temp[-1] = -temp[-1]
  answer = sum(temp)
  return answer

# 코드 리팩토링
# def solution(dartResult):
#   bonus = {'S': 1, 'D': 2, 'T': 3}
#   buffer = []
#   temp = ''
#   for val in dartResult:
#     if val.isdigit():
#       temp += str(val)
#     elif val.isalpha():
#       temp = int(temp) ** bonus[val]
#       buffer.append(temp)
#       temp = ''
#     else:
#       if val == '*':
#         buffer[-2:] = [x*2 for x in buffer[-2:]]
#       if val == '#':
#         buffer[-1] = -buffer[-1]
#   return sum(buffer)