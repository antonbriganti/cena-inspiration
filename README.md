# cena-inspiration
script that generates inspirational wallpapers using John Cena's tweets

## pitch
```
Whenever someone hurts us, it is an opportunity to practice forgiveness. - @JohnCena, August 9 2021
```
John Cena is a pretty inspirational guy. his twitter feed is full of wonderful inspirational quotes, the type of stuff you'd see superimposed in italic text on pictures with beautiful scenery. I could make them myself, or I could find a way to automate the experience. what's more heartfelt than automated inspiration?

## implementation
language wise, I'm going to use Python. path of least resistance. 

I see this as three different parts that come together to make art. the twitter scraper, the inspirational image finder, and the image renderer. 

### twitter scraper 
the goal here is to make something that does the scraping of the `@JohnCena` feed. I can just use a library that someone else has made, because why reinvent the wheel? 

the hard part here is filtering out things that aren't inspirational. John Cena is a busy man, with a lot of things to promote, and so his Twitter account isn't just inspiration. so how do we get just the sauce, so to speak? things that are ads generally have either some kind of hashtag in them or they are a quote retweet of something. so if we filter those out, we should be all good. 

and hey, even if the filter isn't perfect and an ad slips through, that's going to be funny so it's a win either way.

### inspirational image finder
it is what it sounds like, something that finds amazing backgrounds to use for the quotes. I could download a lot and then package all together, but why do that when I can overcomplicate it?

not sure how this is going to work just yet, I just kinda hope Unsplash or something similar has an API I can use.

### image renderer
short and sweet, something that puts text onto an image. needs to make sure that text isn't too big or gets cropped outside the frame of the image.