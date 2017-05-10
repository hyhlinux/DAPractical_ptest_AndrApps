var gplay = require('google-play-scraper');


const numberOfElements = process.argv[2];
const startingPointOfList = process.argv[3];

gplay.list({
    category: gplay.category.MEDICAL,
    num: numberOfElements,
	start: startingPointOfList,
	country: 'en',
  })
  .then(console.log, console.log);
  
  
 
setTimeout(exit, 1700)

function exit(){
	process.exit()
}