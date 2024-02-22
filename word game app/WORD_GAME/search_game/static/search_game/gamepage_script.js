// Extract words from each array element
var extractedWords = printed_words.split(';, ').map(function(element) {
    // Remove HTML-encoded characters and extra square brackets, then parse the JSON
    return JSON.parse('["' + element.replace(/&#x27|\[|\]|\;/g, '') + '"]')[0];
});

var extractedGrid = grid.split('], [').map(function(element) {
    // Remove HTML-encoded characters and extra square brackets, then parse the JSON
    return JSON.parse('["' + element.replace(/&#x27|\[|\]|\;/g, '') + '"]')[0];
});

cleanGrid = [];
for (var i = 0; i < extractedGrid.length; i ++) {
    var k = extractedGrid[i].split(',');
    cleanGrid.push(k);
}

const gridSize = cleanGrid.length;


    document.addEventListener('DOMContentLoaded', function () {
        var tds = document.querySelectorAll('#grid td');

        tds.forEach(function(td) {
            td.addEventListener('mouseover', function() {
                this.style.backgroundColor = 'red';
            });

            td.addEventListener('mouseout', function() {
                this.style.backgroundColor = ''; // Set it back to the default color
            });
        });
    });


// document.getElementsByTagName('td').addEventListener('mouseover', myFunc);
// character = document.getElementById('1_1').innerText



