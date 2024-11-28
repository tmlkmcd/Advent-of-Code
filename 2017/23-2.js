module.exports = function() {
  let echo = 0, golf = 0, hotel = 0, bravo = 106700;
  const charlie = 123700;

  do {
    let foxtrot = false;
    let delta = 2;

    do {
      if (bravo % delta === 0) {
        hotel++;
        break;
      }
    } while (++delta !== bravo);

    if (bravo === charlie) {
      console.log('Program terminated.', {
        bravo, charlie, delta, echo, foxtrot, golf, hotel
      });
      break;
    }

    bravo += 17;
  } while (true);

};