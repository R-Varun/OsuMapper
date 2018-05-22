# OsuMapper
PCG for Osu! Beatmaps

## Current State of the Repository
Just now starting off. 

There are some parsers for a v12 osu file which will extract general song information, hitcircles and sliders. Models package includes representations on how we'll store game information.

## TODO
- Need to transcribe rest of information from beatmap. 
- Method for BeatMap class to write to .osu file (OsuGame readable format)


## Required Packages
Python 3.XX with SciPy installed. FFmeg is also used in a separate process to convert `.mp3` to `.wav`. Make sure to have FFmpeg in path so that the script can access it.


