function solution(my_string) {
    let answer = 0
    return my_string.match(/[0-9]/g).map(Number).reduce((acc, num) => acc + num)
}