function printPyramid(rows) {
  for (let i = 1; i <= rows; i++) {
    let row = ' '.repeat(rows - i) + '* '.repeat(i);
    console.log(row);
  }
}
