#!/usr/bin/node

if (process.argv.length <= 3) {
	console.log('0');
} else {
	const arr = process.argv.slice(2).map(Number);
	const second = arr.sort(function (a, b) { return (a - b)})[1];
	console.log(second)
}
