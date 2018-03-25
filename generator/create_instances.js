const Nightmare = require('nightmare')
const nightmare = Nightmare({ show: true })

function createInstances(instances) {
  nightmare
    .goto('https://repl.it/@yevbar/SlaveNode')
    .wait(20)
    .click('div#page > div:nth-child(0) > div:nth-child(0) > div:nth-child(0) > div:nth-child(0) > div:nth-child(0) > div:nth-child(2) > div:nth-child(0) > div:nth-child(0) > div:nth-child(0) > div:nth-child(1) > div:nth-child(2) > div:nth-child(0) > span:nth-child(0)')
    .end()
    .catch(error => {
      console.error('Error: ', error)
    });
}

console.log("Starting..");

createInstances(5);
