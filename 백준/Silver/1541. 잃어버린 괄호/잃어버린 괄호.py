def minimize_expression(expression):
    # `-`를 기준으로 수식을 분리합니다.
    parts = expression.split('-')

    # 각 부분에서 `+`를 기준으로 숫자들을 합산합니다.
    def sum_of_parts(part):
        return sum(map(int, part.split('+')))

    # 첫 번째 부분은 그냥 더하고, 나머지 부분들은 빼줍니다.
    result = sum_of_parts(parts[0])
    for part in parts[1:]:
        result -= sum_of_parts(part)

    return result


# 입력 받기
expression = input().strip()

# 최소값 계산
print(minimize_expression(expression))
