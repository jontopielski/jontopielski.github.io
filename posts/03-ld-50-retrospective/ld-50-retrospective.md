---
link: blog/ludum-dare-50-retrospective.html
title: Ludum Dare 50 retrospective
date: April 27 2022
---
<h1 style="margin-bottom: 0px;">Ludum Dare 50 retrospective</h1>
<h3 style="color: #97a9c4; margin-top: 0px;">April 27 2022</h3>

Since my [first ever game jam](https://jontopielski.itch.io/retrorunner) roughly 3 years ago, I’ve learned a lot. And yet, things still don’t seem to be getting much easier. Shouldn’t they be getting easier?

This post is both a retrospective for my most recent [Ludum Dare](https://jontopielski.itch.io/hearts-ablaze) I participated in, as well as some things I’ve learned over the years. Hope it’s helpful to someone out there.

<div style="text-align: center;">
    <div style="display: inline-block;">
        <img class="artPanel" src="posts/03-ld-50-retrospective/hearts-ablaze.png" height="225px" width="300px">
    </div>
    <div style="display: inline-block;">
        <img class="artPanel" src="posts/03-ld-50-retrospective/hearts-ablaze-result.png" height="225px" width="300px">
    </div>
</div>

## 1. Making something is better than making nothing

Lots of people want to be game devs without doing the work. What’s most important is that something gets made, not the actual quality of the thing being made. Whether the end result is “good” or “bad” doesn’t matter. Every game provides a learning opportunity, a piece of feedback that says you’re moving in the right or wrong direction. Quantity leads to quality over time.

While coming up with ideas for this game jam, I kept hesitating to commit to anything. I was paralyzed by the desire to come up with a remarkable idea right from the start. This was causing a huge delay and starting to stress my team members. Eventually, we decided to just get to work on a relatively simple idea. In the end, we made something and that’s all that matters.

<div style="text-align: center;">
    <img class="artPanel" src="posts/03-ld-50-retrospective/hearts-ablaze-overthinking.png" width="50%">
</div>

## 2. Game jams never get easier

I’ve done 25 game jams in the last 3 years and it doesn’t seem to be getting any easier. It might never get easier. Every game is different. Different design problems, code structures, art styles, game loops, time constraints, team conditions, and more. There are constantly new and challenging problems that require new and challenging solutions.

One challenge while coming up with the character design in Hearts Ablaze was how to portray the player’s gun. While the player itself was a static sprite that locked to 8 directions, the gun needed to be able to point in any direction so that the player knows they can shoot freely from any angle.

To solve this, I made the gun 3d whereas the player is 2d. Initially, this made the gun feel out of place alongside the character sprite. However, I then applied an outline shader to the 3d gun to make it look more “2d”. This is just one example of the unique types of problems you constantly face while making a game.

<div style="text-align: center;">
    <img class="artPanel" src="posts/03-ld-50-retrospective/hearts-ablaze-shooting.gif" width="50%">
</div>

## 3. The order in which you make a game (might) matter

Let me paint you a “hypothetical” picture. Your “friend” is making a game and she spends the first 50% of her time on the artwork. Then, she does the cover art, even though the game isn’t playable yet. Now, she only has 1 day left and what does she do? She redraws the character art and then spends the rest of the day on environment art. Now there’s only 3 hours left in the jam. She realizes she needs to make the game playable so she aggressively puts the game loop together and with 5 minutes left submits her game.

How is the game, you ask?

Broken. Unbalanced. Lacking content. Inaccessible.

What happened here?

There are technically no rules when it comes to making games. You can start with the art.. the story.. an IPA? You can do whatever you want. But. If you are going for a polished, balanced, gameplay-heavy experience, then you should probably get the gameplay loop working as soon as possible.

This is sadly a lesson I keep learning time and time again. Most of my jam games are not playable until the last hour. And my games usually suffer because of this. In my opinion, having a gameplay loop working early on is one of the healthiest ways to approach making games.

<div style="text-align: center;">
    <img class="artPanel" src="posts/03-ld-50-retrospective/hearts-ablaze-last-second.png" width="50%">
</div>

## 4. Having a team you trust is awesome

Working with a team can be an extremely rewarding experience if you find the right people. People who aren’t afraid to challenge your ideas or push you to your creative limits. When everyone trusts each other, not only is the work more efficient, but everyone has a say in the direction of the project and their opinions make the project wholly better.

Working with [Mafgar](https://twitter.com/mafgar_online), [Alphons6](https://twitter.com/Alphons63), and [Riceputtin](https://twitter.com/Riceputtin2) was a blast because we all respected each others’ opinions and trusted each other to get stuff done.

It took me some time to find the true value in working with a team. I always wanted to be a solo, auteur-type individual like Toby Fox or ConcernedApe. But working with great people has shown me that they have a lot to teach me and likewise, I (hopefully) have a lot to teach them. There is mutual gain.

Furthermore, working with teams and working by yourself is not mutually exclusive. You can still work on solo projects and take the learnings from your more experienced teammates with you.

## 5. Game jams are a means to an end, not an end themselves

Game jams are awesome. They provide a structured way to improve in game development, to find a community of like-minded people, and to put a piece of yourself out into the world that others can find joy in.

But whenever I finish a game jam, the same nagging question pops into my head: When am I going to finally work on a bigger project?

As much as I love game jams, I can’t pay for groceries with them.

This is my dilemma. Game jams are a means to something greater and eventually, that greater needs to take precedence.

Jon