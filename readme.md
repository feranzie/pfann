# pfann

## generate list of songs
```
python gen_list.py --directory <directory containing songs> --output <output file>
```
Output to write the list of music files

## Build a fingerprint database

Usage of `builder.py`:
```
python builder.py <music list file> <output database location> <model config>
```
Music list file is a file containing list of music file paths.
File must be UTF-8 without BOM. For example:
```
/path/to/fma_medium/000/000002.mp3
/path/to/fma_medium/000/000005.mp3
/path/to/your/music/aaa.wav
/path/to/your/music/bbb.wav
```
Model config is a JSON file like in `configs/` folder.
It is used to load a trained model.
If omitted, the model config is `configs/default.json` by default.

This program supports both MP3 and WAV audio format.
Relative paths are supported but not recommended.

## generate segments for query
Usage of `segments.py`:
```
python segments.py --input_dir <directory where input audio is > --output_dir <output directory> --audio_file < name of the audio file>
```
example: python segments.py --input_dir /home/paperspace/recordings --output_dir data  --audio_file recording.wav

## generate list of segments
```
python gen_list.py --directory <directory containing segments> --output <output file>
```
Output to write the list of music files

## Recognize music
Usage of `matcher.py`:
```
python matcher.py <query list> <database location> <output result file>
```

Query list is a file containing list of query file paths. For example:
```
/path/to/queries/out2_snr2/000002.wav
/path/to/queries/out2_snr2/000005.wav
/path/to/song_recorded_on_street1.wav
/path/to/song_recorded_on_street2.wav
```
Database location is the place where `builder.py` saves database.

The result file will be a TSV file with 2 fields: query file path, and matched music path, but without header.
It may look like this:
```
/path/to/queries/out2_snr2/000002.wav	/path/to/fma_medium/000/000002.mp3
/path/to/queries/out2_snr2/000005.wav	/path/to/fma_medium/000/000005.mp3
/path/to/song_recorded_on_street1.wav	/path/to/your/music/aaa.wav
/path/to/song_recorded_on_street2.wav	/path/to/your/music/aaa.wav
```

Matcher will also generate a `_detail.csv` file and a `.bin` file.
CSV file contains more information about the matches.
It has 5 columns: query, answer, score, time, and part_scores.
* query: Query file path
* answer: Matched music path
* score: Matching score, used in my thesis
* time: The time when the query clip starts in the matched music, in seconds
* part_scores: Mainly used for debugging, currently empty


the <output result file>_detail.csv is what gets displayed
