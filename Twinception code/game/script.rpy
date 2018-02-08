
## The script of the game goes in this file.

## Declare characters used by this game. The color argument colorizes the name
## of the character.

define w = Character('?????')
define d = Character('Dante')
define m = Character('Mike')
define c = Character('Charlie')
define a = Character('Alex')
define p = Character('Profile:')

image bg intro = "images/BG/intro.png"
image bg cafe = "images/BG/cafe.png"
image bg bedroom = "images/BG/bedroom.png"
image bg brick = "images/BG/brick.png"

image dante default = "images/CH/Dante.png"
image mike default = "images/CH/Mike.png"
image mike magic = "images/CH/MagicMike.png"
image danteB default = "images/CH/DanteBlack.png"



python early:
    global dcFavor
    global maFavor
    global tempFavor
    global sync
    dcFavor = 0
    maFavor = 0
## The game starts here.

label start:



##intro
scene bg intro
"After years of failure on the dating scene, my sibling and I finally found ourselves opening the infamous DDM."
"DDM, also known as Double Date Me, a popular dating app made for twins, by twins, has been under fire in recent months for it’s “questionable” purposes. But as they say, desperate times call for desperate measures."
"Notorious for connecting pairs to “hot single twins” in their area and making a “sure fire” match in just 7 days, we were excited to see how our experience will turn out."
"We took every test and survey, hoping that the more thorough we were, the hotter the twins would be. Within minutes our inbox chimed with DDM’s “Hotties McHots” alerts, informing us that someone was digging our goods."

p "Magic Mike, You Know What’s Up ;)& dantesinferno.\n
Age: 23\n
Sign: Leo\n
Professions: Baristas\n"
p "About us: We’re just two guys looking for partners to share our lives with. We’re a little crazy, surprisingly different, but we make some damn good lattes, extra foamy ;)"

    
##Day1
scene bg cafe
##show dante default at left
##show mike default at right

"Blue Jazzberry, a newly opened café that supposedly has good music and even better
coffee. And the employees aren’t too hard on the eyes either. Despite the hype, we’ve never
made our way inside until now."
a "They are supposed to be here, right?"
c "{b}{i}sigh{/i}{/b} yeah Alex"
a "Right now? Like, are we too early, are we too late, or –"

show danteB default at left with easeinleft
w "I take it you guys are waiting for us?"
w "Thing1 and…. Thing2?"
c "Yep, that’s us. And you’re…"
hide danteB
show dante default at left
d "Dante. Also known as dantesinferno."
show mike default at right with easeinright
d "And this is my twin Mike, also known as Magic Mike, You Know What’s Up :).\n
Don’t ask."
a "Oh I’m asking."
m "What can I say? Channing Tatum is inspiring."
c "So Dante, according to your profile, you seem like you’re really into the outdoors. And
animals. What’s your favorite animal?"
d "Dogs. They’re very loyal and no matter what you do to them, they love
you unconditionally. Plus, they’re the easiest to train."


menu:
    d "What about you? Are you a dog person or a cat person?"

    "I think I am more of a cat person":
        c "You know; I think I’m more of a cat person. They’re pretty independent and don’t require as much attention as dogs do. Plus, they’re less maintenance"
        d "Cats huh? You know, people always say that you can tell a lot about a person by their preference in animals. And cats, they’re pretty boring."
    "I think I am more of a dog person":
        c "Yeah, I think I’m more of a dog person too. They’re just so compassionate and once you gain their trust, they love you unconditionally."
        d "They’re great right? They say you can learn a lot from a person’s preference in animals. For example, dog lovers are more outgoing, loving, and enjoy collars."
        python:
            ##syncAddC(checkTwo(sync),sync, maFavor)
            dcFavor = dcFavor + 1
label after_menu:

    c "I'm sorry what?"

d "*{b}laugh{/b}s* Nothing :)"
a "Is your brother always like this?"
m "No usually he’s more “Hah! I’ll rule the world and make you my slave! Mwuahahahahaha!”"
a "*{i}awkward laugh{/i}* Haha…hah…haaaa…that was a joke right?"
m "Yeah sure, if you want it to be."
a "Uhm…what are you interested in?"
menu:
    m "Did you not read our profiles?"

    "Of course I did, I was just wondering if there was more to you? It sounds like you’re into anime. Do you like any shows other than Sailor Moon?":
        m "(*smiles*) Heh, yeah there’s a few others. Recently I’ve been watching Cute High Earth Defense Club Love and Puella Magi Madoka Magica. I can really relate to Earth Defense Club but at the same time I just love the realness of Madoka."
        a "I’ve heard of Madoka but not of Cute High Earth Defense Club Love. I’ll have to check them out. Maybe we could watch them together?"
        python:
            ##syncAddA(checkTwo(sync),sync, dcFavor)
            maFavor = maFavor + 1
    "Well I mean, I skimmed it a little bit. You said something about liking flowers right?":
        a "Are you sure you aren’t just interested in Dante?"
        m "What? Dante? Nooooo. I’ve just never seen anime before. Maybe we could watch a few episodes together?"
