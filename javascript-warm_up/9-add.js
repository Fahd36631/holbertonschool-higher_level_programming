#!/usr/bin/node

const args = process.argv.slice(2);

if (args.length < 2) {
  console.log(NaN);
} else {
  const a = Number(args[0]);
  const b = Number(args[1]);
  console.log(a + b);
}
