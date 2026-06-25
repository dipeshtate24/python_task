import win32com.client as wincl

# Initialize the SAPI SpVoice object
speaker = wincl.Dispatch("SAPI.SpVoice")

# Make it speak
speaker.Speak("Hello, this is a free text to speech test on Windows.")