label after_menu:

   "An hour passed before the four of them even realized it. They’d been so invested in their conversations that they didn’t even notice the time flying by. Charlie and Alex felt as though they’d known Dante and Mike for years."

d "Damn! Where did the time go?"
m "Mm? Has it been an hour already?"
c "Is something wrong?"
d "No, it’s just that we needed to start our shift about three minutes ago."
a "Isn’t that kind of a problem?"
m "Well we work here, and our boss hasn’t yelled at us to get behind the counter yet."
d "Yeah, we’re probably fine. It was really nice meeting you two."
m "I had a great time. Are we still on for that anime marathon?"
a "Absolutely! I’m just dying to see Cute High Earth Defense Club Love now!"

menu:
    d "It was great getting to know you Charlie. I feel like I can really just be myself around you, you know? I hope we can meet again soon."

    "No way you sick psycho!":
        c "I ain’t ever seeing you again"
        d "...."
        c "I’m just kidding. Of course I want to see you again!"
    "I know exactly what you mean. I can’t wait to see you again! ":
        python:
            ##syncAddC(checkTwo(sync),sync, maFavor)
            dcFavor = dcFavor + 1
label after_menu:

d "Great, Here’s my number. I’ll talk to you soon"

##Day2
scene bg bedroom

a "Have you spoken to Dante yet?"
c "Yeah we talked for a few hours before I went to sleep. He’s soooooo nice. 
Has Mike texted you yet?"
a "(*smiles*) A lil…."
c "Just a little??"
a "Okay a lot. He’s actually really talkative when he’s texting. 
(Phone chimes) Oh, speaking of Mike…."
c "Ohhh? What did he say?"
a "It’s a good morning text. He wants to know if I’ve woken up and eaten yet."
c "He sounds like a mother hen! That’s so cute! 
(Charlie’s phone chimes) Oh look, it’s Dante.
He wants to know if we can meet up today."
a "(Phone chimes) Mike just asked me the same question. I’m free today."
c "Same here. I’ll let him know."

scene bg cafe
show dante default at left
show mike default at right

"Blue Jazzberry was bustling by the time Alex and Charlie arrive. There was a steady flow of college students and adults in business wear entering and exiting the café. Despite the crowd, it was easy to find Dante and Mike."

c "Hey Dante!"
a "Mike, hi!"
d "Hey, sleep well?"
c "(blushes) Alright. You?"
d "Better with you in my dreams (winks)"
c "D-Dante!"
m "Alex, are you hungry?"
a "Maybe a little. I wasn’t really hungry earlier so I skipped breakfast."
m "Bagel or muffin?"
a "Sorry?"
m "Bagel or muffin? Simple question."

menu:

    "Bagel.":
        a "They’re the best with cream cheese"

    "Muffin.":
        a "I love blueberry muffins"

label after_menu:
    m "Bagel it is. I’ll be right back."

c "You know Dante, I know so much about you, but you don’t really know a lot about me."

hide mike default

menu:
    d "(Surprised) Sure I do! Your name is Charlie, you like dogs, you’re friendly and outgoing, you have a twin named Alex and you two get along very well. Your parents are divorced and you live with your mother. You and Alex still sleep in a bunk bed and you like to take morning runs through the park."

    "(Laughs) Where’d you get that info?":
        d "(Laughs) I might’ve looked you up on Facebook last night. I hope you don’t mind."
        c "Wow, I forgot all about Facebook! I haven’t been on that thing for the past few months. In fact, I thought I’d deleted it."
        d "Well nothing is ever actually deleted off the internet. Anyways, I noticed that you and Alex like some local indie bands and I was wondering if you two wanted to come back to Blue Jazz later. We’re having live music tonight."
        python:
            ##syncAddA(checkTwo(sync),sync, dcFavor)
            dcFavor = dcFavor + 1
    "WHAT THE FUCKITY FUCK FUCK HOW DO YOU KNOW THAT??!?!?!":
        d "Jesus, don’t act so paranoid. We talked for hours yesterday. You told me that stuff. Like how you hate still bunking with Alex but you feel lonely when you sleep by yourself"
        c "You’re right. I’m sorry. I probably just forgot about that."
        d "It’s okay, it happens. Anyways, I remembered that you and Alex like some local indie bands and I was wondering if you two wanted to come back to Blue Jazz later. We’re having live music tonight."
