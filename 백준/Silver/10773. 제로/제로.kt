fun main() {
    val stack = mutableListOf<Int>()
    val K = readln().toInt()

    for (i in 0 until K) {
        val number = readln().toInt()
        if (number == 0) {
            // 스택의 마지막 요소 제거 (pop)
            if (stack.isNotEmpty()) {
                stack.removeAt(stack.size - 1)
            }
        } else {
            stack.add(number)
        }
    }

    val sumOfNumber = stack.sum()
    println(sumOfNumber)
}