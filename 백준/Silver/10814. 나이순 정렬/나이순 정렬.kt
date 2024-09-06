fun main() {
    val N = readln().toInt()
    var people = MutableList(N) {
        readln().split(" ")
    }

    // 나이(첫 번째 요소)를 기준으로 우선 정렬하고, 나이가 같으면 인덱스 순서대로 정렬
    people = people.withIndex()
        .sortedWith(compareBy({ it.value[0].toInt() }, { it.index }))
        .map { it.value }
        .toMutableList()

    // 출력
    people.forEach {
        println("${it[0]} ${it[1]}")
    }
}