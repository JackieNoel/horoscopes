# import random,
# then put 3-4 horoscope messages in each array so that you can
# return a random array index to
# add variation to what is returned for the user's horoscope
import random


def horoscopes(input):
    num = random.randint(0, 2)
    Capricornus = [
        'Though youre one of the more reserved members of the zodiac, intimacy wont feel so scary this morning, thanks to a sweet connection between the Leo moon and Venus. These vibes are perfect for intimate exchanges and letting down guards, especially when it comes to family members or housemates. An auspicious energy will surround you mid-morning when Luna enters Virgo, activating the sector of your chart that governs spirituality and luck. Unfortunately, a harsh opposition between Mars and Saturn could cause you to second guess your instincts, but try not to let an overly practical disposition block your intuition.',
        'Excuse me? A stressful standoff between brusque Mars and your ruling planet, strict Saturn, spans your communication houses today. Although you might be excited to share your bold vision, a cynic could toss a wet blanket on your aspirations. Are they just baiting you or do they have a solid argument? Dont throw in the towel over a momentary challenge. Look at this as a chance to do your homework and shore up your plan. Youll be even more prepared when you finally press the launch button.',
        'Theres nothing quite so satisfying as a job well done. Remind yourself of that if your enthusiasm starts to wane in the face of what seems like a mountain of details all clamoring for your attention. Why not hand some of those tasks over to a trustworthy associate? Tell them the results you need and the timeline youre on. Just remember that once you do, its strictly hands off. Really. Youre in good hands, so go ahead and relax.']

    Aquarius = ['Though youre one of the more reserved members of the zodiac, intimacy wont feel so scary this morning, thanks to a sweet connection between the Leo moon and Venus. These vibes are perfect for intimate exchanges and letting down guards, especially when it comes to family members or housemates. An auspicious energy will surround you mid-morning when Luna enters Virgo, activating the sector of your chart that governs spirituality and luck. Unfortunately, a harsh opposition between Mars and Saturn could cause you to second guess your instincts, but try not to let an overly practical disposition block your intuition.',
                'The creativity you need to unleash today wont come as quickly as youd like. Instead of a gushing torrent of brilliant ideas, youll probably only get a trickle of half-baked ones. You cant let this discourage you, though. To knock loose the plug in your pipes, get outside and walk around. Fresh air will revive your gray matter, and the outside world will encourage you to think outside of the box. Natural beauty is an effective tool to jump-start to any stalled day, so remember that in the future.',
                'You’ve had the pedal to the metal lately under the assumption that there just aren’t enough hours in the day to get it all done. Although you do have a lot on your plate, you could be running yourself ragged because of internal—not external—pressure. Today’s balancing Libra moon in your vision realm is coaxing you to recalibrate. Shift your perspective and recognize that you’ll get through your to-do list at some point, Aquarius. And that victory will feel much sweeter if you’re not stressed to the max when you cross the finish line!']

    Pisces = ['Give your body some extra love when you wake up, dear Pisces, as the Leo moon joins forces with harmonious Venus. This celestial exchange will bring extra grace to your morning routine, helping you float into the office with ease. Your focus may shift to matters of the heart when Luna migrates into Virgo, pushing you to prioritize relationships where you feel the most needed and valued. Just remember not to upset your own balance catering to someone elses needs, as Mars and Saturn face off overhead, threatening to disrupt the tranquil vibes the day started off with.',
              'The more you try to zero in on the work that’s in front of you today, the less you’ll be able to focus on it! Chalk it up to the flirtatious Libra moon in your libidinous eighth house all day. In a new relationship? You could feel superglued to your sweetie, thanks to oxytocin, the “cuddle chemical”. Keep trying to concentrate on the task at hand. It may help to narrow your lens to one small step at a time so you don’t swerve back into the daydreaming lane.',
              'Getting overwhelmed simply isnt going to be a concern for you today. Your mind is sharp, and you can handle anything that comes your way. From overbearing teachers to micromanaging bosses, the people youll be dealing with wont be able to frustrate you. You might have no clue why this sudden calmness has come over you, but that doesnt matter. Just enjoy it! This is a great day to take a big social risk. Youre feeling confident, and it shows.']

    Aries = ['The Leo moon cozies up with sweet Venus this morning, dear Aries, putting you in a playful mood thats perfect for celebrating your relationships. New opportunities may fall in your lap when the Nodes of Fate become active, though your balance may take a temporary hit if you decide to take on more work or goals. Youll sense a shift mid-morning when Luna migrates into Virgo, providing you with the organization needed to thrive around the office. However, youll want to be on guard for hidden obstacles when Mars faces off with Saturn, taking care to double-check your projects.',
             'Getting into an argument is a choice, and its one you dont have to make if you dont want to. If someone pushes your buttons or annoys you or is just plain rude to you, you can turn the other cheek if you really want to. If you dont, then make sure your words are objective. Dont hit below the belt. Cheap shots demean you far more than they demean the person you are mad at. Dont let them get the better of you.', ]

    Taurus = ['The Leo moon cozies up with your planetary ruler, Venus, this morning, bringing a sense of fullness and peace to your heart. Your home will feel particularly warm and comforting, though these dreamy vibes could make it difficult to crawl out from under the covers. Luckily, youll find the motivation to get moving once Luna migrates into efficient Virgo, putting you in the mood to socialize and pursue special interests. This luminary placement can also bring organization to your artistic pursuits, nudging you to return to any passion projects that have been collecting dust. Unfortunately, an opposition between Mars and Saturn could bring forth distraction, especially when it comes to screens.', ]

    Gemini = ['Your words will carry a certain level of poetry this morning, dearest Gemini, thanks to a cosmic union between the Leo moon and sweet Venus. People will be eager to connect with you, and there may be some extra flirting as the hours unfold. Youll feel a shift when Luna migrates into Virgo and your solar fourth house, shifting your priorities to domestic affairs and familial ties. If any chores have built up within your space, this luminary placement can help you find the motivation to tidy up. Watch out for emotional blocks within yourself and others later tonight when the moon and Mars face off with stoic Saturn.', ]

    Cancer = ['Beauty wont be hard to find as the Leo moon cozies up with Venus this morning, dear Cancer, coating your world with a sweetness that will leave you appreciating each moment. Consider going out on a limb to achieve success when the Nodes of Fate become active, promising to open new doors. Youll sense a shift mid-morning when Luna migrates into Virgo, putting you in a more practical and information-driven headspace. If any books need reading or topics youve been meaning to research, use this energy to direct your focus accordingly. Just be sure to stay grounded in the texts you seek as Mars and Saturn face off overhead.', ]

    Leo = ['Listen to your heart as the moon and Venus join forces in your sign, sweet Lion, providing you with heightened intuition and plenty of grace. Meanwhile, the North Node becomes active in your house of spirituality, ushering you into the future with signs and synchronicities. Youll sense a shift mid-morning when Luna enters Virgo, putting you in a grounded and efficient headspace. Use this energy to get caught up on any tasks that need handling before the workweek ends, and consider touching base with your bodys needs. Watch out for stagnant vibes when the moon and Mars oppose Saturn later tonight, and try not to let stubbornness get in the way of harmony.', ]

    Virgo = ['You should wake up with a deep sense of peace, dearest Virgo, as the Leo moon and Venus join forces in your solar twelfth house. Though there may be personal grief that still needs unpacking, this cosmic climate asks you to embrace warmth and love, giving your heart a chance to feel supported. Opportunities for transformation will come to fruition when the Nodes of Fate become active, so try to be open to change. Your spirits will lift mid-morning when the moon enters your sign, giving you permission to take the initiative while prioritizing your own needs for a change.', ]

    Libra = ['Youll walk with more than your fair share of social graces today, dearest Libra, as the Leo moon and Venus join forces in your solar eleventh house. Lean into these vibes by allowing your charm to shine through, especially when moving through public spaces. A nostalgic energy may take hold when the Nodes of Fate become active, nudging you to revisit pleasant memories. Youll sense a shift mid-morning when Luna migrates into Virgo, putting you in a more private mood thats perfect for taking care of business behind the scenes. Just try not to get frustrated if you dont check everything off your to-do list, as an opposition between Mars and Saturn threatens to slow us all down.', ]

    Scorpius = ['People will admire your professional yet compassionate nature this morning, dearest Scorpio, thanks to a cosmic union between the Leo moon and Venus. These vibes can also help you manifest new levels of success, especially when you follow your heart and intuition. Youll sense a shift mid-morning when Luna makes her debut into Virgo, promoting themes around teamwork while nudging you to reach out to community. If its been a while since you met your friends or colleagues for an outing after work, now might be a good day to do so. Just dont be offended if not everyone on your guest list shows up, as an opposition between Mars and Saturn may cause feet to drag.', ]

    Sagittarius = ['Youll be a darling of the universe as the Leo moon and Venus align, dear Sagittarius, supercharging the sector of your chart that governs luck and spirituality. Move with an open and generous heart right now, as the universe will eagerly reward kindness and good deeds. However, your composure will shift mid-morning when Luna migrates into Virgo, putting you in a more guarded, work-oriented headspace. These vibes are perfect for creating reasonable boundaries, especially if others have been taking advantage of your benevolence. Meanwhile, Mars and Saturn face off in our skies, threatening to trigger mood swings if you dont take care to recharge.', ]
    if input == "Capricorn" or 'capricorn':
        return f'-------- Daily Horoscope: -------- {Capricornus[num]}'
    if input == "Aquarius" or 'aquarius':
        return f'-------- Daily Horoscope: -------- {Aquarius[num]}'
    if input == "Pisces" or 'pisces':
        return f'-------- Daily Horoscope: -------- {Pisces[num]}'
    if input == "Aries" or 'aries':
        return f'-------- Daily Horoscope: -------- {Aries[num]}'
    if input == "Taurus" or 'taurus':
        return f'-------- Daily Horoscope: -------- {Taurus[num]}'
    if input == "Gemini" or 'gemini':
        return f'-------- Daily Horoscope: -------- {Gemini[num]}'
    if input == "Cancer" or 'cancer':
        return f'-------- Daily Horoscope: -------- {Cancer[num]}'
    if input == "Leo" or 'leo':
        return f'-------- Daily Horoscope: -------- {Leo[num]}'
    if input == "Virgo" or 'virgo':
        return f'-------- Daily Horoscope: -------- {Virgo[num]}'
    if input == "Libra" or 'libra':
        return f'-------- Daily Horoscope: -------- {Libra[num]}'
    if input == "Scorpius" or 'scorpius':
        return f'-------- Daily Horoscope: -------- {Scorpius[num]}'
    if input == "Sagittarius" or 'sagittarius':
        return f'-------- Daily Horoscope: -------- {Sagittarius[num]}'


print(horoscopes('Capricorn'))
