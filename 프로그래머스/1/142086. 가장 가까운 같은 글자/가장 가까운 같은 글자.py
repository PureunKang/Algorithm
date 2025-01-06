def solution(s):
    # 각 문자 위치
    location_char = {}
    
    each_char = []
    
    # enumerate() => '인덱스, 요소' 튜플 반환 
    for i, char in enumerate(s):
        if char in location_char:
            each_char.append(i - location_char[char])
        else:
            each_char.append(-1)
        location_char[char] = i
                
    return each_char