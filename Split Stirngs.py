def solution(s):
    s = list(s)
    if ((len(s)) % 2) == 1:
        s.append('_')
    result = [s[idx:idx+2] for idx in range(0, len(s), 2)]
    final_result = [''.join(result[i]) for i in range(0, len(result))]
    return final_result


s = 'abcdfg'

print(solution(s))
