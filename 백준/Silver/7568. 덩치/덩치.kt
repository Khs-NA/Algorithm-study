fun main(){
    val N = readln().toInt()
    val cnt = MutableList(N) { 1 }

    val people = MutableList(N) {
        readln().split(" ").map { it.toInt() }
    }

    for( i in 0 until N){
        for(j in 0 until N){
            if(people[i][0] > people[j][0] && people[i][1] > people[j][1]){
                cnt[j] += 1
            }
        }
    }

    cnt?.let{
        println(cnt.joinToString(" "))
    }

}