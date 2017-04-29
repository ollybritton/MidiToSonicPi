# MidiToSonicPi
This python code is a script which converts [Tone.js formatted JSON](https://tonejs.github.io/MidiConvert/) into Sonic Pi Code. However, I am currently reworking the program into something that doesn't convert the midi file into JSON.

## Using
To use the script on any midi file, for example, `allstar.mid`, you need to first convert into a JSON by going to the [Tone.js MidiConvert website](https://tonejs.github.io/MidiConvert/). Copy and paste the result into `data.json` and run either `python run.py` or `python3 run.py` and the result will be outputted to `code.txt`.

One thing to note however is that the **amount of notes in the song is by default capped at 200.** This is because having too many notes in a song will slow down Sonic Pi stop it from executing. For example, `examples/pluginbaby.json` has over *1550* notes, which Sonic Pi just can't handle.

## Settings
You can change how the script converts the JSON file in the file `settings.json`. Here's a brief rundown of all the parameters:

- `path: str`: This sets the path to the JSON file to convert. For example, to run `hello.json`, you need to change it to `examples/hello.json`. By default it's `data.json`.

- `synth: str`: Sets the synth to be used at the top of the Sonic Pi file. For example, `pretty_bell` converts to `use_synth :pretty_bell`. By default, it's set to `piano`. A word of warning, however: setting it to something like `blade` will cause all the notes to blend together and become an inharmonic mess.

- `speed_multiplier: num`: Multiplies all the timings by the number given. For example, setting it to 2 will make the song twice as slow, whereas setting it to 0.1 will make the song 10 times as fast. By default, it's 1.

- `pretty: bool`: Controls whether the code should be condensed (take up as little space as possible) or be nice and separated. You can either type it as `true` or `"true"` but not as `True` or `"True"`, as JSON gets upset. By default, it is `true`.

- `cutoff: int`: Cuts off the song at that number of notes. If you set it to `"false"`, then there is no limit, but as I mentioned before, the song will take ages to run in the Sonic Pi software.

- `shift: int`: Shifts all the notes by the number given. For example, if you have the melody:

      use_synth :piano

      play 61
      sleep 0.3

      play 63
      sleep 0.3

      play 64
      sleep 0.3

      play 66
      sleep 0.3

      play 68
      sleep 0.3

    Which is in D minor, and you want to convert it to A minor you count the number of semitones D is away from A and set that as the shift.
