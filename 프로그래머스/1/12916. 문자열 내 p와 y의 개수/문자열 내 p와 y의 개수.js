function solution(s){

const convertedS = s
  .toLowerCase()
  .split("")
  .filter((char) => char !== " ");

let countP = 0;
let countY = 0;

for (let char of convertedS) {
  if (char === "p") {
    countP++;
  } else if (char === "y") {
    countY++;
  } else {
    continue;
  }
}
if (countP === countY) {
  return true;
} else {
  return false;
}
}