def solution(t, p):
    p_length = len(p)
    p_value = int(p)
    # 조건을 만족하는 부분 문자열의 개수를 저장할 변수
    count = 0

    # t 순회, p와 길이가 같은 부분 문자열을 확인
    for i in range(len(t) - p_length + 1):
        # 현재 위치에서 길이 p_length만큼 부분문자열(substring) 추출
        substring = t[i:i + p_length]
        # 부분문자열, 정수 변환 후 p_value와 비교
        if int(substring) <= p_value:
            count += 1

    return count