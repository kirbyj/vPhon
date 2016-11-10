# CHANGELOG

## [0.2.6] - 2016-11-09
### Added
- Added -o, --ortho flag to output Viet orthography along with IPA transcription.
- Added -m, --delimit flag to have output separated by a user-specified delimiter.

### Changed
- Output now uses Python 3-style print function 
- Supplying a filename as a command-line argument no longer works: vPhon now reads only from STDIN and writes only to STDOUT. Any text processing should be done in usual Unix fashion (i.e. using shell redirection, `cat`, etc.).

### Fixed
- Fixed bug that was treating gì, gĩ... and qùy, qũy...  as non-Viet characters.
- Fixed bug that was outputing checked syllables with nặng as 21g instead of 21.



## [0.2.5b] - 2016-03-16
### Added
- Added -t, --tokenize flag to preserve underscores or hyphens in tokenized inputs, so that e.g. anh_ta is output as anh1_ta1. 
This flag has the effect of not automatically treating inputs with hyphens as non-Viet words.
