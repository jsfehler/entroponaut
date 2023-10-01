default sc_name = "???"
define sc = DynamicCharacter("sc_name", kind=nvl, color="#9a89ff")

define rx = NVLCharacter("NEWBORN MAN", color="#b2d63f")

default s_name = "???"
define s = DynamicCharacter("s_name", kind=nvl, color="#00bcff")

define m = NVLCharacter("MARS", color="#ff2f4a")

# Flags
default examine_room = False
default examine_bathroom = False
default has_pyjamas_shirt = False
default use_toilet = False

# The game starts here.

label start:

    $ _quit_slot = "quitsave"

    "SPEED METAL VIMANA EPISODE 04 [[PROTOTYPE]"
    "CHAPTER 01. BOOTLEG"

    """
    Light floods in through a wide rectangular window.
    UV rays crawl along eggshell white pyjama pants, the only clothing of a man sprawled out on his back.
    In a single bed parallel to the window, he sleeps. A single white pillow cradles his head.
    The rays dance across his bare chest, up his face, and hit his eyes.
    His dreams, now only a distant, fading memory, release their grip entirely.

    His fingers and toes wiggle. His hands open and close.
    For a moment he is lost in the subtle sensation of his hand stretching.
    The cool, climate controlled air in the room tingles against his chest.

    He stares at the ceiling. The contrast of the dark room and bright sunlight is a brief amusement.
    His head drifts left and for a moment the window crosses his sight.
    Immediately, his head turns away.
    Not out of fear, but instinct.
    His mind retreats from the assault of new visual information.

    He stretches out along the bed, feels the edges of the bed, feels himself lying flat on the bed.
    With the understanding that he is in a bed and on his back, he makes the decision
    to turn to the right and lift his torso.
    Now sitting, he inhales and stretches his shoulders.
    """

    """
    These first minutes are dreamlike. No mental distractions.
    No plans for the day. No reminders of unfinished business.
    Like a newborn, he is satisfied with the novelty of sensory information.

    He stands, faces the window, and steps towards it.
    His finger, outstretched, slides down the window.
    Mild condensation is pushed away, leaving a clean streak in his finger's wake.
    He feels air flowing in and out of his nose with every breathe.
    These tactile sensations collect enough to give him pause.

    The mist of innocence disperses. Thoughts bubble up from his mind.
    Physical tough gives way to lucid questions:
    "What day is it? Weekend? Why did I fall asleep shirtless?
    When did I fall asleep? Are these pyjamas? Where am I?"

    His heart picks up a faster beat. Wonder has faded in favour
    of cold analysis. "What do you {i}mean{/i}, where am I?" He asks himself.

    He focuses, tightens his gaze, turns around and scans the room like a security camera.
    The area around him resembles a small hotel room.
    """

    jump inside_room

