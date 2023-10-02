---
link: blog/methods-for-onboarding.html
title: Methods for onboarding players
date: July 28 2022
---
<h1 style="margin-bottom: 0px;">Methods for onboarding players</h1>
<h3 style="color: #97a9c4; margin-top: 0px;">July 28 2022</h3>

A common pitfall when trying to teach a game is for designers to create a rules page with a huge wall of text. The problem is that players haven’t even played the game yet and you’re asking them for too much before they even know what the game is like. Players need to be able to interact with things in order to figure out how the game works.

I’ve been guilty of throwing players into the deep end. [Ghost Roulette](https://jontopielski.itch.io/ghost-roulette) is a game of tactical roulette where the rules are never explained to the player. Below are the first three screens that a player sees when they start the game. See if you have any idea how the game works (answer at the bottom of this post, if curious).

<div style="text-align: center;">
    <div style="display: inline-block;">
        <img class="artPanel" src="posts/04-methods-for-onboarding/ghost-roulette-intro.png" height="175px" width="225px">
    </div>
    <div style="display: inline-block;">
        <img class="artPanel" src="posts/04-methods-for-onboarding/ghost-roulette-second.png" height="175px" width="225px">
    </div>
    <div style="display: inline-block;">
        <img class="artPanel" src="posts/04-methods-for-onboarding/ghost-roulette-gameplay.png" height="175px" width="225px">
    </div>
</div>

While some players could eventually figure out the rules through trial and error, it’s not an ideal experience and many will not stick around. There is no need for this unnecessary friction in the onboarding process.

Below I outline a few onboarding solutions that differ depending on the type of game and the amount of work required. I also provide examples from my own games.

## The Tutorial

Tutorials are effective and robust, but costly for both the player and the designer. Players would rather not go through them because they’re tedious and designers would rather not create them because they often require tweaking systems with one-off exceptions.

Still, tutorials definitely have their place. If your game has many interconnected systems or has complex, unintuitive mechanics, a tutorial is probably a good idea.

<div style="text-align: center;">
    <img class="artPanel" src="posts/04-methods-for-onboarding/flipjack.png" width="75%">
</div>

My most recent game, [Flipjack](https://prifurin.itch.io/flipjack), requires a tutorial because the game’s mechanics and art style are obtuse and experimental, by design. I probably won’t be making something this abstract again, but it’s a good example of when you absolutely need a tutorial.

## The In-Game Instructions

The in-game instructions are a great way to describe the rules of a game while the game is happening. Usually these appear on-screen in the introductory stage and can provide passive instructions or checkbox-style tasks that block progress until they are completed. In-game instructions are useful when there are only a few key rules to a game that the player needs to understand.

<div style="text-align: center;">
    <img class="artPanel" src="posts/04-methods-for-onboarding/deep-web-instructions.png" width="75%">
</div>

[Into the Deep Web](https://jontopielski.itch.io/into-the-deep-web) is an auto-battler where players can manipulate dice values by dragging ability buttons on top of the dice. Only a few in-game instructions are needed to convey this idea and I decided to add them to the first level with both text (while the game’s UI is in the background) and an on-screen task.

In-game instructions share some of the same designer cost as tutorials, often requiring one-off exceptions in core gameplay systems when the player is still learning. Additionally, the designer has the challenge of making sure the first gameplay area is not too difficult so its teachable, but also interesting enough so that if there are subsequent playthroughs in the future, it’s not a complete waste of time.

## The Invisible Tutorial

The invisible tutorial is when the game’s difficulty curve is so gentle that the player doesn’t even realize that they are being tutorialized. They think they are just playing the game. The first few levels or moments of the game are designed in such a way that they teach the player one small thing at a time and build up to the point where the player knows everything they need to play the game.

<div style="text-align: center;">
    <img class="artPanel" src="posts/04-methods-for-onboarding/puzzle-sigma.png" width="75%">
</div>

In [Puzzle Sigma](https://jontopielski.itch.io/puzzle-sigma), you touch a flag to move to the next level. Then, you grab number blocks to form expressions. Then, you rotate the blocks to alter them. And so on. The cognitive load on the player is very light and they aren’t faced with a real challenge until the fourth level.

The invisible tutorial is not a good idea in replayable games (like roguelikes) because experienced players will be forced to play the same introductory sections over and over again.

## No Tutorial, By Design

Another way to reduce tutorialization is in the game’s overall design and user interface. Everything from the art style, to the sound effects, to the game’s title should help improve the game’s clarity. If you build things in an intuitive way that leverages existing knowledge, players will have an easier time understanding what is going on. If a game is so intuitively designed that from reading the title and seeing a screenshot of the game, a new player could tell exactly what’s going on, then no tutorial is needed.

<div style="text-align: center;">
    <img class="artPanel" src="posts/04-methods-for-onboarding/spinny-discs.png" width="75%">
</div>

[Spinny Discs](https://jontopielski.itch.io/spinny-discs) is a game all about hitting and dodging big discs. That’s it. Screenshots show the arena top-down movement of the game with a protagonist and some things you might want to avoid (namely, the spinning discs). The game design speaks for itself.

It should be noted that this method is not always possible when a game design is more esoteric or unique. If the benefits of an unintuitive system outweigh the cons of the cognitive load on the player, you should keep that system even if it’s hard to explain.

## Conclusion

Sometimes a single instructive sentence can make or break a player’s onboarding experience. Onboarding is extremely important and understanding the complexity of your game’s rules is essential to determining the appropriate onboarding system. Usually, the one with the least cognitive load on the player is best.

Jon

_Ghost Roulette rules are: enemies bet before you do, each round consists of exactly 3 turns, and you have a deck of cards that allows you to manipulate chips on the table before the roulette wheel spins_