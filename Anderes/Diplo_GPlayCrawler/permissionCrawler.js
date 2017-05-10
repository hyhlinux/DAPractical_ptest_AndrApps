var gplay = require('google-play-scraper');


const args = process.argv[2];
console.log(args);
gplay.permissions({appId: args}).then(console.log);

setTimeout(exit, 1000)

function exit(){
	process.exit()
}