label inside_room:
    menu:
        "Examine the window.":
            passive "Examine the window."

            """
            A large body of water, birds flying in the sky, and what might be a city in the distance.
            None of it is familiar.

            He looks up and down, from every angle he can. The view of the ground eludes him.
            The structure he is inside is monumentally large and extends out of the water.
            It must be several kilometres long.
            The structure descend into the water, but as to how deep, he cannot tell.
            """
            jump inside_room

        "Examine the room.":
            passive "Examine the room."

            """
            The room is baked in a soft, golden glow.

            A bed, a window, an armchair facing towards the room.
            A door to a bathroom, and a door clearly labelled as the room's exit.

            The banal hospitality of the room is comforting, somewhat.
            Pleasant, inoffensive, bland.
            It could pass for a hotel room.

            Despite his best effort, the man won't remember when or how he got inside the room.
            This knowledge was never in his brain.
            """
            $ examine_room = True
            jump inside_room

        "Examine the bed.":
            passive "Examine the bed."
            """
            The bed is simple and functional. The sheets and pillow case
            are devoid of stains or signs of heavy use. They still carry the
            faint scent of laundry detergent.

            The bed, sheet, and pillow are average in every possible way.
            They elicit no emotional response, trigger no memories, and
            contain no thrilling revelations.

            It is an unopinionated bed. A mundane bed. A bed devoid of any history.

            In that much, the man and his bed are equals.
            """
            jump inside_room

        "Examine the armchair." if examine_room:
            passive "Examine the armchair."

            """
            The armchair is boxy, uncomplicated, and grey. It has only one point of interest:
            The top to his pyjamas. An eggshell white, long sleeved button-up shirt.

            The man lifts the shirt, holds it open, and slides it on. He leaves it unbuttoned.
            The fabric provides little protection from the elements, but does feel a bit warmer.
            """

            $ has_pyjamas_shirt = True
            jump inside_room

        "Enter the bathroom." if examine_room:
            passive "Enter the bathroom."

            """
            He walks inside and finds a small but functional area.
            Noticing the mirror above the sink, he creeps towards it as if worried something would jump out.

            The face that awaits him is unfamiliar, but familiar.
            He touches his cheek and confirms through the reflection that it is his face.
            He sticks out his tongue and confirm that it is his tongue.
            Greyish purple skin. Two flesh covered horns on each side of his forehead.
            Very long, lavender coloured hair.
            All normal enough, everything in the right place. Systems all green.

            Except for his beard.

            Too bushy, too heavy, and too rough, it's more like a loose bundle of straw.
            The man has no answer as to when his hair grew so long or when his beard grew so savage.
            Neither have style or shape, both have grown to their maximum length.

            He locks the middle finger of his left hand between the thumb and index finger
            of his right hand and cracks the finger.
            As if teaching himself, he interlocks his fingers, turns his hands backwards, and pushes out,
            cracking the knuckles in both hands all at once.
            The stretching, pressure, and sound dispel any remaining notions of a dream world.

            Having cracked, he will, with some self-admiration, stretch his arms up and flex his pectoral muscles.
            "This is nice. Very nice." He thinks, admiring himself just long enough
            for shame to replace narcissism.

            He stretches his tail and feel silly for having forgotten he had a tail.
            """

            """
            He looks down at himself.
            His body is not only adult, but youthful. It feels strong, in excellent physical health.

            He pulls the waistband of the pyjama pants and remarks to himself that
            everything seems pretty great down there. A familiar but unfamiliar body.
            Brand-new and nostalgic at the same time. He recalls no detail about this body.
            """

            """
            He exits back into the bedroom, satisfied, at least in the moment, by his physical state.
            """
            $ examine_bathroom = True

            jump inside_room

        "Examine the door on the wall opposite to the window. (Proceed.)" if examine_room:
            passive "Examine the door on the wall opposite to the window."

            """
            It's locked. The man retreats and sits down on the armchair.

            "Is this what amnesia feels like?" He thinks.
            An attempt to rationalize his current situation.

            He cannot remember any details about what happened directly before waking up.
            He rests his arm on the chair and massages the bridge of his nose.

            More questions seep out, darker now:
            Am I stuck in here? Am I being watched?
            Any weapons around here? Can you kill a man with a pillow?
            """
            jump first_convo


label first_convo:
    """
    Noise drifts into the room and captures the man's attention.

    He looks around and finds the source: A speaker above the door.
    It takes him a few seconds to realize the noise is a voice; someone is trying to communicate with him.
    The voice stops. Thirty seconds later, the voice repeats.
    Identical each time, he realizes that it's a recording.

    After hearing it several times, the man feels confident that he understood what was said.
    He wonders why it took any time at all to realize the noise was the spoken word, but pushes the concern aside.

    "Please respond once you understand this message." The message repeats a fourth time.
    A calm, smooth voice. It sounds neutral, giving no hint towards any particular emotion.
    """

    rx "Hello?"
    "He answers, uncomfortable with how unsteady he is in the use of his tongue."

    "The recording stops."

    sc "Hello to you too."
    "The same voice, but live now."

    sc "How do you feel?"

    "The man breathes in, feels a deep, slimy anxiety deep within, and exhales."

    rx "I'm good."

    """
    The man pushes that anxiety into a tiny, horrid little ball.
    He focuses on the conversation, what he can do in this moment, and the problems
    he can solve immediately.
    """

    rx "Could use a coffee."

    sc "Hmm."
    "That calm voice can't hide its amusement."
    sc "Okay. We've got coffee."
    sc "I'll unlock the door. We're-"

    """
    There is another, deeper voice heard through the speaker, but from a distance.
    The only part the man hears clearly is: "Don't yell ooga booga. He might be deranged."

    The calm voice responds to the intrusion.
    "Shush, both of you!" A stern rebuke to unknown troublemakers.
    """

    rx "Hello?"

    sc "Oops."
    "The calm voice is calm once more."

    sc "The door is unlocked. We're outside in the lounge. So... Whenever you're ready."

    jump examine_room


