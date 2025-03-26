/**
 * @param {number} n
 * @param {number[][]} rectangles
 * @return {boolean}
 */
var checkValidCuts = function(n, rectangles) {
    const checkIsCan = (direct) => {
        rectangles.sort((a,b) => a[direct] - b[direct])
        let lastEnd = rectangles[0][direct+2]
        let cnt = 0

        for (let rectangle of rectangles){
            if (lastEnd <= rectangle[direct]){
                cnt += 1
            }
            lastEnd = Math.max(lastEnd, rectangle[direct+2])
        }

        return cnt >= 2 ? true : false

    }

    return checkIsCan(0) || checkIsCan(1)

};