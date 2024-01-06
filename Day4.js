function printCenteredNumberPyramid(rows) {
  for (let i = 1; i <= rows; i++) {
    let row = '';
    let spaces = ' '.repeat(rows - i);

    for (let j = 1; j <= i; j++) {
      row += j + ' ';
    }

    console.log(spaces + row.trim());
  }
}