label examine_room:
    menu:
        "Use the toilet." if not use_toilet:
            passive "Use the toilet."

            "The man enters the bathroom and looms over the toilet."

            rx "Hey, are there cameras in the bathroom?"

            sc "...No."

            rx "Are you sure?"

            s "We've all seen you naked already!"
            "A new voice blares through the speakers. It's energetic and higher pitched, likely female."
            s "You weren't born in pyjamas!"

            """
            The man recognizes the voice, or at least it reminds him of a familiar one.
            He wants to say a name, it's on the tip of his tongue.
            The name is stuck in his throat like a muscle cramp.
            Without a name to put to the voice, he keeps any possible recognition to himself.
            """

            rx "How many people are there?"

            sc "You're in an observation room, we're not voyeurs. And there's four of us, counting you."

            s "What are you worried about? Everyone does it."

            """
            A spark ignites in the man's brain.
            Even over something as petty as whether or not one is being watched in the bathroom,
            he argues. On principle.
            """

            rx "On principle! Don't spy on people while they're- It's a sacred moment!"
            rx "A unique bonding time between man and throne!"

            s "It's a historical moment! It should be shared with the world!"

            rx "Historical? Just admit you want to watch me pee!"

            sc "Both of you, please. This is a non-issue."
            sc "Your bladder can't possibly be full right now."
            sc "Why are you both arguing?"

            """
            Because it's fun to argue valid points from ridiculous angles, of course.
            The voice is correct, however.
            """

            s "So are you going to pee or not?"

            rx "I'll hold it in."

            $ use_toilet = True
            jump examine_room

        "Exit the room. (Proceed.)":
            passive "Exit the room."

            """
            The man grasps the door's handle.
            Pulling downward, it rotates by fourty-five degrees.
            He pushes and the door opens.
            """

            jump exit_room

