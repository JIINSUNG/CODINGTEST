function solution(my_string) {
    var answer = '';
    my_string = my_string.toLowerCase()
    my_string = my_string.split('')
    my_string.sort()
    return my_string.join('');
}