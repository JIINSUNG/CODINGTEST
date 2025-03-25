/**
 * @param {number} days
 * @param {number[][]} meetings
 * @return {number}
 */
var countDays = function(days, meetings) {
    let answer = 0 
    let start = 1
    meetings.sort((a, b)=> a[0]-b[0])
    for (let [s, e] of meetings){
        console.log(start, s, e)
        if (start < s){
            answer += s - start
        }
        start = Math.max(start, e + 1)
    }

    return answer + (days-start+1)
};