label after_menu:
     c "I’d love that!"

show mike default at right

m "Here you go"
a "Thank you. You didn’t have to do that. I can pay –"
m "Don’t worry about it. It’s my treat. Next time, bagels are on you."
a "(blushes) Next time?"


menu:
    m "(Confused) Was I wrong in assuming there’d be a next time?"

    "Um yeah buddy! You can’t just go around assuming things about others!":
        m "Well excuse me then. Maybe I should just not assume and also not talk to you."
        a "I didn’t mean it like that. Let’s just see how things go today before we make any more plans."
        m " Hmm..."
    "No! No! It’s just…you’re very upfront about what you’re thinking. I like that. I don’t feel like I have to play any guessing games with you.":
        m "(Smiles) It’s so much easier talking to you than it is talking to anyone else. I like that I can be myself around you and I would really like to be able to talk to you more, if that’s okay. "
        a "(darker blush) I’d like that. Maybe we can meet up again tomorrow? I’ll buy the bagels this time around."
        m "(Smiles) Sounds like a plan."
        python:
            ##syncAddC(checkTwo(sync),sync, maFavor)
            maFavor = maFavor + 1
label after_menu:
c "Hey Alex!"

a "Yeah?"
c "Dante just told me that this café is going to be having live music tonight. You in?"
a "Mike, are you going to go?"
m "I’m working tonight, but you’re welcomed to hang out by the bar and keep me company."
a "I guess someone has to keep you sane while you deal with caffeine obsessed hipsters."
d "Great! Sounds like a plan! Let’s meet back here around eight."

"The four met back up"

##Day3
scene bg bedroom

c "Charlie is awoken by a gentle shake."
show dante default at left
d "Sleep well?"
c "AHHHH!!!!!!"
c "How did you get in here?!"
d "You should really lock your window at night."
c "It WAS locked!!"
d "They should really make windows brick-proof then."

"(Charlie’s heart was pounding in fear. And maybe a little bit of…excitement??
Charlie listened for signs of wakefulness from Alex, who was asleep up above Charlie’s bed. No luck)"

c "Dante, what on earth are you doing here?"
d "I need to talk to you about something, but I can’t have anyone interrupting us. It’s a very special talk, and very important. I need you to be quiet though, because I would hate to harm Alex, should your twin wake up. Understood?"
"Charlie nodded."
d "Good! Okay then!"

hide dante default

"A few hours later, Alex wakes up, feeling refreshed and full of vigor."
a "Mornin’ Charlie!"
"Silence."
a "(Huh, I guess Charlie isn’t awake right now. Odd)"
"Alex jumps down from the bunk and turns to see Charlie’s disheveled bed."
a "(Even weirder!)"
a "Charlie? Chaaaaaarlie!!"
"Alex tried texting but got no response. "
"Next Alex called Charlie and was met with the abrupt “I’m sorry but…”"
"Terrified, Alex hung up."
"(Maybe Dante knows where Charlie is. Maybe they’re together)"
"Alex let out a growl of frustration."
a "If only I had Dante’s number!"
a "Oh! Mike!"
"Fingers flying, Alex quickly dialed Mike’s number."
m "Morning beautiful. How – "
a "Mike! Where’s Dante?"
m "Dante? Why do you need to know where he is?"
a "It’s urgent. Can you tell me? I don’t have his number."
m "Why don’t you just ask Charlie for it."


if ((maFavor == 1) or (dcFavor < 2)):
   jump Bad_End
if ((maFavor >= 1) and (dcFavor >= 2)):
   jump Good_End

label Bad_End:
a "I would if I could, but Charlie is missing! I was hoping Dante would know where Charlie is!"
m "Riiight. Sure. You two are practically attached at the hip. As if Charlie would do anything without you. You’re just trying to get Dante’s number. Trust me, I’ve been through this before. It’s easier if you’re honest."
a "Mike! Can you please give me Dante’s number?"
"There was a long pause as Mike thought about it."
m "Hmm, no. Goodbye."
"Before Alex could say anything else, Mike hung up."
"GAME OVER -- BAD END"
jump END_GAME

