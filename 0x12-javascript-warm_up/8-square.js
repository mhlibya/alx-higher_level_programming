#!/usr/bin/node

if (isNaN(process.argv[2]) || process.argv[2] === undefined) {
	console.log('Missing size')
}
for (let i = 0; i < parseInt(process.argv[2]); i++) {
	for (let j = 0; j < parseInt(process.argv[2]); j++) {
		process.stdout.write('X');
	}
	console.log();
}
