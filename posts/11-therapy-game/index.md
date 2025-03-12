---
link: blog/therapy-game.html
title: The making of my "microtherapy" game
date: March 12 2025
---
<h1 style="margin-bottom: 0px;">The making of my "microtherapy" game</h1>
<h3 style="color: #97a9c4; margin-top: 0px;">March 12 2025</h3>

Last week, I released a game with the wordy title, [microtherapy for when you overthink a comment you made](https://jontopielski.itch.io/microtherapy). In it, you answer a few questions, receive some insights, and then draw and purge an embarassing comment you might have said from your mind.

<div style="text-align: center;">
    <div style="display: inline-block; padding-right: 10px;">
        <img class="artPanel" src="posts\11-therapy-game\cover.png" height="240px" width="320px">
    </div>
    <div style="display: inline-block; padding-left: 10px;">
        <img class="artPanel" src="posts\11-therapy-game\book.png" height="240px" width="320px">
    </div>
</div>

Of course, this is quite different from the kinds of games I usually make. Normally, I focus on fun, strategic decision making, or aesthetics and this game really has none of that. After I released it, a couple of friends have asked me what my inspiration was for it so I thought I'd talk a bit about that.

Firstly, I made the game for a game jam who's theme had to do with this concept of "perception boxes", or how we perceive the world around us based on the \[ box \] of our own lived experiences. When I first saw the theme, I was ready to dismiss it for being a little too specific and real-worldy. But then I took an extra moment to think seriously if there was anything going on in my life that might be relevant.

<div style="text-align: center;">
    <img class="artPanel" src="posts\11-therapy-game\box.png" width="50%">
</div>

And that's when I realized that yes, I was currently overthinking several (not just one) things that I said at some point to friends or family in the weeks prior that occasionally popped up while I was trying to go to sleep. Yes, they were silly, mindless comments that we all make and to be honest I can't even remember what I said at this point. But I knew then that they were causing me a little bit of anxiety.

So, I wondered if there was something I could do with this disturbed feeling and make a game around that. And that's when I thought back to a game I had played a few years ago where you got to draw (or type) a message onto a paper, put it inside of a glass bottle, and drop it into a river that gets dumped into the ocean. I can't remember the game's name but I remember playing it and feeling a bit better after releasing a nagging thought into the wild.

I decided to try to make a game like this but for my comment anxiety. I thought I'd also include a section where you got to answer a few questions before you actually purge your negative thought (like a therapy session). I typed up some questions into a Google spreadsheet and then I manually "played" the game by thinking of an embarassing comment myself and going through the sequence of questions to see if it actually helped me.

<div style="text-align: center;">
    <img class="artPanel" src="posts\11-therapy-game\sheet.png" width="50%">
</div>

Surprisingly enough, it kinda worked! I did feel a bit better after answering the questions and hearing some advice (even though I was the one who *wrote* the questions and advice). Now all I had to do was translate the questions into Godot and build the drawing and purging part.

For the canvas, I decided to keep things really simple and just have drawing and erasing via the mouse. I considered having a textbox too but decided it would be too much work. After all, I only gave myself a few days to work on this. I created a blank canvas inside of a SubViewport in Godot (with Viewport clearing every frame turned off) and that was pretty much all I needed to be able to draw freely.

<div style="text-align: center;">
    <img class="artPanel" src="posts\11-therapy-game\drawing.png" width="50%">
</div>

For the purging, I decided to go with a very simple custom "particle" system - basically just instantiating a circle at a certain point that moves upwards, shrinks, and then deletes itself. Spawning a bunch of these with slight changes to their parameters was enough to make it look vaguely smoke-esque.

<div style="text-align: center;">
    <img class="artPanel" src="posts\11-therapy-game\smoke.gif" width="75%">
</div>

I still didn't know if purging a drawing would actually make you feel better. I couldn't test the theory until the project was basically done. For all I knew, it could have done absolutely nothing or maybe even made things worse. But yet again, I tested it myself and somehow it worked and made me feel better, even if a little bit.

In all honesty, I thought nobody would play this game or get it and I even debated releasing it on an anonymous account, out of fear. My criteria was if one person was helped even to the smallest degree, it will have been worth putting out. And thankfully, I succeeded in that at least several people claimed to have been helped by the project:

<div style="text-align: center;">
    <img class="artPanel" src="posts\11-therapy-game\comments.png" width="75%">
</div>

Finally, I attempted to make music for this project, which I'm pretty bad at. But if you want to give it a listen, the two very short (and simple) songs can be found here: [microtherapy ost](https://jontopielski.bandcamp.com/album/microtherapy-for-when-you-overthink-a-comment-you-made)