label Good_End:
a "I would if I could but Charlie is missing! I was hoping Dante would know where Charlie is!!"
m "Shit. Charlie’s missing? Fuck. I think I might know where they are."
a "Are you even sure that they’re together?"
m "Oh I’m positive. Meet me at Blue Jazz in twenty minutes."

scene bg cafe
show mike default at right

"Mike is waiting outside as Alex rushes up to meet him."
a "Where do you think Charlie is?"
m "Where do you think Charlie is?"

"Alex followed Mike as he walked around the café and headed straight for a warehouse that was completely hidden from view when standing in front of Blue Jazzberry."

scene bg brick
show mike default at right

"He stopped abruptly in front of the front entrance."
a "What are you waiting for? Let’s go!"
m "Give me a minute."
"Mike turns to face Alex, his face set, jaw clenched."
m "PRETTY"
m "MAGICAL"
m "CRYSTAL"
m "PURITY"
m "TRANSFORM MEEEEEEE!!!!!"

"A series of bright flashing lights flickered before Alex’s eyes. Mike became enveloped in their glowing white brilliance. His body moved in a fluid and well-choreographed dance as he transformed from Mike into…."

m "MAGICAL CRYSTAL PURITY, LADY VIRTUEEEEEEE!!!!!!!!"

"The glowing light faded, leaving behind only Mike, who looked like a stunningly beautiful magical girl."

show mike magic at right

m "Okay, I’m ready!"
"Alex fell to the ground with a heavy thud."

menu:
    m "Alex, are you alright?"

    "Uh –":
        a " I know you’re into cosplay and all, but isn’t this going too far...?"
    "Woah!":
        a "You’re a magical girl – er, I mean boy! Everything makes sense now!!"
label after_menu:
    m "Only people with the purest of hearts can do this. I was given a crystal with magical powers when I was a little boy and ever since then I’ve been LADY VIRTUE, DEFENDER OF THE MAGICAL CRYSTALS OF PURITY AND PROTECTOR OF ALL PRETTY MAGICALLY GIRLS!"

a "Okay…okay. And Dante?"
m "Nah, Dante’s just messed up. Which is why we should probably go save Charlie now."
a "Right. Um…lead the way…Lady Virtue…?"
m "Yeah. But next time say it with more gusto. Put more feeling into it."
"The two ran inside.
While they’d expected to see a dire situation, upon entering the warehouse, they found Charlie and Dante enjoying a lovely brunch together under a broken skylight."
a "Charlie!"

"Charlie looked up, shocked to see Alex in the warehouse. Dante had been so positive that it was secluded and that they’d be completely alone. Initially Charlie was wary of going anywhere alone with Dante. All throughout Charlie’s life, Alex was always there. They rarely did anything alone. Charlie never experienced the thrill of being alone before now. It was kind of exciting."
c "Alex! What are you doing here?"
a "You weren’t there when I woke up. I was worried so I called Mike and he took me here."
"Charlie turned to Mike."
c "How did you – WOAH!"
"Charlie jumped back in shock"
"Charlie almost didn’t even recognize Mike, in his magical boy outfit."
c "Jeez Mike, I know you’re into cosplay and all, but isn’t this going too far…?"

show dante default at left

"Dante laughed."
d "Yeah, you’d think so, but really isn’t the most shocking thing he’s done before. Hello Lady Virtue. I haven’t seen you in a while."
m " Dante, what are you doing?"
d "What does it look like? Charlie and I are having a little brunch together. See, Charlie was very worried about how I knew so many personal details, so I figured I’d explain over a nice little meal."
a "But I didn’t hear the doorbell ring."
d "You’d be amazed at what you can sleep through, Alex."
c "That’s true! I always knew you were a heavy sleeper, but the fact that you didn’t wake up even after Dante hurled a brick through our window is ridiculous!"
a "You threw a brick through our window??? And Charlie, you’re okay with that?"
c "Not at first, silly. But once Dante and I were alone, he explained everything to me. See, Dante’s just suuuuper insecure and he was just worried about how I felt towards him."
"Dante flashed them a chilling grin."
c "He’s really quite a sweetie. We were just talking about our past pets. Dante’s had three dogs in the past. From the sounds of them, they were all lovely! I think their names were Michelle, Chad, and…oh! Ester."
a "Who the heck names their dogs Michelle, Chad, and Ester?"
"Mike made a pained expression."
m "Erm…someone who never actually had “traditional” pets."
a "What….oooooooooh."
c "Guys why don’t you join us!"
a "Should I…?"
m "It can wait until after brunch."
a "…you’re right. It can wait."
"GOOD END"

label END_GAME:
## This ends the game.

return
