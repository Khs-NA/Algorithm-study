package com.example.bj1008

fun main() {
    // 두 개의 Double 값을 입력받기
    val (A, B) = readln().split(" ").map { it.toDouble() }
    
    // 나눗셈 결과 출력
    println(A / B)
}
