fun main() {
    val N = readln().toInt()  // 입력받은 숫자의 개수
    val Numbers = readln().map { it.toString().toInt() }  // 각 문자를 숫자로 변환하여 리스트로 만듦
    val sumOfNumbers = Numbers.sum()  // 리스트의 모든 숫자를 더함

    println(sumOfNumbers)  // 합계 출력
}