label exit_room:
    """
    The man steps halfway out before committing to an exit.
    He attempts to act casually: he doesn't want to appear overly cautious.
    He wants to retain an element of surprise; anything which may give him an edge
    if the calm voice ends up an unfriendly one.

    Beyond the room, a hallway. Cream-coloured walls lit by LED lamps in the ceiling.
    The façade of a hotel gives way to the mood of a clinic.
    The thought of being in a hospital, asylum, or rehab clinic enters his mind.
    Every potential answer is an uncomfortable fit.

    To his left, a dead end. To his right, a corner.

    He exits and walks right.
    He makes a deliberate effort to keep his arms relaxed and his legs steady.
    He won't want to make his heightened guard obvious.
    "If everything was fine, I wouldn't be an amnesiac getting led out of a locked room." he tells himself.

    He turns the corner and sees, as promised, the entrance to a lounge.

    The room is a semi-circle with a radius of about 5 meters.
    The ceiling about four meters tall.
    Large windows showcase a panorama of an ocean.
    Natural light washes in and gives the room a relaxed mood.

    Carpeted floors cushion his feet, each step muffled by the soft fibres.
    In the centre of the room, two armchairs and a brown fabric-upholstered couch sandwich a coffee table.
    Three individuals await him. Two on the couch, one in an armchair.

    In an armchair sits an androgynous man. His hair is long and straight, well maintained and styled.
    His skin is a very light cyan; he's quite pale.
    He wears a blue sweater, brown corduroy pants, and a white lab coat.
    On the couch, a cyan-skinned woman waves both arms rapidly as if seeing an old friend from across a street.
    Her sleeveless top gives her arms full mobility. Her frame is similar to that of an endurance athlete.
    """

    s "Hey! Over here!"

    """
    Next to her sits a tall, muscular, and terrifying man wearing a leather jacket.
    His armoured head, coloured a more saturated red than his skin,
    is floating above his stump of a neck.
    He waves a hand in greeting as if seeing an acquaintance at a bar.

    The man walks towards them.
    """

    m "Coffee machine's on the back wall."

    """
    The man stares at the two on the couch.
    The silence is uncomfortable.
    """

    rx "You look a lot like Mars."

    m "That's because I am."

    s "Who do I look like?"

    """
    He stares at the two. Their faces familiar, but only a distant recollection.
    As if meeting them for the first time in many years.
    He knows their names, he knows he knows them, but cannot remember how.
    """

    rx "Shiva?"

    $ s_name = "SHIVA"
    s "Yeah!"

    "She hops to her feet."

    s "See? He recognises us!"

    "She gets into his personal space, circling him like a scavenger bird."

    s "This is amazing!"

    rx "You're both-"
    rx "When did you-"

    """
    Too many thoughts and emotions flood the man's thoughts.
    Too many questions, too many possible answers.
    There is a traffic jam in the man's brain and the honking of horns
    is deafening.
    """

    rx "What's going on?"

    """
    Shiva explains in a haphazard manner.
    The man cannot focus on her words.

    Words like 'experimental', 'ethically dubious', 'quasi-legal', and 'utter-and-complete-nightmare-scenario';
    they all barely register as his eyes dart around the room and his breathing becomes shallow.
    The man becomes nauseous.
    """

    m "Hey, Shiva?"

    s "Yes?"
    "She turns back to Mars."

    m "He's not listening. You gave him an anxiety attack about 30 seconds ago."

    s "Oops."

    sc "Please, stop. Help him sit down and let me do the explaining."

    "Shiva puts her arm around the man and guides him into the other armchair."

    s "Hey, come on, down we go."

    "Once the man has sat down, she returns to the couch."

    sc "It's a bit much, I know."

    sc "My name is Doctor Amrita."
    $ sc_name = "DR. AMRITA"

    sc """
    It's good to see you awake, and it's normal to feel disoriented.

    You're doing great, all things considered.
    """

    """
    The doctor leans forward.
    """

    sc "How does your body feel?"

    """
    The man looks down at his hands.
    For the first time he notices the length of his finger nails.
    """

    jump ask_lounge

label ask_lounge:

    menu:
        "Could use a pair of nail scissors.":
            passive "Could use a pair of nail scissors."

            sc "We weren't really sure if you'd be ready for sharp objects."

            m "On the bright side, you didn't use those nails to claw your own face off."

            "Doctor Amrita turns to Mars."
            sc "Not helping, and happens more often than you might think."

            "Then, he turns back to the man."
            sc "You seem in full control over your body. That's a good sign."
            sc "After this we'll get you cleaned up."

            jump ask_lounge

        "How long was I asleep for?":
            passive "How long was I asleep for?"

            rx "Was I in a coma?"

            sc """
            If I said your body has only been asleep for twelve hours,
            what would your next guess be?
            """

            """
            The man thinks. Overgrown beard, overgrown hair. Woke up in a clinic.
            Not recovering from a coma.

            "Are you a hobo?" He wonders.
            """

            rx "Did you pick me up off the street? Or find me in a forest?"

            sc "We did pick you up, but not like that."

            jump ask_lounge

        "I don't like playing twenty questions. (Proceed.)":
            passive "I don't like playing twenty questions."

            rx "You're keeping secrets from me."

            sc """
            Easing you into the real world, that's all.

            Just trying not to overload you.
            """

            jump lounge_continue

