package com.example.bj2662

fun main(){
    // 변경 가능한 리스트로 선언
    val numList = mutableListOf<Int>()

    // 9개의 숫자를 입력받아 리스트에 추가
    for (i in 0..8){
        numList.add(readln().toInt()) // 입력을 정수로 변환 후 추가
    }

    // 리스트에서 최대값 구하기
    val maxNumberOfList = numList.maxOrNull()

    // 최대값 출력, 그 값의 인덱스 출력
    if (maxNumberOfList != null){
        println(maxNumberOfList)
        println(numList.indexOf(maxNumberOfList) + 1)
    }

}