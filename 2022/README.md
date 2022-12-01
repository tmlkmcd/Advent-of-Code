## Day 1

- Estimated completion time: ~3 minutes

Easy peasy. Got snagged for a minute on parsing the empty line between each elf which was a bit silly.

## Day 2

- Estimated completion time: ~20 minutes

Hard-coding ftw. Fumbled a lot on trying to figure out a more dynamic strategy before deciding to simply hard-code everything. I'm TOO TIRED!!

## Day 3

- Estimated completion time: ~15 minutes

Spent a long time fumbling over part 1 because I wasn't sure if I had understood the question correctly (unique duplicates or just all duplicates?) - my solution kept coming up with a number that was way too high then randomly output the right answer without any change on my part that I knew of. Part 2 went down on the first try (about 2 minutes) which is atypical for me.

## Day 4

- Estimated completion time: ~15 minutes

This 5am thing is really biting me. Trying to get the logic right when I can barely think is a bit of a monster...

## Day 5

- Estimated completion time: ~30 minutes

As ever, long time deciding how to parse input in a half-asleep haze. Though each step of the way lots of debugging and figuring out but it did go down smoothly. Getting harder but still fun.

## Day 6

- Estimated completion time: ~15 minutes

Surprisingly easy that we're near a week into the challenge, should have finished a lot faster but got snagged on the looping/deduping logic which I think I'd have done much faster in JavaScript. It being 5am still doesn't help...

Also, didn't know about sets in python / that they were that similar to JS. This is how we learn!!

## Day 7

- Estimated completion time: ~35 minutes

First trickier one of the year and great fun. Object-oriented programming ftw. Had a full night's sleep last night - the right choice, I'd never have been able to do this one groggy...

## Day 8

- Estimated completion time: ~70 minutes

Tough one today. Both parts there was trouble getting the looping logic correct, part 2 I had trouble with because I misread the brief a few times before implementing it correctly.

## Day 9

- Estimated completion time: ~90 minutes

Much of the delay was implementing the 'snapping' logic when a 'tail' piece has to move diagonally (and implementing various visualisations before I realised that was what the bug was).

#### Forgot to update for a few days...

