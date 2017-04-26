"""
A Python script to convert Tone.js json song data into Sonic Pi code.
"""

import json

with open("settings.json", "r") as settings_file:
    settings = json.load(settings_file)

with open(settings["settings"]["path"], "r") as data_file:
    data = json.load(data_file)["tracks"][1]["notes"]

speed_multiplier = settings["settings"]["speed_multiplier"]

if settings["settings"]["cutoff"] == "false":
    cutoff = len(data)
else:
    cutoff = settings["settings"]["cutoff"]

if settings["settings"]["pretty"] == "false":
    code = open("code.txt","w+")

    code.write("use_synth :" + settings["settings"]["synth"] + ";")

    for i in range( cutoff ):

        code.write("play " + str(data[i]["midi"])
                   + ",release:" + str(data[i]["time"] * speed_multiplier)
                   + ";sleep " + str(data[i]["duration"] * speed_multiplier)
                   + ";")


elif settings["settings"]["pretty"] == "true":
    code = open("code.txt","w+")

    code.write("use_synth :" + settings["settings"]["synth"] + "\n\n")

    for i in range( cutoff ):

        code.write("play " + str(data[i]["midi"])
        + ", release: " + str( data[i]["time"] * speed_multiplier)
        + "\n")

        code.write("sleep " + str(data[i]["duration"] * speed_multiplier) + "\n")

        code.write("\n")

else:
    print("You put an illegal value for the \"pretty\" setting in the settings.json file. Try turning it into \"true\" or \"false\".")
