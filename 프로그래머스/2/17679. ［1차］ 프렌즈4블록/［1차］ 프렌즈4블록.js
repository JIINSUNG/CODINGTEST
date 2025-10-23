function solution(m, n, board) {
    let answer = 0;
    let boards = board.map(line => line.split(""));

    while (true) {
        const removePos = new Set();

        for (let i = 0; i < m - 1; i++) {
            for (let j = 0; j < n - 1; j++) {
                const block = boards[i][j];

                if (block === '0') {
                    continue;
                }

                if (
                    block === boards[i + 1][j] &&
                    block === boards[i][j + 1] &&
                    block === boards[i + 1][j + 1]
                ) {
                    removePos.add(`${i},${j}`);
                    removePos.add(`${i + 1},${j}`);
                    removePos.add(`${i},${j + 1}`);
                    removePos.add(`${i + 1},${j + 1}`);
                }
            }
        }

        if (removePos.size === 0) {
            break;
        }

        answer += removePos.size;

        removePos.forEach((pos) => {
            const [x, y] = pos.split(',').map(Number); 
            boards[x][y] = '0'; 
        });

        for (let j = 0; j < n; j++) {
            const columnBlocks = [];
            for (let i = 0; i < m; i++) {
                if (boards[i][j] !== '0') {
                    columnBlocks.push(boards[i][j]);
                }
            }

            for (let i = m - 1; i >= 0; i--) {
                const blockIndex = columnBlocks.length - (m - i);
                
                if (blockIndex >= 0) {
                    boards[i][j] = columnBlocks[blockIndex];
                } else {
                    boards[i][j] = '0'; 
                }
            }
        }
    }

    return answer;
}