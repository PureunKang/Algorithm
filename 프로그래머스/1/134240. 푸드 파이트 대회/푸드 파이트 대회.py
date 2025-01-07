def solution(food):
    arrForFood = []

    # 물 제외하여 순회
    for i in range(1, len(food)):
        # 사용할 음식 갯수 (일단 arrForFood 배열의 절반만 만들 것)
        usedFood = food[i] // 2
        # extend, 특정요소 여러번 추가 가능
        arrForFood.extend([str(i)] * usedFood)
    
    # 배열 절반 + 물 + 배열 거울상 절반 (역순 만들기 [::-1])
    result = ''.join(arrForFood) + '0' + ''.join(arrForFood[::-1])
    
    return result