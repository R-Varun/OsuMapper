# OsuMapper
PCG for Osu! Beatmaps

## Current State of the Repository
Nearly completed parsing for `.osu` files (being able to write back to them as well)


## Latest Updates
- Parsing, writing for `.osu` files,
- 1D convolution (peak detect) on Song waveform to identify points of potential beat
- Waveform visualization add ons
- Genetic Algorithm resample, mutate, crossover

## TODO
- Support for parsing/ encoding sliders
- Genetic Algorithm fitness functions, crossover functions, and mutation functions

## Required Packages
Python 3.XX with SciPy installed. FFmeg is also used in a separate process to convert `.mp3` to `.wav`. Make sure to have FFmpeg in path so that the script can access it.


## Approach
For the GA, I've modelled the problem as at each time step of the BPM (or in code, Milliseconds per beat (Mspb)), there's a GANote object. At every division of a measure, we make a decision on whether there is a note there or not and additionally where the note is placed.
