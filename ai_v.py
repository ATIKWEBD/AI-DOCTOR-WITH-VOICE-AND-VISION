# import os 
# from gtts import gTTS
# def tex(text, output_filepath):
#  language="en"

#  audioobj= gTTS(
#           text=text,
#            lang=language,
#           slow=False
        
#           )
#  audioobj.save(output_filepath)


# input_text="Hey this is me atik my first AI project"

# tex(input_text, output_filepath="gtts_testing.mp3")



# # # from elevenlabs import generate, save, set_api_key
# # from elevenlabs import ElevenLabs, Voice, VoiceSettings

# # # set_api_key(os.environ.get("ELEVENLABS_API_KEY"))
# # # ELEVENLABS_API_KEY=os.environ.get("ELEVENLABS_API_KEY")
# # client = ElevenLabs(
# #     api_key=os.environ.get("ELEVENLABS_API_KEY")
# # )

# # def text_t(texture, output_filepath):
# #     # # client=ElevenLabs(api_key= ELEVENLABS_API_KEY)
# #     # audio= client.generate(
# #     #    text=texture,
# #     #    voice="Aria",
# #     #    output_format="mp3_22050_32" ,
# #     #    model="eleven_turbo_v2"
# #     # )
# #     # save(audio,output_filepath)

# #     audio = client.text_to_speech(
# #         text=texture,
# #         voice=Voice(
# #             voice_id="21m00Tcm4TlvDq8ikWAM",  # Aria's default voice ID
# #             settings=VoiceSettings(stability=0.5, similarity_boost=0.75)
# #         ),
# #         model="eleven_turbo_v2",
# #         output_format="mp3_22050_32"
# #     )
# #     with open(output_filepath, "wb") as f:
# #         f.write(audio)

# # from elevenlabs import ElevenLabs

# # client = ElevenLabs(api_key=os.environ.get("ELEVENLABS_API_KEY"))

# # def text_t(text, output_filepath):
# #     # Use the TTS client correctly
# #     audio_bytes = client.tts.generate(
# #         text=text,
# #         voice="Aria",
# #         model="eleven_turbo_v2",
# #         format="mp3_22050_32"
# #     )

# #     with open(output_filepath, "wb") as f:
# #         f.write(audio_bytes)
# # text_t(input_text, output_filepath="elevenlabs_testing.mp3")
# import subprocess
# import platform


# def texy(text, output_filepath):
#  language="en"

#  audioobj= gTTS(
#           text=text,
#            lang=language,
#           slow=False
        
#           )
#  audioobj.save(output_filepath)
#  os_name = platform.system()

#  try:
#         if os_name == "Windows":
#          subprocess.run(['powershell', '-c',f'(New-Object Media.Soundplayer "{output_filepath}").PlaySync();'])
#         else:
#          raise OSError("Unsupported operating system")

#  except Exception as e:
#     print(f"An error occured while trying to play the audio: {e}")


# input_text="Hey this is me atik my first AI project"

# texy(input_text, output_filepath="gts_testing.mp3")
# import sys
# print("Running Python from:", sys.executable)

from gtts import gTTS
import os
import platform
import subprocess
from pydub import AudioSegment

def texi(text, output_filepath_mp3, output_filepath_wav):
    language = "en"
    audioobj = gTTS(text=text, lang=language, slow=False)
    audioobj.save(output_filepath_mp3)

    # Convert MP3 to WAV
    sound = AudioSegment.from_mp3(output_filepath_mp3)
    sound.export(output_filepath_wav, format="wav")

    os_name = platform.system()
    try:
        if os_name == "Windows":
            subprocess.run(['powershell', '-c', f'(New-Object Media.SoundPlayer "{output_filepath_wav}").PlaySync();'])
        else:
            raise OSError("Unsupported operating system")
    except Exception as e:
        print(f"An error occurred while trying to play the audio: {e}")

input_text = "aaaryan dongre is a bitch"
texi(input_text, output_filepath_mp3="gtts_testing.mp3", output_filepath_wav="gtts_testing.wav")


