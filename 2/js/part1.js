const fs = require('fs');

const instructionToMotions = {
  'forward': d => ([d, 0]),
  'up': d => ([0, -d]),
  'down': d => ([0, d]),
};

fs.readFile(process.argv[2], 'utf-8', (err, data) => {
  console.log(
    data.split("\n")
      .map(s => s.split(' '))
      .map(([instruction, s]) => ([instruction, parseInt(s)]))
      .map(([instruction, d]) => instructionToMotions[instruction](d))
      .reduce(([h, d], [horizontal, depth]) => ([h + horizontal, d + depth]), [0, 0])
      .reduce((acc, n) => acc * n, 1)
  );
});
