fun main(){
    val (N, K) = readln().split(" ").map { it.toInt() }

    // 요세푸스 순열 구하기
    val josephusSequence = josephusPermutation(N, K)

    // 출력 형식에 맞춰 결과 출력
    println(josephusSequence.joinToString(prefix = "<", postfix = ">", separator = ", "))
}


fun josephusPermutation(N: Int, K:Int): List<Int>{
    val people = mutableListOf<Int>()
    val result = mutableListOf<Int>()

    for (i in 1..N){
        people.add(i)
    }

    var index = 0

    while (people.isNotEmpty()){
        index = (index + K - 1) % people.size

        result.add(people.removeAt(index))
    }

    return result

}