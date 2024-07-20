import pyttsx3
# engine = pyttsx3.init()
# engine.say("I will speak this text")
# engine.runAndWait()

# import pyttsx3
# pyttsx3.speak("I will speak this text")



# import pyttsx3
# engine = pyttsx3.init() # object creation

# """ RATE"""
# rate = engine.getProperty('rate')   # getting details of current speaking rate
# engine.setProperty('rate', 150)     # setting up new voice rate


# """VOLUME"""
# volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
# engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1

# """VOICE"""
# voices = engine.getProperty('voices')       #getting details of current voice
# # engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
# engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female

# engine.say("Tao là Tùng béo")
# engine.say('Pho len ti lô Rô nan đô siu!')
# engine.runAndWait()
# engine.stop()


# """Saving Voice to a file"""
# # On linux make sure that 'espeak' and 'ffmpeg' are installed
# engine.save_to_file('Hello World', 'test.mp3')
# engine.runAndWait()


# for voice in voices:
#     print(voice.id)



# import pyttsx3
# def onStart(name):
#    print ('starting', name)
# def onWord(name, location, length):
#    print ('word', name, location, length)
# def onEnd(name, completed):
#    print ('finishing', name, completed)
# engine = pyttsx3.init()
# engine.connect('started-utterance', onStart)
# engine.connect('started-word', onWord)
# engine.connect('finished-utterance', onEnd)
# engine.say('The quick brown fox jumped over the lazy dog.')
# engine.runAndWait()



# import pyttsx3
# def onWord(name, location, length):
#    print ('word', name, location, length)
#    if location > 10:
#       engine.stop()
# engine = pyttsx3.init()
# engine.connect('started-word', onWord)
# engine.say('The quick brown fox jumped over the lazy dog.')
# engine.runAndWait()



# engine = pyttsx3.init()
# voices = engine.getProperty('voices')
# for voice in voices:
#    engine.setProperty('voice', voice.id)
#    engine.say('The quick brown fox jumped over the lazy dog.')
# engine.runAndWait()



# engine = pyttsx3.init()
# rate = engine.getProperty('rate')
# engine.setProperty('rate', rate+50)
# engine.say('The quick brown fox jumped over the lazy dog.')
# engine.runAndWait()



# engine = pyttsx3.init()
# volume = engine.getProperty('volume')
# engine.setProperty('volume', volume-0.25)
# engine.say('The quick brown fox jumped over the lazy dog.')
# engine.runAndWait()



# engine = pyttsx3.init()
# def onStart(name):
#    print ('starting', name)
# def onWord(name, location, length):
#    print ('word', name, location, length)
# def onEnd(name, completed):
#    print ('finishing', name, completed)
#    if name == 'fox':
#       engine.say('What a lazy dog!', 'dog')
#    elif name == 'dog':
#       engine.endLoop()
# engine = pyttsx3.init()
# engine.connect('started-utterance', onStart)
# engine.connect('started-word', onWord)
# engine.connect('finished-utterance', onEnd)
# engine.say('The quick brown fox jumped over the lazy dog.', 'fox')
# engine.startLoop()



engine = pyttsx3.init()
engine.say('The quick brown fox jumped over the lazy dog.', 'fox')
engine.startLoop(False)
# engine.iterate() must be called inside externalLoop()
engine.endLoop()