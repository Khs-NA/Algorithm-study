fun main() {
    val N = readln().toInt()
    var count = 0
    var weight = N

    while (weight >= 0) {
        // 5킬로그램 봉지를 최대한 사용하고, 남은 무게를 3으로 나누어떨어지게 처리
        if (weight % 5 == 0) {
            count += weight / 5
            println(count)
            return
        }
        // 5로 나누어 떨어지지 않으면 3킬로그램 봉지를 하나 추가해서 무게를 줄임
        weight -= 3
        count++
    }

    // 정확히 나누어떨어지지 않을 경우
    println(-1)
}