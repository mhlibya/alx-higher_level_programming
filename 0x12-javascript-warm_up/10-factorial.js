#!/usr/bin/node

function factorial(n) {
	if (n == 0 || n == 1 || n == undefined || isNaN(n)) {
		return (1);
	} else {
		return (n * factorial(n - 1));
	}
}
console.log(factorial(Number(process.argv[2])));
