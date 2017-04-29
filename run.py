"""
A Python script to convert Tone.js json song data into Sonic Pi code.
"""

import json

with open("settings.json", "r") as settings_file:
    settings = json.load(settings_file)["settings"]
    # Load convert settings

with open(settings["path"], "r") as data_file:
    data = json.load(data_file)["tracks"][1]["notes"]
    # Load the data


speed_multiplier = int(settings["speed_multiplier"])

if settings["cutoff"] == "false":
    cutoff = len(data)
else:
    cutoff = int(settings["cutoff"])

if settings["pretty"] == "false" or settings["pretty"] == False:
    code = open("code.txt","w+")

    code.write("use_synth :" + settings["synth"] + ";")

    for i in range( cutoff ):

        code.write("play " + str(data[i]["midi"] + int(settings["shift"]))
                   + ",release:" + str( round(data[i]["time"] * speed_multiplier * 1000)/1000 )
                   + ";sleep " + str( round(data[i]["duration"] * speed_multiplier * 1000)/1000 )
                   + ";")


elif settings["pretty"] == "true" or settings["pretty"] == True:
    code = open("code.txt","w+")

    code.write("use_synth :" + settings["synth"] + "\n\n")

    for i in range( cutoff ):

        code.write("play " + str(data[i]["midi"] + int(settings["shift"]))
        + ", release: " + str( round(data[i]["time"] * speed_multiplier * 1000)/1000)
        + "\n")

        code.write("sleep " + str( round(data[i]["duration"] * speed_multiplier * 1000)/1000) + "\n")

        code.write("\n")

else:
    print("You put an illegal value for the \"pretty\" setting in the settings.json file. Try turning it into \"true\" or \"false\".")
