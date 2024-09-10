package com.project.a09_10

fun main(){
    val N = readln().toInt()
    var numberOfList = MutableList(N) {
        readln().split(" ").map {it.toInt()}
    }

    val sortedList = numberOfList.sortedWith(compareBy({ it[1]}, { it[0] } ))

    sortedList.forEach { println(it.joinToString(" ")) }



}