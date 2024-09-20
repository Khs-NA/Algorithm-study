fun main(){
    val N = readln().toInt()
    var queue  = mutableListOf<Int>()

    for (i in 1..N) {
        val command = readln().split(" ") //리스트로 반환됨

        when (command[0]) {
            "push" -> {
                val X = command[1].toInt()
                queue.add(X)
            }
            "pop" -> {
                if (queue.isEmpty()){
                    println(-1)
                } else{
                    println(queue.removeFirst())
                }
            }
            "size" -> {
                println(queue.size)
            }
            "empty" -> {
                if (queue.isEmpty()){
                    println(1)
                } else{
                    println(0)
                }
            }
            "front" -> {
                if (queue.isEmpty()){
                    println(-1)
                } else{
                    println(queue.first())
                }
            }
            "back" -> {
                if (queue.isEmpty()){
                    println(-1)
                } else {
                    println(queue.last())
                }
            }
        }
    }
}