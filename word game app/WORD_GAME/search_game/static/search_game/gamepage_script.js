// Extract words from each array element
var extractedWords = printed_words.split(';, ').map(function(element) {
    // Remove HTML-encoded characters and extra square brackets, then parse the JSON
    return JSON.parse('["' + element.replace(/&#x27|\[|\]|\;/g, '') + '"]')[0];
});

var extractedGrid = grid.split('], [').map(function(element) {
    // Remove HTML-encoded characters and extra square brackets, then parse the JSON
    return JSON.parse('["' + element.replace(/&#x27|\[|\]|\;/g, '') + '"]')[0];
});

let cleanGrid = [];
for (var i = 0; i < extractedGrid.length; i ++) {
    var k = extractedGrid[i].split(',');
    cleanGrid.push(k);
}

const gridSize = cleanGrid.length;

//word list is stored in extractedWords
//grid is stored in a 2d array called cleanGrid
//grid size is stored in gridSize


let X1 = 0;
let Y1 = 0;
let X2 = 0;
let Y2 = 0;
let x1 = 0;
let y1 = 0;
let x2 = 0;
let y2 = 0;
let count = 0;
document.addEventListener('DOMContentLoaded', function () {
    
    var tds = document.querySelectorAll('#grid td');
    let counter = 0;

    tds.forEach(function(td) {

    td.addEventListener('click', function() {
        counter++;
        if (counter == 1) {
            [X1, Y1] = this.id.split('_');
            x1= parseInt(X1);
            y1 = parseInt(Y1);
            this.style.backgroundColor = 'blue';
        } 
        else if (counter == 2) {
            document.getElementById(`${x1}_${y1}`).style.backgroundColor = ''
            [X2, Y2] = this.id.split('_');
            x2= parseInt(X2);
            y2 = parseInt(Y2);
            let selectedString = '';

            if (x1 == x2){
                if (y1 < y2) {
                    for(let i = y1-1; i < y2; i++) {
                        selectedString += cleanGrid[x1-1][i].trim();
                    }
                }

                if (y2 < y1) {
                    for(let i = y1; i >= y2; i--) {
                        selectedString += cleanGrid[x1-1][i-1].trim();
                    }
                }
            }

            if (y1 == y2) {
                if (x1 < x2) {
                    for(var i = x1; i <= x2; i++) {
                        selectedString += cleanGrid[i-1][y1-1].trim();
                    }
                }

                if (x2 < x1) {
                    for(var i = x1; i >= x2; i--) {
                        selectedString += cleanGrid[i-1][y1-1].trim();
                    }
                }
            }

            
            if (Math.abs(y2 - y1) == x2 - x1) {
                if (y2 > y1) {
                    for (var i = 0; i <= y2 - y1; i++) {
                        selectedString += cleanGrid[x1 + i - 1][y1 + i - 1].trim();
                    }
                }
            
                if (y1 > y2) {
                    for (var i = 0; i <= y1 - y2; i++) {
                        selectedString += cleanGrid[x1 + i - 1][y1 - i - 1].trim();
                    }
                }
            } 
                            
            counter = 0;
            extractedWords.forEach(function(word){
                wordElem = document.getElementById(word);
                if (word == selectedString && wordElem.style.borderColor != 'green') {
                    wordElem = document.getElementById(word);
                    wordElem.style.borderColor = 'green';
                    wordElem.style.backgroundColor = 'white';
                    if (x1 == x2){
                        if (y1 < y2) {
                            for(let i = y1-1; i < y2; i++) {
                                document.getElementById(`${x1}_${i+1}`).style.backgroundColor = 'green';
                            }
                        }
        
                        if (y2 < y1) {
                            for(let i = y1; i >= y2; i--) {
                                document.getElementById(`${x1}_${i}`).style.backgroundColor = 'green';
                            }
                        }
                    }
        
                    if (y1 == y2) {
                        if (x1 < x2) {
                            for(var i = x1; i <= x2; i++) {
                                document.getElementById(`${i}_${y1}`).style.backgroundColor = 'green';
                            }
                        }
        
                        if (x2 < x1) {
                            for(var i = x1; i >= x2; i--) {
                                document.getElementById(`${i}_${y1}`).style.backgroundColor = 'green';
                            }
                        }
                    }
        
                    
                    if (Math.abs(y2 - y1) == x2 - x1) {
                        if (y2 > y1) {
                            for (var i = 0; i <= y2 - y1; i++) {
                                document.getElementById(`${x1+i}_${y1+i}`).style.backgroundColor = 'green';
                            }
                        }
                    
                        if (y1 > y2) {
                            for (var i = 0; i <= y1 - y2; i++) {
                                document.getElementById(`${x1+i}_${y1-i}`).style.backgroundColor = 'green';
                            }
                        }
                    }
                    count++;
                }
            })

            if (count == extractedWords.length) {
                document.getElementById('gameOver').style.display = 'block';
                document.getElementById('restartButton').style.display = 'flex';
                document.getElementById('redirectLink').style.display = 'none';
            }

            
        }
        
    })
    });
});




