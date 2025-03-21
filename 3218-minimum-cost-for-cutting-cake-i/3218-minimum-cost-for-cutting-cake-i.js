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

    let pq = [];

    let h = m, v = n;

    for (let cut of horizontalCut) {
        pq.push([cut, 'h']);
    }

    for (let cut of verticalCut) {
        pq.push([cut, 'v']);
    }

    pq.sort((a, b) => a[0] - b[0]);

    let totalCost = 0;

    while (pq.length > 0) {
        let [cost, direction] = pq.shift();

        if (direction === 'h' && h > 1) {
            totalCost += cost * v;
            h -= 1;
        } else if(direction === 'v' && v > 1) {
            totalCost += cost * h;
            v -= 1;
        }
    }

    return totalCost;
};