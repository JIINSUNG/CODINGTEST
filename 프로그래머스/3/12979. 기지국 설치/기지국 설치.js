

function solution(n, stations, w) {
    let answer = 0;
    let position = 1; 
    for (let i = 0; i < stations.length; i++) {
        let left = stations[i] - w; 
        if (position < left) {
            let gap = left - position;
            answer += Math.ceil(gap / (2 * w + 1));
        }
        position = stations[i] + w + 1;
    }
    // 마지막 커버 이후 남은 구간
    if (position <= n) {
        let gap = n - position + 1;
        answer += Math.ceil(gap / (2 * w + 1));
    }
    return answer;
}