function solution(strings, n) {
  const mapped = new Map();
  for (let i = 0; i < strings.length; i++) {
    mapped.set(strings[i], strings[i][n]);
  }
  console.log(mapped);

  const sorted = Array.from(mapped).sort((a, b) => {
    if (a[1] === b[1]) {
      return a[0] > b[0] ? 1 : -1;
    }
    return a[1] > b[1] ? 1 : -1;
  });

  const result = sorted.map((item) => item[0]);

  return result;
}