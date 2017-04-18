# Burrito Bison bot

*Edit (05-19-13): This is years old. Keeping it for time capsule  purposes..*   

Below are some of the thoughts and failed ideas that I went through while wrtting this thing. All the problems I faced
are most likely really simple and will likely seem trival as I learn more, but I leave them here for those who, like me,
are just starting out. 

Simple little script to 'play' Burrito Bison (found here: http://notdoppler.com/burritobison.php). The code is pretty
weak, this was written just to learn python a little more, and these 'launch' games all seemed mindless enough that
I could easily get a bot to control them.. (it ended up being trickier than I expected)

The code is pretty crappy, and there are tons of things I'd do differently, and, in fact, if you look at the code you'll
notice that calls start changing little by little and becoming more concise. Which was really the point of this, to 
get a little better at constructing a program. So the things I don't like about how it's written now, didn't occur to 
me as possible issues when I first started coding, but little by little, better ways of approaching a problem became 
clear. 

It's now completely workable, and will play the game from start to finish. There's only one menu that it doesn't catch,
I noticed it when I was recording the final start-to-finish playthrough, but I was too lazy to fix it. 

The bot works by gathering in about the game by taking screen shots and then checking specific pixel locations. 
It's a very fragil way to do things, as any difference in browser size ruins the expected pixel values. 

I tried all kinds of things to get around this problem. Being that all important events are different colors from the
main stage and gummies (like the cop for instance), I tried all kinds of funniness with averaging the colors of a 
snapshot, assuming that when a new color appeared on screen the average color disrtibution would change. I still think
it's a neat idea for flexibly checking what's on screen, but in practice I couldn't get it to work due to speed issues 
(and probably poor code issues). Several variations of this idea were tried in an effort to reduce the number of 
calculations needed. A few attempts were made at grayscalling the image first and then getting the colors, others 
included taking a full snapshot of the playarea, thumbnailing it to something like 25x25, and then averaging the colors
that way. 

Of all the things I tried (revalting to the getcolors idea) this proved the most reliable way 
of noticing when a cop was on screen. Reliable in my case being about (maybe)10% success rate.  Even the current 
iteration is quite poor, altough, when the bison is moving at slower speeds I'd say it's around a 40% success rate. 
Which I was happy enough with to move on. There tons of things with the current implementation that could raise this 
number quite a bit (I think). Such as multiprocessing some of the search events so there's not so much time inbetween 
calls, turning off all of the other search features that aren't needed anymore (like dialog boxes) would free up a ton
of processing room. They're the old version that takes a unique screen shot instead of 'sharing' one between all 
functions. 

 




