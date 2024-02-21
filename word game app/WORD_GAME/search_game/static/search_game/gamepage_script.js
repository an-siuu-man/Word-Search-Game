let isMouseDown = false;
let selectedLetters = [];
let startCell = null;

document.getElementById('grid').addEventListener('mousedown', function (event) {
    isMouseDown = true;
    selectedLetters = [];
    startCell = event.target;
});

document.addEventListener('mouseup', function () {
    isMouseDown = false;
    displaySelectedLetters();
    startCell = null;
});

function handleCellClick(event) {
    if (isMouseDown) {
        const cell = event.target;
        const letter = cell.textContent;

        // Check if the letter is not already in the selectedLetters array
        if (!selectedLetters.includes(letter)) {
            selectedLetters.push(letter);
            cell.classList.add('selected');
        } else {
            // If the letter is already selected, remove it
            selectedLetters = selectedLetters.filter(selected => selected !== letter);
            cell.classList.remove('selected');
        }
    }
}

function displaySelectedLetters() {
    const selectedString = selectedLetters.join('');
    console.log('Selected letters:', selectedString);
    // You can do whatever you want with the selected string here
}

document.getElementById('grid').addEventListener('mouseover', function (event) {
    if (isMouseDown) {
        handleCellClick(event);
    }
});

document.getElementById('grid').addEventListener('click', function (event) {
    handleCellClick(event);
});

document.getElementById('grid').addEventListener('focusin', function (event) {
    const cell = event.target;
    cell.classList.add('read');
});

document.getElementById('grid').addEventListener('focusout', function (event) {
    const cell = event.target;
    cell.classList.remove('read');
});

// Function to get letters between two cells
function getLettersBetweenCells(start, end) {
    const startRow = start.parentNode.rowIndex;
    const startCol = start.cellIndex;
    const endRow = end.parentNode.rowIndex;
    const endCol = end.cellIndex;

    const letters = [];

    for (let row = Math.min(startRow, endRow); row <= Math.max(startRow, endRow); row++) {
        for (let col = Math.min(startCol, endCol); col <= Math.max(startCol, endCol); col++) {
            const cell = document.getElementById('grid').rows[row].cells[col];
            letters.push(cell.textContent);
        }
    }

    return letters.join('');
}

// Event listener for the double click to get letters between two cells
document.getElementById('grid').addEventListener('dblclick', function (event) {
    if (startCell && isMouseDown) {
        const endCell = event.target;
        const selectedString = getLettersBetweenCells(startCell, endCell);
        console.log('Letters between two cells:', selectedString);
    }
});


