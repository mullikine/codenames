Play Codenames with Glove
=========================

This repository implements a simple single-player version of the codenames game
by Vlaada Chvátil.
You can play as the agent or the spymaster, and the Glove word vectors will
take the role of your partner, as you try to find the 8 marked words in as few
rounds as possible.

```
$ git clone git@github.com:thomasahle/codenames.git
...
$ sh get_glove.sh
...
$ python3 codenames.py
...Loading vectors
...Normalizing
...Loading words
...Making word to index dict
...Loading codenames
Ready!

Will you be agent or spymaster?: agent

     buck       bat   pumpkin    charge      iron
     well      boot     chick superhero     glove
   stream   germany      sock    dragon scientist
     duck     bugle    school       ham   mammoth
   bridge      fair  triangle   capital      horn

Thinking 8 ... 0.110 19001
Thinking 7 ... 0.265 11339
Thinking 6 ... 0.379 2410

Clue: golden 6! (Score: 0.37934797651586716)

Your guess: bridge
Correct!
```