Last time I was on a train in mainland Europe doing [Advent of Code](https://adventofcode.com/2019/day/13) I was [playing breakout](https://github.com/tmlkmcd/AoC-2019/commit/3845d1b5b20cc2cded70ea0cf9d1ff9f3ae00a11) on an intcode computer...

## Day 10

- Estimated completion time: ~45 minutes 

Didn't complete this on the actual day due to illness. Most of the delay came from trying to figure out what the problem actually meant (both parts) with the TV on (but how good is The Office, right??). Initially tried to implement as a simply line loop that increments the step by 2 (but needs to double up the code for each cycle for the 'addx' command). Decided this wouldn't work for part 2, tried rebuilding it as a per-cycle loop but wasn't sure of a clean way to increment the register so went back to the first solution.

Ended up with a bug that meant certain pixels were missing in part 2 so I couldn't read the message. After some tinkering about, it seemed to fix itself and I'm not sure what I had wrong to begin with...🤷

## Day 11

- Estimated completion time: ~30 minutes

OOP for the win again. Had a little trouble implementing the 'keep away' logic correctly, mostly - as ever - because my knowledge of the nuances of python are holding me back a little but otherwise it works well enough. Caught onto the 'trick' for part 2 quite quickly, reminded me of another similar problem a few [years ago](https://adventofcode.com/2020/day/13). 

## Day 12

- Estimated completion time: ~30 minutes

Thankfully learned Dijkstra's as a [solution](https://github.com/tmlkmcd/AoC-2021/blob/master/day15/sol-2.py) to one of [last year's problems](https://adventofcode.com/2021/day/15), got a little stuck implementing it in a way that wasn't causing the 'pointer' to simply run around the map in circles but got there in the end.

Part 2 came quite easily once I figured out it was blowing the recursion limit because not all potential starting points can even reach the end, brute-forcing the solution was a bit of a cheat - I'd prefer to have a method that automagically eliminates unnecessary starting points if another successful path already has shown there to be a closer 'a', but the original pathfinding solution was fast enough that this was actually viable.

## Day 13

- Estimated completion time: ~20 minutes

Surprised at how quickly this one went down. Misread the problem at the start so implemented the solution slightly wrong but the correction was easy to make. Part 2 as easy as implementing a sorting function.

## Day 14

- Estimated completion time: ~35 minutes

Given how much the [similar](https://adventofcode.com/2018/day/17) problem put me off a few years ago (especially considering I was doing that year in GoLang), surprised at how quickly this one went down too. I must be getting better.

## Day 15

- Estimated completion time: ~60 minutes

Got snagged for way too long not realising that my regex was not parsing negative numbers and giving me too low an output for pt 1. Worked pretty quickly once I fixed that.

Part 2 decided to see if a library existed for merging ranges instead of simply doing it manually (low and behold, there was something). Feels a bit cheap to still brute-force my way through all y-coordinates to find the right one but definitely much faster than cycling through every coordinate manually. Takes a long time to run when scanning 4 million by 4 million points but I guess this is perhaps the quickest that could be expected 🤷 I'm not fussed about implementing sub-optimal solutions whilst I'm on holiday...

## Day 16

- Estimated completion time: ~150 minutes

By far the hardest exercise for AoC this year (so far...?). Still not even 100% sure that my answer would work for all inputs but it got me the stars so I'm happy, plus I have the extra hours while the gf is napping (still on holiday here)...

Both parts run pretty quickly on the test input but with the puzzle input, part 2 took about 5 minutes to complete.

## Day 17

- Estimated completion time: ~3 hours

Harder than yesterday? Part 1 went down easy - was fun - part 2 I could not figure out where this 'fudge factor' was coming from but it appeared consistently in the results off-setting the remainder for some unknown reason. A lot of time spent figuring out what said fudge-factor was through trial and error. Not a good solution but until I can figure out where the extra amount was coming from 🤷

## Day 18

- Estimated completion time: ~1 hour

Nice easy one to round out the weekend, still got snagged on working out how to calculate an 'infinite' area in a reasonable amount of time. Current solution does work but does take a few minutes to run. But we have to check out of the hotel in under an hour so it'll have to do 🤷

## Day 19

- Estimated completion time: ~6 hours, on-and-off

Most of this time spent waiting for a solution to run. Initially calculated absolutely every step possible per minute which caused the program to peak at about 45Gb mem usage for part 1, decided that waiting for the program to scan a list of 150 million items when much of it is held in swap space was impractical.

Next, tried the same but with some hashing code to de-dupe and not calculate some possibilities unnecessarily and reworked the solution to DFS instead of BFS, bringing down the mem usage to max about half a gig (for memo-ization), managed to calculate part 1 in a few hours.

Not sure why it took so long to calculate based on production steps rather than minutes which is similar to the approach taken in day 16. This cut the time taken for part 1 to almost instant and part 2 to a couple of minutes. There are further optimisations to consider here but I'm fine with what I have...

## Day 20

- Estimated completion time: 20 minutes

First easy one for a while. Spent some time trying to figure out a strategy before deciding that I could use complex numbers to track the original position of the number in the list as it keeps moving (works over multiple 'mix' cycles too). Deque usage was down to remembering how the [marble game](https://adventofcode.com/2018/day/9) worked in an earlier year.

## Day 21

- Estimated completion time: 45 minutes

The comments in the code tell the story here. Part 1 easy-peasy. Part 2 tried brute-forcing, it got to about 30000 before I decided there was probably a slicker approach (actual answer was about 8 orders of magnitude higher). I'm sure there's a programmatic way to calculate the needed value for 'humn' here but I figured it was probably faster to simply manually calculate it.

## Day 22

- Estimated completion time: ~4 hours

Part 1 was fun - not much to say here. Part 2 I had a heck of a time making a miniature cube just to help me visualise which face connected to which face and was painstakingly going through my hard-coding, checking all of the connections with test inputs, until realising that I was getting the wrong answer because I wasn't resetting the navigator's direction if they encountered a wall as soon as they had changed face on the cube. Then submitted the wrong answer because I ran the correct program against a testing input... 🤦

## Day 23

- Estimated completion time: ~2 hours

Enjoyed this one but it took a long time. Got snagged on simulating each 'round' correctly, mostly because I missed certain parts of the description and the code I'd written was not so easily adapted.

Part 2 took a long time to simulate (estimated about 2 rounds a second; given that the answer was just under 1000 that's a little under 10 minutes to simulate) - I had already implemented every optimisation I could think of when writing part 1, further optimisations included not checking elves that had not moved for a long time (but other elves might then get near them much later) or elves in areas that had been dormant for a while...but figured it was just easier to let the simulation run since I had an idea of how far through it was. Turned out to be fine...

## Day 24

- Estimated completion time: ~1.5 hours

Enjoyed this one too, was pretty proud of the way I chose to model the blizzards. Couldn't figure out why it seemed to be running forever until, when running the program against a testing input, I figured that I wasn't memo-izing the previously seen outcomes properly. Program takes a long time to run (few minutes per step) but I'm fine with that since it got me the correct answer.

## 🎄

- Estimated completion time: 1 hour

Converting from 'snafu' is easy, converting from it took a long time to figure out a strategy. I ended up manually calculating the answer just to submit something quickly - it worked but was not elegant. The loop I have in place now was derived shortly after. 

Merry Christmas!

Conclusion: had heaps of fun this year in spite of the banging my head on a table trying to get day 19 to run. Will be much faster next year.