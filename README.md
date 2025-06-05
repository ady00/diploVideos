hi this is my super janky script for scraping through the LOADS of content filmed for wtp diplomacy :P

to run the script run ```python3 scraper.py``` (make sur eyou have python3 installed, vscode is also preferable to have)
to install ALL the files make sure you ```git clone``` this (there should be instructions on how to download a repo on google its super easy)

you can change the search parameters via the ```keywords_to_search``` parameter in the scraper.py file
currently, it is set to all mentions of russia, but that can be changed to any keyword

the program will return any/all mentions of that word via the google transcript feature (which is also kinda janky, but wayyy easier than having to sift through hours of footage)

example

```python3 scraper.py``` (with the current keywords_to_search) would return this:

```
ItalyOne – 1:57 – strong against Russia I'm fully fine to let that play out before like moving in there at all Mhm I think if things work – https://youtu.be/HExNim2Ul0A?t=1m57s
ItalyOne – 2:16 – enough people alive to take out Russia before we have to deal with it because – https://youtu.be/HExNim2Ul0A?t=2m16s
ItalyOne – 2:54 – think that I have enough I think they're too invested in Russia to worry so far – https://youtu.be/HExNim2Ul0A?t=2m54s
ItalyOne – 3:34 – Russia has like a border with that's like the end of the game So we just need to get like somewhere and then we can – https://youtu.be/HExNim2Ul0A?t=3m34s
...
GermanyOne – 1:04 – at the beginning russia told us that turkey russia and austria were all going to – https://youtu.be/qhwbHH_gUs4?t=1m4s
GermanyOne – 2:06 – other than like russia hasn't lied i think other than russia i – https://youtu.be/qhwbHH_gUs4?t=2m6s
GermanyOne – 2:44 – of lied to both france and russia last turn but – https://youtu.be/qhwbHH_gUs4?t=2m44s
GermanyOne – 3:20 – more on the north side west side back into russia where would you go – https://youtu.be/qhwbHH_gUs4?t=3m20s
GermanyOne – 3:31 – north because russia is threatening us the most right now i think – https://youtu.be/qhwbHH_gUs4?t=3m31s
...
TurkeyOne – 2:06 – with Russia and that would pit us against Austria and uh Italy or our – https://youtu.be/06IBczNjSIk?t=2m6s
TurkeyOne – 2:12 – other option was to ally with Austria and Italy and we would go against Russia – https://youtu.be/06IBczNjSIk?t=2m12s
TurkeyOne – 2:30 – seriously as Russia had also been offering uh Austria an option to – https://youtu.be/06IBczNjSIk?t=2m30s
TurkeyOne – 2:56 – correct choice now that you have Russia on the ropes – https://youtu.be/06IBczNjSIk?t=2m56s
TurkeyOne – 3:02 – i definitely think Austria going against Austria would have been the easier choice um because Russia brought up fair – https://youtu.be/06IBczNjSIk?t=3m2s
TurkeyOne – 3:17 – us in the short term we would gain a lot of land initially but the second that happened being allied with Russia didn't – https://youtu.be/06IBczNjSIk?t=3m17s
TurkeyOne – 3:29 – working with Austria was the smartest plan there but doesn't the same logic apply but for Russia once Russia is gone – https://youtu.be/06IBczNjSIk?t=3m29s
... [add in a lot more results here from other videos, you get the point]
```

Results are timestammped with the timestamp link as well as the video (TurkeyOne for instance points to Turkey Week 1 interview). 

email/dm me if any qeustions :D :D 
