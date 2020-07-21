# CHANGELOG

## [2.1.0] - 2020-07-21
### Added
- Major re-write of script logic - now generates internal G2P representation as basis for all output types
- As a result, G2P 'rules' mapping greatly simplified
- Changed default tone encodings; options to force strict lowercasing and suppression of glottals
- Added continuous integration testing
- Both surface and underlying outputs now follow Pham (2006)

## [2.0.1] - 2020-05-24
### Added
`syllables.txt` test file

### Changed
- Transcription of \<ch\> (and, for Northern, \<tr\>) to /tɕ/
- Transcription of \<b\> and \<d\> to reflect canonical preglottalized/implosive pronunciation
- Transcriptions of Central tones
- Internally, \<oo\> and \<ôô\> are now represented as long vowels, but they are then shortened before output

### Fixed
- Errors in mappings involving \<e\> and \<ê\>

## [2.0.0] - 2020-05-15
### Added
- Python 3 support. To use vPhon with Python 2, see the v1.0.0 release.

### Changed
- Since `optparse` is deprecated, upgraded to work with `argparse`.
- the -d, --dialect flag is no longer obligatory: vPhon will default to Northen dialect.
- Changed behavior of -o, --ortho flag which outputs Viet orthography along with IPA transcription. Like the -m, --delimit flag, this option now requires a delimiter.
- the -8, --cao option now returns sắc and nặng in checked syllables as 7 and 8, respectively, instead of 5b and 6b.

## [1.0.0] - 2020-05-14
- Final Python 2 version -- legacy release

## [0.2.6] - 2016-11-09
### Added
- Added -o, --ortho flag to output Viet orthography along with IPA transcription.
- Added -m, --delimit flag to have output separated by a user-specified delimiter.

### Changed
- Output now uses Python 3-style print function 
- Supplying a filename as a command-line argument no longer works: vPhon now reads only from STDIN and writes only to STDOUT. Any text processing should be done in usual Unix fashion (i.e. using shell redirection, `cat`, etc.).

### Fixed
- Fixed bug that was treating gì, gĩ... and qùy, qũy...  as non-Viet characters.
- Fixed bug that was treating checked syllables with nặng as 21g instead of 21 in Northern and Southern dialects.
- Fixed bug that was treating sonorant-final syllables with sắc as 45 instead of 24 in Northern and Central dialects.

## [0.2.5b] - 2016-03-16
### Added
- Added -t, --tokenize flag to preserve underscores or hyphens in tokenized inputs, so that e.g. anh_ta is output as anh1_ta1. 
This flag has the effect of not automatically treating inputs with hyphens as non-Viet words.

