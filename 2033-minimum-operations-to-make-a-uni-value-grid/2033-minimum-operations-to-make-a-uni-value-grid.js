/**
 * @param {number[][]} grid
 * @param {number} x
 * @return {number}
 */
var minOperations = function(grid, x) {
        grid = grid.flat().sort((a, b) => a-b)
        let target = grid[Math.floor(grid.length / 2)]
        let answer = 0
        for (let g of grid){
            if((target-g) % x == 0){
                answer += Math.abs(target - g) / x
            }
            else
                return -1
        }

        return answer
};