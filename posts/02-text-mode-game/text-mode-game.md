---
link: blog/making-a-text-mode-game.html
title: Making a TEXT-MODE game
date: March 24 2022
---
<h1 style="margin-bottom: 0px;">Making a TEXT-MODE game</h1>
<h3 style="color: #97a9c4; margin-top: 0px;">March 24 2022</h3>

In the beginning of this month, I participated in my first 7-day rogue-like jam ([7DRL](https://itch.io/jam/7drl-challenge-2022) for short) and released [Echo Chamber](https://jontopielski.itch.io/echo-chamber), a turn-based game where you combo different spells while traversing a dungeon. [Mafgar](https://twitter.com/mafgar_online) assisted with all things audio and I used a tile set called [mrmotext](https://mrmotarius.itch.io/mrmotext) by [Mrmo Tarius](https://mrmotarius.itch.io/).

<div style="text-align: center;">
    <img class="artPanel" src="posts/02-text-mode-game/echo-chamber.gif" width="50%">
</div>

This was the first time I made a game using a style known as [text-mode](http://polyducks.co.uk/what-is-textmode/). The idea is that you have a fixed tile set and you can only use those tiles to compose the graphics on the screen. While this may seem restrictive at first, it allows for creativity in deciding what tiles should be used to effectively depict something.

_Disclaimer - I didn’t stick to just one tile set for Echo Chamber (for example, I did all the characters myself), but the majority of the tiles were from one single tile set._

Let’s say I wanted to draw a 64x64 wizard using the text-mode style. I start with a base set of tiles, such as this one from the Commodore-64.

<div style="text-align: center;">
    <img class="artPanel" src="posts/02-text-mode-game/text-mode-tiles.png" width="50%">
</div>

I take this tile set and import it into my preferred tile set editor. I personally use [Godot](https://godotengine.org/) since I’m already familiar with the workflow. It’s easy to rotate, flip, and copy tiles.

For this example, I’m using the tile set, [mrmotext](https://mrmotarius.itch.io/mrmotext) by [Mrmo Tarius](https://mrmotarius.itch.io/), which is also the tile set I used in the game.

I create my image by drawing tiles one at a time, flipping and rotating them as needed.

<div style="text-align: center;">
    <img class="artPanel" src="posts/02-text-mode-game/mrmo-text-godot.png" width="50%">
</div>

One of the drawbacks of using Godot to draw an image with tiles is that you cannot color tiles individually. So what I do is take a screenshot of the image and then paste it into Aseprite.

<div style="text-align: center;">
    <div style="display: inline-block;">
        <img class="artPanel" src="posts/02-text-mode-game/white-wizard.png" height="200px" width="200px">
    </div>
    <div style="display: inline-block;">
        <img class="artPanel" src="posts/02-text-mode-game/colored-wizard.png" height="200px" width="200px">
    </div>
</div>

Once in Aseprite, I apply a grid and then manually color in each tile.

This was my approach for most of the graphics in the game. I should mention that there are dedicated tools for this art style like [Playscii](http://vectorpoem.com/playscii/) and [lvllvl](https://lvllvl.com/), which have more support for things like coloring in individual tiles.

<div style="text-align: center;">
    <div style="display: inline-block;">
        <img class="artPanel" src="posts/02-text-mode-game/echo-chamber-menu.png" height="250px" width="225px">
    </div>
    <div style="display: inline-block;">
        <img class="artPanel" src="posts/02-text-mode-game/echo-chamber-in-game.png" height="250px" width="225px">
    </div>
    <div style="display: inline-block;">
        <img class="artPanel" src="posts/02-text-mode-game/echo-chamber-title.png" height="250px" width="225px">
    </div>
</div>

I enjoyed working within this art style for several reasons. For one, using tiles naturally looks good in video games, which have historically been tile based due to limitations in hardware. Using tiles today even though you don’t have to can be considered an artistic choice that also has a nostalgic feel to it.

Text-mode specifically is borne of limitations based on the tiles that you have. You won’t always be able to find the “perfect” tile for the corner or edge that you need, so you use something close and that naturally creates an imperfect look. But the sum of these slight imperfections creates its own unique look.

Another advantage of the text-mode style is that someone who isn’t great at pixel art can still create something interesting looking. My pixel art ability isn’t the best, but by using an existing tile set to depict things, I can be creative within that tile set without being limited by my pixel art skills.

One of the downsides of the text-mode style is that it can be time consuming to create each piece. Particularly, coloring in individual tiles takes lots of time. I was fortunate to work in a relatively low resolution, but if I worked on a game that was much larger, I would imagine that creating lots of assets would take a long time.

Despite this, I would absolutely work in text-mode again in the future. In fact, I feel inspired to create my own unique text-mode tile set for a specific game. I think that would be a really cool way to inject the personality of that game into its tile set because the tile set would be designed around the game’s particular aesthetic, similar to creating a unique font for a specific game.

## Favorite Things
**Book - Steal Like an Artist**. Ironically, I stole this book because my friend sent me a pdf of it. The summary - as an artist, steal the things you like unabashedly. Every great artist was influenced by those that came before them, so you should do the same. Every great research paper cites other papers. Every great game has taken pieces of games that came before it.

**Game - Anodyne 2**. A beautiful game that ties in both 2d zelda-like dungeon crawling with nostalgic PS1 third person exploration. The thing that caught me most off guard was the Earthbound level of humor in the dialogue. It has it all.

**Location - Antigua, Guatemala**. In an impulse decision, I spent a week in Antigua, Guatemala learning Spanish and it was the highlight of my travels for the last month. A beautiful city surrounded by volcanoes and filled with some of the kindest people I have met.

This blog will continue to change form as I figure out the best way that I’d like to go about it. Hope you have a wonderful day wherever you are.

Jon