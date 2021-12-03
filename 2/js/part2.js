const fs = require('fs');

const instructionToMotions = {
  'forward': (x, h, d, a) => ([h + x, d + a * x, a]),
  'up': (x, h, d, a) => ([h, d, a - x]),
  'down': (x, h, d, a) => ([h, d, a + x]),
};

fs.readFile(process.argv[2], 'utf-8', (err, data) => {
  console.log(
    data.split("\n")
      .map(s => s.split(' '))
      .map(([instruction, s]) => ([instruction, parseInt(s)]))
      .reduce(([h, d, a], [instruction, x]) => instructionToMotions[instruction](x, h, d, a), [0, 0, 0])
      .slice(0, 2)
      .reduce((acc, n) => acc * n, 1)
  );
});