label lounge_continue:

    """
    The man looks at the other three.
    A cyborg biker, an athlete, and a doctor.
    Two familiar, but all three strange.

    The man wonders why his body is even a topic of conversation.
    There's nothing he finds wrong with it.
    His health is fine. Beard aside, his body is the least of his concerns.
    Even the way they phrased it is strange: your body.

    Not you, but 'your body'.
    """

    rx "Why did you say 'your body'?"
    """
    "Is it a verbal tick? Or..." The man thinks.
    """

    sc "What do you mean?"

    rx "You're talking like it's clothing."

    sc """
    On purpose. Sorry, I'm not being obtuse.
    I can tell you but it's better if you can tell us.
    """

    rx "I'm pretty sure I have amnesia."

    sc "How old are you?"

    rx "Amnesia!"
    "The man doesn't yell, but the frustration in his voice is clear."

    sc "Gut feeling?"

    rx "I've had a long life."
    "The man has no real answer."

    sc "I'm sure you have, but how old does your body feel? How do you feel?"

    """
    Amrita looks at him with the same sort of expression
    a patient teacher has. That annoying, pained-yet-compassionate face which says
    "You can do it, I believe in you, but {i}please{/i} hurry up.
    You're boring the rest of the class."
    """

    rx "Did you de-age me, or something like that?"

    sc "Your body has only ever aged in one direction."

    """
    "Again with the 'your body' this and 'your body' that", the man thinks.
    As if it were something one buys in a store.

    "Oh." A solution forms in the man's head.
    """

    rx "Am I a clone?"

    sc """
    Your body's made from a brand new DNA mix.
    Nobody's ever had one like it.
    """

    """
    "Oh. {i}Fuck{/i}." The man thinks. "That's much worse."
    """

    rx "This isn't even close to my original body, is it?"

    sc "There we go."

    """The man leans back into the armchair and grips the chair's arms."""

    rx "Why am I in a new body?"

    sc """
    Because we didn't have the old one.
    We didn't have any of the original DNA.
    We couldn't even ask you what sort of body you'd like, since you were...
    """

    """
    The doctor's voice trails off for a moment.

    The man uses the moment to interupt. He'll say it. He wants to.
    """

    rx "Dead."

    sc "Yes."

    rx "What killed me?"

    sc "Unknown."

    """
    Mars stands up and walks towards the back of the room.

    Shiva had been sitting in silence these past few minutes.
    She had time to prepare for this conversation, but hadn't expected it
    to be so difficult to watch a friend claw back their understanding
    of the universe.
    """

    s """
    I'm pretty sure it wasn't a horrific death or anything!
    """

    rx "You don't know? And you lost my body? All of it?"

    sc "We didn't lose it. We never had it. Nobody has it. There is no DNA to recover."

    rx "Then how am I even-"
    """
    The man pauses. He has to stop, there are too many questions, he doesn't want to ramble.
    He wants the questions to count.
    """

    rx "Where's the DNA from?"

    "The doctor points to Shiva, then to Mars."

    sc "They said it's what you'd have wanted."
    sc "Genetically, you are their son."

    s "They grow up so fast."
    "Shiva pretends to sniffle."

    """
    Mars returns with a cup of coffee.
    """

    m "There's no fortune to inherit but there are several blood-feuds you could get in on."
    m "Coffee?"
    """Mars places a ceramic cup on the table in front of the man."""

    "The man looks at the two."
    rx "Really?"

    s "Hey, it's a good mix! Real potent stuff!"

    m "I'm just thankful we didn't have to change any diapers."

    "The man looks back towards the doctor."

    rx "Is this weird or not uncommon?"
    "It's weird, the man thinks. There is no possible way this cannot be at least a little weird."

    sc """
    These are exceptional circumstances, and, well, there weren't many options. But a little weird. Yes.
    """

    """
    The man sighs and leans forward.
    He doesn't sense any malicious intent from the other three.
    If only his memories were clearer, if only it didn't feel like each
    recollection was something dug up and dusted off from a pit.
    """

    rx "Is that why I have amnesia?"

    sc "No, and it's not amnesia."

    """
    Every answer this morning is too complicated, the man thinks.
    """

    rx "What is it?"

    sc "Exceptional circumstances."
    sc "You're in a fresh body. Not even a clone of your old body."
    sc "We had very little to work with. Not even a copy of your memories."

    """
    The man's eyes widen.
    """

    sc """
    For you, we had to reconstruct everything from scratch.
    We created various data points based on what you should know.
    Recreations based on what Shiva knew of your life.
    """

    sc """
    You have trouble remembering because memories aren't like video recordings.
    They're like data nodes.
    When we have someone's body and mapped memory records, it's plug and play.

    Depending when the record was made, there might be some confusion upon waking, but nothing drastic.
    Sometimes reconstructued memories are inserted to fill in gaps of information.
    """

    sc """
    However, we don't know exactly how they should be connected.
    If we tried to guess the mapping, the chance of incompatibility goes up.
    All we could really do was make sure you got the basics. You can walk and
    talk, for example.

    You'll have to piece things together yourself.
    Nobody else can do it.
    """

    s "If it makes you feel better, we threw in tons of useful stuff too."
    s """
    Like how to get stains out of a white shirt, how to fix an oil leak in a car, and how to make a shank out of toothpaste and toilet paper!
    """

    rx "Wow. Thanks Mom."

    rx "Does this happen often?"
    """If there was any comfort to be had, it would if he wasn't the only person this ever happened to."""

    sc "Oh my, no."
    sc """
    Partial memory patches happen, but a full reconstruction?
    Without any mapping? In a new body?
    I'm not even sure it's been done outside of experiments.
    The legality is questionable, even.
    The ethical implications alone would give most pause.
    You might be the first success ever.
    """

    """The man fell into a contemplative silence.
    He mulled over what all this information meant.
    A new body, fictionalized, obfuscated memories.
    Questions kept piling up, threatening to overwhelm him.
    """

    m "Fictional memories, but aren't they all?"

    rx "If the body is new, and the memories are fake-"

    sc "Reconstructed, not fake."

    rx "If this body is brand new and the memories are reconstructed, how do I know you didn't just make everything up?"
    rx "You could have just invented a whole fictional person."

    s "I mean technically-"

    sc "Ah. Let me."
    sc """
    Historically, trying to bring the dead back to life just by cloning them
    and writing memories into the new body has not ended well.
    Modern technology is much better. We've gotten very good at reviving people.

    But, it's a bit complicated to explain.
    At the very least, if you're not 'you', those nodes would not be connecting well.
    If you're not 'you', then each memory would feel like trying to shove a
    square peg into a round hole.

    If you're not 'you', then you're just some random soul being mashed into the shape of someone else.
    """

    sc "And even if you are, you're still being mashed into the shape of who your friends think you were."

    sc "...You're doing surprisingly great, all things considered."

    s "You're definitely you! You look a lot cooler now but you're still you!"

    rx "Cooler?"

    sc "You're not ugly, if it makes you feel better."

    "The man strokes his beard."
    rx "I look like I live on a boat and hunt whales."

    m "How do you know that isn't an upgrade?"

    rx "...Is it?"

    s "The beard is..."
    """Shiva exhales with a 'pfft' sound."""
    s "Big. You don't have to shave, but that's a sad old man beard."

    rx "Was I a sad old man?"

    s "Everyone gets sad sometimes."

    """
    She dodges the question. He can see it in her eyes.
    She doesn't want to say "A little bit, yes."

    Mars stands up and stretches his right shoulder.
    """

    m "You're alive. You know that for sure. We'll figure out the rest later."

    sc "Would you like to get changed, at least?"
    sc "Pyjamas aren't your style, I hope."

    """
    As Shiva pokes Mars and says "You've used that line before.", the man stands
    up and looks out upon the vastness of the ocean.

    He recalls wondering once, how much of his body he could change
    and still feel like himself. It seems the answer was over one hundred percent.

    Even that recollection is just a bootleg.
    """

    return
