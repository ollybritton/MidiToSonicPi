# MidiToSonicPi
MidiToSonicPi is a python script which coverts [Tone.js JSON](https://tonejs.github.io/MidiConvert/) into
Sonic Pi script.

## Running
To run the program, go into the directory and run:

`python run.py`

Or, if you're a cool:

`python3 run.py`

This will generate the code and place it into the file `code.txt`.


## Settings
You can change the settings in the `settings.json` file:


    {
      "settings": {
        "path": The path to the file, by default "data.json".
        "synth": The synthesizer, by default "piano". "piano" will generate code "use_synth :piano", so don't include the colon.
        "speed_multiplier": The number to multiply all the times by. For example, 2 will make the song twice as slow as all the notes last twice as long. By default 1.
        "pretty": Toggles whether the code is pretty or not. By default "true".
        "cutoff": The amount of notes that it should generate. By default 100, as otherwise Sonic Pi takes ages to run.
      }
    }

## Examples
The examples that come by default are (surprisingly) in the `examples` folder. To try one of them, set the path to `examples/filename.json`.
