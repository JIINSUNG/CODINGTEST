function solution(numbers) {
    var answer = 0;
    numbers.sort((a, b) => a-b)
    return Math.max(numbers[0] * numbers[1], numbers.at(-1) * numbers.at(-2))
}