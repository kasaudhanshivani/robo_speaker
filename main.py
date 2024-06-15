import os

if __name__ == '__main__':
    print("Welcome to RoboSpeaker 2.0 created by Shivani")
    while True:
        x = input("Enter what you want to pronounce: ")
        if x.lower() == "quit":
            bye_command = 'powershell -Command "Add-Type -AssemblyName System.Speech; ' \
                          ('$speak = New-Object System.S'
                           'peech.Synthesis.SpeechSynthesizer; ') \
                          '$speak.Speak(\'bye bye friend\');"'
            os.system(bye_command)
            break

        command = f'powershell -Command "Add-Type -AssemblyName System.Speech; ' \
                  f'$speak = New-Object System.Speech.Synthesis.SpeechSynthesizer; ' \
                  f'$speak.Speak(\'{x}\');"'
        os.system(command)
