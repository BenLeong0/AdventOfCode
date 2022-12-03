import * as fs from 'fs';


const INPUT_FILE = "inputs/day01.in"

const part1 = Math.max(...fs.readFileSync(INPUT_FILE, "utf8").split("\n\n").map(b => b.split("\n").reduce((x,y)=>x+parseInt(y),0)))
const part2 = fs.readFileSync(INPUT_FILE, "utf8").split("\n\n").map(b => b.split("\n").reduce((x,y)=>x+parseInt(y),0)).sort().slice(-3).reduce((x,y)=>x+y)

console.log(part1)
console.log(part2)
