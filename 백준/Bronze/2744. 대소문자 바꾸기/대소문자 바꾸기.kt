fun main(){
    val word = readln()
    var formattedWord = word.toMutableList()
    // 각 문자를 순회하며 대문자는 소문자로, 소문자는 대문자로 변환
    for (i in 0 until formattedWord.size) {
        if (formattedWord[i].isUpperCase()) {
            formattedWord[i] = formattedWord[i].lowercaseChar() // 대문자는 소문자로 변환
        } else {
            formattedWord[i] = formattedWord[i].uppercaseChar() // 소문자는 대문자로 변환
        }
    }

    println(formattedWord.joinToString(""))
}