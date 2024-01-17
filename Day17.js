function diamond(row) {
    s = "";
  // upper
    for (i = 1; i < row + 1; i++) {
      s += "\n";
      for (j = 1; j <= row - i + 1; j++) {
        s += "*";
      }
      for (j = 1; j <= 2 * i - 1; j++) {
        if (j == 1 || j == 2 * i - 1) {
          s += "$";
        } else {
          s += " ";
        }
      }
      for (j = 1; j <= row - i + 1; j++) {
        s += "*";
      }
    }
  // bellow
    for (i = row - 1; i > 0; i--) {
      s += "\n";
      for (j = 1; j <= row - i + 1; j++) {
        s += "*";
      }
      for (j = 1; j <= 2 * i - 1; j++) {
        if (j == 1 || j == 2 * i - 1) {
          s += "$";
        } else {
          s += " ";
        }
      }
      for (j = 1; j <= row - i + 1; j++) {
        s += "*";
      }
    }
    return s;
  }
  console.log(diamond(5));