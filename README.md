[![Build Status](https://travis-ci.com/kirbyj/vPhon.svg?branch=master)](https://travis-ci.com/kirbyj/vPhon)

# vPhon: a Vietnamese phonetizer

Package: vPhon version 2.1.0

Author: James Kirby <j.kirby@ed.ac.uk>

Web: [https://github.com/kirbyj/vPhon](https://github.com/kirbyj/vPhon)

This software takes UTF-8 Vietnamese orthography and returns UTF-8 output in the International Phonetic Association (IPA) alphabet for three major dialects of Vietnamese: Northern (Hà Nội), Central (Huế), and Southern (Sài Gòn) speech.

For more information on the IPA, go to

https://www.internationalphoneticassociation.org/content/full-ipa-chart

## Installation

No installation is required. vPhon should work with Python 3.4 and higher. vPhon requires the `sys`, `string`, `re`, `io`, and `argparse` modules, all of which should come standard with Python >= 3.5. The correspondence file `rules.py` should live in the same directory as `vPhon` itself.

## Usage

From v2.0.0, vPhon does not take any obligatory arguments: it defaults to producing narrow (surface) Northern dialect forms, including glottal onsets, with tones in Gedney-style superscript. For more details, see [Representational considerations](#representational-considerations).

vPhon was designed to work in a manner similar to that of Unix command line utilities, and as such it expects to receive UTF-8 text via STDIN. If you have a file called `tuoi.txt`, for example, and want to create Southern-dialect IPA from it, either of the following will work:

```
[user@terminal]$ python vPhon.py -d s < text/tuoi.txt
[user@terminal]$ cat text/tuoi.txt | python vPhon.py --dialect s
```

If no input is provided, vPhon will enter an interactive mode allowing you to enter UTF-8 Vietnamese orthography on the command line. When you are done, send `EOF` (Ctrl-D) to get the output. By default, output is sent to STDOUT.

## Options

The full list of options can be seen by using the `-h, --help` flag:

```
usage: vPhon.py [-h] [-d {n,c,s}] [-c] [-g] [-6] [-n] [-p] [-m DELIMIT]
                [-o OUTPUT_ORTHO] [-t]

python vPhon.py

optional arguments:
  -h, --help            show this help message and exit
  -d {n,c,s}, --dialect {n,c,s}
                        Specify dialect region (Northern, Central, Southern)
  -c, --chao            Phonetize tones as Chao values
  -g, --glottal         No glottal stops in underlying forms
  -n, --nosuper         No superscripts anywhere
  -p, --phonemic        Underlying transcriptions after Pham (2006)
  -m DELIMIT, --delimit DELIMIT
                        produce delimited output (bi ca = .b.i.33. .k.a.33.)
  -o OUTPUT_ORTHO, --ortho OUTPUT_ORTHO
                        output orthography as well as IPA (quốc: wok⁴⁵)
  -t, --tokenize        Preserve underscores or hyphens in tokenized inputs
                        (anh_ta = anhᴬ¹_taᴬ¹)
```

vPhon's default behavior is to produce narrow (surface) Northern dialect forms, including glottal onsets, with tones in [Gedney-style superscript](#tones). The `--chao` flag will output superscript Chao tone numbers. If you would like to supress the superscripts (also for labialization), use the `--nosuper` flag:

```
[user@terminal]$ python vPhon.py --chao --nosuper < text/wordlist-top.txt 
ʔaː33 zuə33
ʔaː33 haː33
ʔaː33 hwaːn32
ʔaː33 laː33 haːn24
```

As noted above, vPhon can produce an "underlying" (phonemic) representation following the analysis of Pham (2006). To generate this, use the `--phonemic` flag:

```
[user@terminal]$ python vPhon.py --phonemic < text/baamboo.txt 
tɕuŋᴮ¹ tojᴬ¹ ɲɨŋᶜ² ŋɨəjᴬ² ɗaːŋᴬ¹ laːmᴬ² saːnᶜ¹ fəmᶜ¹ [baamboo] tɕaᴬ¹ tɨᴬ² kaːmᶜ¹ tʰəjᴮ¹ zətᴰ¹ tɨᴮ² haːwᴬ² ɗɨəkᴰ² laːmᴬ² viəkᴰ² kuŋᴬ² kaːkᴰ¹ ɓaːnᴮ² motᴰ² koŋᴮ² ɗoŋᴬ² tɕiᴬ¹ tʰɨkᴰ¹ luənᴬ¹ ɲiətᴰ² hʷiətᴰ¹ vaᴬ² sajᴬ¹ meᴬ¹ laːmᴬ² viəkᴰ² hʷaːnᴬ² tʷaːnᴬ² viᴬ² sɨᴮ² faːtᴰ¹ tɕiənᶜ¹ tɕuŋᴬ¹ maᴬ² xoŋᴬ¹ kɔᴮ¹ ɓətᴰ¹ kiᴬ² ɗoŋᴮ² kəᴬ¹ kaᴮ¹ ɲənᴬ¹ naːwᴬ²
```

Compare 

```
python vPhon.py < text/baamboo.txt 
tɕuŋ͡mᴮ¹ toːjᴬ¹ ɲɨŋᶜ² ŋɨəjᴬ² ɗaːŋᴬ¹ laːmᴬ² saːnᶜ¹ fəmᶜ¹ [baamboo] tɕaːᴬ¹ tɨːᴬ² kaːmᶜ¹ tʰəjᴮ¹ zətᴰ¹ tɨːᴮ² haːwᴬ² ɗɨəkᴰ² laːmᴬ² viəkᴰ² kuŋ͡mᴬ² kaːkᴰ¹ ɓaːnᴮ² moːtᴰ² koŋ͡mᴮ² ɗoŋ͡mᴬ² tɕiːᴬ¹ tʰɨkᴰ¹ luənᴬ¹ ɲiətᴰ² hʷiətᴰ¹ vaːᴬ² sajᴬ¹ meːᴬ¹ laːmᴬ² viəkᴰ² hʷaːnᴬ² tʷaːnᴬ² viːᴬ² sɨːᴮ² faːtᴰ¹ tɕiənᶜ¹ tɕuŋ͡mᴬ¹ maːᴬ² xoŋ͡mᴬ¹ kɔːᴮ¹ ɓətᴰ¹ kiːᴬ² ɗoŋ͡mᴮ² kəːᴬ¹ kaːᴮ¹ ɲənᴬ¹ naːwᴬ²
```

which features labiodorsal finals and lengthened vowels in open syllables. 

By default, glottal stops are inserted in onsetless syllables in both the surface and underlying transcriptions. To suppress the insertion of glottal stops, use the `--glottal` flag.
 
The `--tokenize` flag is useful if you are processing an older source in which morphemes are separated by hyphens, and you wish to retain the hyphens in your output, or if you are processing the output of e.g. [vnTokenizer](http://mim.hus.vnu.edu.vn/phuonglh/softwares/vnTokenizer):

```
[user@terminal]$ python vPhon.py -t -n -c -p < text/tokenized.txt
tɕaw24 ʔoŋ͡m33_taː33 kuŋ͡m3g5 viən33 tɕɨə33 ɓiət45
```

The `--delimit` flag will produce produce output where each phonetic symbol is separated by user-specified delimiter. If you use this flag, you must also specify a delimiter, e.g. 

```
[user@terminal]$ python vPhon.py -m . -c < text/tokenized.txt
.tɕ.a.w.²⁴. [ông_ta] .k.u.ŋ͡m.³ˀ⁵. .v.iə.n.³³. .tɕ.ɨə.³³. .ɓ.iə.t.⁴⁵
```

The `--ortho` flag will output the orthographic input followed by a user-specified delimiter, followed by the phonetized output. If you use this flag, you must also specify a delimiter, e.g. 

```
[user@terminal]$ python vPhon.py -o , < text/wordlist-top.txt 
a dua,ʔaːᴬ¹ zuəᴬ¹
a ha,ʔaːᴬ¹ haːᴬ¹
a hoàn,ʔaːᴬ¹ hʷaːnᴬ²
a la hán,ʔaːᴬ¹ laːᴬ¹ haːnᴮ¹
a-lô,[a-lô]
```

```
[user@terminal]$ python vPhon.py -o $'\n' -c -n -p -g < text/wordlist-top.txt
a dua
a33 zuə33
a ha
a33 ha33
a hoàn
a33 hwaːn32
a la hán
a33 la33 haːn24
a-lô
[a-lô]
```

## Notes

All non-alphanumeric characters in the input are stripped prior to processing (unless the `--tokenize` option is selected, in which case `-` and `_` will be retained in the output). 

Any input containing non-Vietnamese orthography, or series of characters not conforming to Vietnamese phonotactics, will be braced in the output, e.g.

```
[user@terminal] cat text/tuoi.txt | python vPhon.py -c -n -g
[tt] [hacao] [linux] laː32 moːt21 heː21g ɗiəw32 haɲ32 ɲɔː312 ɣɔːn21g tok͡p45 ɗoː21g ɗəj32 ɗuː312 tiən21g ŋiː33 miən3g5 fiː24 maː3g5 ŋuən32 məː312 ɗɨək21 taːw21g zaː33 zaɲ32 tɕɔː33 tət45 kaː312 mɔːj21g ŋɨəj32
[hacao] [linux] kɔː24 theː312 tɕaj21g tɕɨk21 tiəp45 tɕeːn33 [cd] maː32 xoŋ͡m33 laːm32 aɲ312 hɨəŋ312 ɗeːn24 heː21g thoŋ͡m24 maj24 tiːɲ24 hiən21g taːj21g ŋaːj32 zaː33 [hacao] [linux] kɔːn32 kɔː24 theː312 kaːj32 ɗat21 vaːw32 kaːk45 thaɲ33 ɲəː24 [usb] haj33 kaːj32 thaŋ312 vaːw32 oː312 kɨŋ24 maj24 tiːɲ24
hiən21g naj33 [hacao] [linux] kɔː24 haːj33 fiən33 ɓaːn312
fiən33 ɓaːn312 ɲɔː312 ɣɔːn21g tok͡p45 ɗoː21g zaɲ32 tɕɔː33 ɲɨŋ3g5 ŋɨəj32 iəw33 thiːc45 sɨː21g ɲɔː312 ɣɔːn21g [79,5mb]
```

You could also extract just these items, e.g.

```
[user@terminal] cat text/tuoi.txt | python vPhon.py | awk -F '[][]' '{for (i=2; i<=NF; i+=2) {printf "%s ", $i}; print ""}'
tt hacao linux 
hacao linux cd hacao linux usb 
hacao linux 
79,5mb 
```

Try playing with the examples in the `text/` directory to get a better idea of this behavior. 


### Known issues

There is no Unicode upper-case superscript 'C'. If this really bothers you, use `--nosuper` and/or the `--delimit` flag, or `--chao` .


## Representational considerations

From version 2.1, vPhon's output is based on the phonetic and phonological analysis presented by Pham (2006). This is not the only possible representational solution to the problem of Vietnamese phonotactics, but it has the advantage of a being a well-documented one. See Pham (2006) for details and references to earlier work. 

### General

For onsets and codas, vPhon uses the transcription proposed in Brunelle (2015), with the exception that the affricated palatal plosive is transcribed as [tɕ]. Internally, vPhon uses different onset symbols for *tr* and *ch*, *x* and *s*, and *r gi d*. In the narrow surface forms, orthographic *x* and *s* are merged to [s] in the Southern varieties. While vPhon uses /r/ to encode orthographic *r* in Central and Southern dialects, the actual phonetic realization can vary widely, unlike in typical Hanoi speech where *r* is consistently [z]. The choice of /ʈ/ to represent orthographic *tr* is similarly motivated. The use of distinct symbols for the different dialects is designed to facilitate cross-dialectal comparison, but should not be interpreted as making specific claims about phonetic realization or variability.

In narrow phonetic output, the labiodorsal allophones of /ŋ k/ are represented as [ŋ͡m k͡p].

The representational issue of vowel length is vexed. Phonetically, Vietnamese distinguishes (At least) 3 surface vowel lengths, predictable to a large extent on the basis of syllable structure (see Emerich 2012 for some phonetic data on the realization of vowel length in Northern Vietnamese). Phonologically, however, only 2 degrees of vowel length are contrastive, and then only in certain contexts. For typographic simplicity, many authors (e.g. Kirby 2011, Brunelle 2015) will indicates the (phonetically and phonologically) short vowels <â> <ă> with a brevis, i.e. [ə̆ ă], and leave other vowels unmarked for length on the surface, but this solution is less suitable for Southern varieties. For consistency, from version 2.1 vPhon follows IPA convention and eschews the brevis, so that in the surface (phonetic) representations, phonetically short vowels are unmarked and long vowels are indicated as such with a length diacritic (e.g. [aː]).

### Tones

vPhon represents tone using one of two methods. By default, vPhon returns tones using "Gedney"-style notation (A1, A2, B1...) following Michaud (2004) and Brunelle (2015). In this system each tone receives a combination of a letter and a number. The *A* tones derive from historically open syllables, *B* tones derive from creaky syllables and syllables originally closed by a glottal stop, *C* tones derive from syllables with final spirants (-h), and *D* tones from historically `checked' syllables, i.e. those with obstruent coda. *1* is used for tones found on syllables that originally had a voiceless onset and *2* is used for syllables that originally had a voiced onset.

If passed the `--chao` flag, vPhon will instead return Chao tone numbers as given the table below, which are based on Alves (2007), Hoàng Thị Châu (1989), Nguyễn Văn Lợi and Edmonson (1997), Nguyễn Văn Lợi (2012), and Vũ (1982). Note that, especially for Central (Huế) speech, a wide range of proposals abound: see Nguyễn Văn Lợi (2012) for some discussion.

Note that in the following table, *g* is used to indiciate both (medial) laryngealization and (final) glottalization. This is the output that vPhon produces when passed both the `--chao` and `--nosuper` flags; if only `--chao` is passed then it will produce e.g. `maːn²¹ˀ`, `maː³ˀ⁵` etc.

Name | North | Central | South
---- | ----- | ------- | -----
ngang|33|35|33
huyền|21|42|21
hỏi|312|32g|214
ngã|35g|32g|214
sắc|24/45|2g4/45|45
nặng|21/g|31|212

Regardless of method, for the Central and Southern dialects, orthographic *hỏi* and *ngã* tones are both phonetized as *hỏi* (see Hoàng 1989: 212 *ff.*)


### Northern

- Velar codas are indicated as palatalized [-ʲk, -ʲŋ] after front monophthongs and short [a], and labio-velarized as [-k͡p, -ŋ͡m] after back monophthongs. See Haudricourt (1952) and Pham (2006).
- The affricated palatal (orthographic *ch* *tr*) is transcriped as [tɕ].

### Southern/Central

- The Northern diphthongs [ie ɨə uo] are represented as long [i:n ɨː uː], contrasting with the monophthongs [i ɨ u].
- /i e/ are realized [ɨ ə] before surface coronals.
- On the surface, short back vowels are centralized in closed syllables.
- The hyperformal contrast between /s/ *x* and /ʂ/ *s* only preserved if `--phonemic` is used.
- Similaly, orthographic *v* is merged with *j* in the surface output.
- Following Brunelle (2015), orthographic *tr* is [ʈ] and <ch> is [c].
- Pham (2006) represents non-labial finals as placeless in these dialects; vPhon simply implements the merger in both the underlying and surface forms.
- It is not clear that "Central Vietnamese" is a meaningful construct. Even a careful study of the speech of Huế city has not been carried out for some time. When invoked with `-d c`, vPhon simply produces segmental forms as for Southern vietnamese with surface tones basically following Nguyễn Văn Lợi (2012).


### Things not represented

- Offglides/diphthongization of monophthongs in open syllables
- Possible Southern tendency to realize /x/ as [kʰ] or [xʰ]
- Possible merger between Southern short /ə/ and /a/ (Pham 2006: 128)
- Allophonic variants of the medial glide, including deletion (Brunelle 2015: 912) 

## Citation

If you use vPhon for a project or paper, please cite it as:

    Kirby, James. 2008. vPhon: a Vietnamese phonetizer (version [current_version]). Retrieved on <date> from http://github.com/kirbyj/vPhon/.
    
## Alternatives

[ADRPhone](http://www.mica.edu.vn/ADRPhone) is a lightweight, standalone phonetizer for Vietnamese written in standard C by Nguyễn Thị Minh Tuyền and Mathias Rossignol. It has many of the same functions as vPhon, but helpfully outputs XML as well. 

## Thank You

Thanks to Mark Alves, Luke Bradley, Marc Brunelle, Doug Cooper, James Myers, Nguyễn Thúy Nhã Uyên, and Paul Sidwell for many useful comments and suggestions, and to [Branislav Gerazov](https://github.com/gerazov) and Jia-Cing Ruan (阮家慶) for motivating me to finally make vPhon compatible with python3. Any errors or inconsistencies are, of course, mine alone, but I would love to hear about them.

## References

Alves, Mark J. (2007). "A look at North-Central Vietnamese." In *SEALS XII*, ed. R. Wayland et al., Canberra, Australia, pp. 1-7.

Brunelle, Marc. (2015). "Vietnamese (Tiếng Việt)". In *The handbook of Austroasiatic languages*, ed. M. Jenney and P. Sidwell, pp. 909-953. Leiden: Brill.

Cao Xuân Hạo. (1998). *Tiếng Việt – Mấy vấn đề ngữ âm, ngữ pháp và ngữ nghĩa*. Hà Nội: NXB Giáo dục.

Emerich, Giang H. (2012). *The Vietnamese vowel system*. PhD dissertation, University of Pennsylvania.

Hoàng Thị Châu. (1989). *Tiếng Việt trên các miền đất nước: Phương ngữ học*. Hà Nội: Khoa học Xã hội.

Kirby, James. (2011). "Vietnamese (Hanoi Vietnamese). *Journal of the International Phonetic Association" 41(3), 381-392.

Michaud, Alexis. (2004). Final consonants and glottalization: New perspectives from Hanoi Vietnamese. *Phonetica* 61, 119-146.

Nguyễn Đình-Hoà. (1997). *Vietnamese: Tiếng Việt không son phấn*. Amsterdam: John Benjamins Publishing Company.

Nguyễn Văn Lợi (2012). Hệ thống thanh điệu tiếng Huế (dựa trên kết quả khảo nghiệm bằng computer). *Tạp chí Từ điển học & Bách khoa thư* 5(19), 54-65.

Nguyễn Văn Lợi & Edmondson, Jerold A. (1997). Tones and voice quality in modern northern Vietnamese: Instrumental case studies. *Mon-Khmer Studies* 28, 1-18.

Pham, Andrea Hoa. (2006). Vietnamese rhyme. *Southwest Journal of Linguistics* 25(2), 109-141.

Thompson, Laurence E. (1965). *A Vietnamese reference grammar*. Seattle: University of Washington Press.

Vũ, T. P. (1982). Phonetic properties of Vietnamese tones across dialects. In *Papers in Southeast Asian Linguistics Volume 8 - Tonation*, ed. D. Bradley. Sydney, Australian National University, pp. 55-75.
