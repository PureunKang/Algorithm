N, M = map(int, input().split())
board = [input() for _ in range(N)]

# 체스판을 다시 칠하는 최소 개수
# 최댓값으로 설정 필요
min_count = 64

# 보드의 모든 칸 검사
for i in range(N - 7):
    for j in range(M - 7):
        count_w_start = 0  # 왼쪽 위, 흰색
        count_b_start = 0  # 왼쪽 위, 검은색
        
        for x in range(8):
            for y in range(8):
                # 현재 잘라낸 보드 칸의 색상 파악
                current = board[i + x][j + y]
                
                # 체스판 형식과 비교: (x + y) % 2로 위치 색 판단
                if (x + y) % 2 == 0:
                    if current != 'W':
                        count_w_start += 1
                    if current != 'B':
                        count_b_start += 1
                else:
                    if current != 'B':
                        count_w_start += 1
                    if current != 'W':
                        count_b_start += 1
        
        # 최소 갯수 선택
        min_count = min(min_count, count_w_start, count_b_start)

print(min_count)
