const fs = require('fs');

const instructionToMotions = {
  'forward': (x, h, d) => ([h + x, d]),
  'up': (x, h, d) => ([h, d - x]),
  'down': (x, h, d) => ([h, d + x]),
};

fs.readFile(process.argv[2], 'utf-8', (err, data) => {
  console.log(
    data.split("\n")
      .map(s => s.split(' '))
      .map(([instruction, s]) => ([instruction, parseInt(s)]))
      .reduce(([h, d], [instruction, x]) => instructionToMotions[instruction](x, h, d), [0, 0])
      .reduce((acc, n) => acc * n, 1)
  );
});
