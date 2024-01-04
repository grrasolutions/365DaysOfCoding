Sorting Array :-
Using loops. 
// Example array
let numbers = [5, 2, 8, 1, 6];

// Bubble Sort algorithm
for (let i = 0; i < numbers.length - 1; i++) {
  for (let j = 0; j < numbers.length - 1 - i; j++) {
    // Swap elements if they are in the wrong order
    if (numbers[j] > numbers[j + 1]) {
      let temp = numbers[j];
      numbers[j] = numbers[j + 1];
      numbers[j + 1] = temp;
    }
  }
}
