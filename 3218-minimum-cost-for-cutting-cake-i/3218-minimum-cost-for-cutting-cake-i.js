/**
 * @param {number} m
 * @param {number} n
 * @param {number[]} horizontalCut
 * @param {number[]} verticalCut
 * @return {number}
 */
var minimumCost = function(m, n, horizontalCut, verticalCut) {
    horizontalCut.sort((a, b) => a - b);
    verticalCut.sort((a, b) => a - b);

    // Priority Queue 초기화
    let pq = [];

    // 초기 케이크 조각 크기
    let h = m, v = n;

    // 수평 및 수직 절단 비용을 Priority Queue에 추가
    for (let cut of horizontalCut) {
        pq.push([cut, 'h']);
    }
    for (let cut of verticalCut) {
        pq.push([cut, 'v']);
    }

    // Priority Queue를 비용 기준으로 정렬
    pq.sort((a, b) => a[0] - b[0]);

    // 총 비용 초기화
    let totalCost = 0;

    // 모든 절단을 처리할 때까지 반복
    while (pq.length > 0) {
        let [cost, direction] = pq.shift();

        if (direction === 'h') {
            // 수평 절단
            totalCost += cost * v;
            h -= 1;
        } else {
            // 수직 절단
            totalCost += cost * h;
            v -= 1;
        }
    }

    return totalCost;
};