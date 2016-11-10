#coding: utf-8

###########################################################################
#       vPhon.py version 0.2.6
#       Copyright 2008-2016 James Kirby <j.kirby@ed.ac.uk>
# 
#
#       vPhon is free software: you can redistribute it and/or modify      
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation, either version 3 of the License, or 
#       (at your option) any later version.                  
#
#       vPhon is distributed in the hope that it will be useful,     
#       but WITHOUT ANY WARRANTY; without even the implied warranty of 
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the 
#       GNU General Public License for more details.            
#
#       You should have received a copy of the GNU General Public License 
#       along with vPhon.  If not, see <http://www.gnu.org/licenses/>. 
#
###########################################################################

# for python 3-style printing:
from __future__ import print_function

import sys, codecs, re, StringIO
from optparse import OptionParser
from string import punctuation

def trans(word, dialect, glottal, pham, cao, palatals):

    # This looks ugly, but newer versions of python complain about "from x import *" syntax
    if dialect == 'n':
        from north import onsets, nuclei, codas, tones, onglides, offglides, onoffglides, qu, gi
    elif dialect == 'c':
        from central import onsets, nuclei, codas, tones, onglides, offglides, onoffglides, qu, gi
    elif dialect == 's':
        from south import onsets, nuclei, codas, tones, onglides, offglides, onoffglides, qu, gi

    if pham or cao:
        if dialect == 'n': from north import tones_p
        if dialect == 'c': from central import tones_p
        if dialect == 's': from south import tones_p
        tones = tones_p

    ons = ''
    nuc = ''
    cod = ''
    ton = 0
    oOffset = 0
    cOffset = 0 
    l = len(word)

    if l > 0:
        if word[0:3] in onsets:         # if onset is 'ngh'
            ons = onsets[word[0:3]]
            oOffset = 3
        elif word[0:2] in onsets:       # if onset is 'nh', 'gh', 'kʷ' etc
            ons = onsets[word[0:2]]
            oOffset = 2
        elif word[0] in onsets:         # if single onset
            ons = onsets[word[0]]
            oOffset = 1

        if word[l-2:l] in codas:        # if two-character coda
            cod = codas[word[l-2:l]]
            cOffset = 2
        elif word[l-1] in codas:        # if one-character coda
            cod = codas[word[l-1]]
            cOffset = 1
                            

        #if word[0:2] == u'gi' and cod and len(word) == 3:  # if you just have 'gi' and a coda...
        if word[0:2] in gi and cod and len(word) == 3:  # if you just have 'gi' and a coda...
            nucl = u'i'
            ons = u'z'
        else:
            nucl = word[oOffset:l-cOffset]

        if nucl in nuclei:
            if oOffset == 0:
                if glottal == 1:
                    if word[0] not in onsets:   # if there isn't an onset....  
                        ons = u'ʔ'+nuclei[nucl] # add a glottal stop
                    else:                       # otherwise...
                        nuc = nuclei[nucl]      # there's your nucleus 
                else: 
                    nuc = nuclei[nucl]          # there's your nucleus 
            else:                               # otherwise...
                nuc = nuclei[nucl]              # there's your nucleus
        
        elif nucl in onglides and ons != u'kw': # if there is an onglide...
            nuc = onglides[nucl]                # modify the nuc accordingly
            if ons:                             # if there is an onset...
                ons = ons+u'w'                  # labialize it, but...
            else:                               # if there is no onset...
                ons = u'w'                      # add a labiovelar onset 

        elif nucl in onglides and ons == u'kw': 
            nuc = onglides[nucl]
                
        elif nucl in onoffglides:
            cod = onoffglides[nucl][-1]
            nuc = onoffglides[nucl][0:-1]
            if ons != u'kw':
                if ons:
                    ons = ons+u'w'
                else:
                    ons = u'w'
        elif nucl in offglides:
            cod = offglides[nucl][-1]
            nuc = offglides[nucl][:-1]
                
        elif word in gi:      # if word == 'gi', 'gì',...
            ons = gi[word][0]
            nuc = gi[word][1]

        elif word in qu:      # if word == 'quy', 'qúy',...
            ons = qu[word][:-1]
            nuc = qu[word][-1]
                
        else:   
            # Something is non-Viet
            return (None, None, None, None)


        # Velar Fronting (Northern dialect)
        if dialect == 'n':
            if nuc == u'a':
                if cod == u'k' and cOffset == 2: nuc = u'ɛ'
                if cod == u'ɲ' and nuc == u'a': nuc = u'ɛ'

            # Final palatals (Northern dialect)
            if nuc not in [u'i', u'e', u'ɛ']:
                if cod == u'ɲ': cod = u'ŋ'
            elif palatals != 1 and nuc in [u'i', u'e', u'ɛ']:
                if cod == u'ɲ': cod = u'ŋ'
            if palatals == 1:
                if cod == u'k' and nuc in [u'i', u'e', u'ɛ']: cod = u'c'

        # Velar Fronting (Southern and Central dialects)
        else:
            if nuc in [u'i', u'e']:
                if cod == u'k': cod = u't'
                if cod == u'ŋ': cod = u'n'

            # There is also this reverse fronting, see Thompson 1965:94 ff.
            elif nuc in [u'iə', u'ɯə', u'uə', u'u', u'ɯ', u'ɤ', u'o', u'ɔ', u'ă', u'ɤ̆']:
                if cod == u't': 
                    cod = u'k'
                if cod == u'n': cod = u'ŋ'

        # Monophthongization (Southern dialects: Thompson 1965: 86; Hoàng 1985: 181)
        if dialect == 's':
            if cod in [u'm', u'p']:
                if nuc == u'iə': nuc = u'i'
                if nuc == u'uə': nuc = u'u'
                if nuc == u'ɯə': nuc = u'ɯ'

        # Tones 
        # Modified 20 Sep 2008 to fix aberrant 33 error
        tonelist = [tones[word[i]] for i in xrange(0,l) if word[i] in tones]
        if tonelist:
            ton = unicode(tonelist[len(tonelist)-1])
        else:
            if not (pham or cao):
                if dialect == 'c':
                    ton = unicode('35')
                else:
                    ton = unicode('33')
            else:
                ton = unicode('1')
            
        # Modifications for closed syllables
        if cOffset !=0:

            # Obstruent-final nang tones are modal voice
            if (dialect == 'n' or dialect == 's') and ton == u'21g' and cod in ['p', 't', 'k']:
                #if ton == u'21\u02C0' and cod in ['p', 't', 'k']: # fixed 8 Nov 2016
                ton = u'21'

            # Modification for sắc in closed syllables (Northern and Central only)
            if ((dialect == 'n' and ton == u'24') or (dialect == 'c' and ton == u'13')) and cod in ['p', 't', 'k']:
                ton = u'45'

            # Modification for 8-tone system
            if cao == 1:
                if ton == u'5' and cod in ['p', 't', 'k']:
                    ton = u'5b'
                if ton == u'6' and cod in ['p', 't', 'k']:
                    ton = u'6b'

            # labialized allophony (added 17.09.08)
            if nuc in [u'u', u'o', u'ɔ']:
                if cod == u'ŋ':
                    cod = u'ŋ͡m' 
                if cod == u'k':
                    cod = u'k͡p'

        return (ons, nuc, cod, ton)
    
def convert(word, dialect, glottal, pham, cao, palatals, delimit):
    """Convert a single orthographic string to IPA."""

    ons = ''
    nuc = ''
    cod = ''
    ton = 0
    seq = ''

    try:
        (ons, nuc, cod, ton) = trans(word, dialect, glottal, pham, cao, palatals)
        if None in (ons, nuc, cod, ton):
            seq = u'['+word+u']'
        else:
            seq = delimit+delimit.join(filter(None, (ons, nuc, cod, ton)))+delimit
    except (TypeError), e:
        pass

    return seq
            
def main():
    sys.path.append('./Rules')      # make sure we can find the Rules files

    usage = 'python vPhon.py <input> -d, --dialect N|C|S'

    glottal = 0
    pham = 0 
    cao = 0
    palatals = 0
    tokenize = 0 
    output_ortho = 0 
    delimit = ''

    # Command line options
    parser = OptionParser(usage)
    parser.add_option('-g', '--glottal', action='store_true', dest='glottal', help='prepend glottal stops to onsetless syllables')
    parser.add_option('-6', '--pham', action='store_true', dest='pham', help='phonetize tones as 1-6')
    parser.add_option('-8', '--cao', action='store_true', dest='cao', help='phonetize tones as 1-4 + 5, 5b, 6, 6b')
    parser.add_option('-p', '--palatals', action='store_true', dest='palatals', help='use word-final palatal velars in Northern dialects')
    parser.add_option('-t', '--tokenize', action='store_true', dest='tokenize', help='preserve underscores or hyphens in tokenized inputs (e.g., anh_ta = anh1_ta1)')
    parser.add_option('-o', '--ortho', action='store_true', dest='output_ortho', help='output orthography as well as IPA')
    parser.add_option('-m', '--delimit', action='store', type='string', dest='delimit', help='produce explicitly delimited output (e.g., bi ca = .b.i.33. .k.a.33.')
    parser.add_option('-d', '--dialect', action='store', type='string', dest='dialect', help='specify dialect region ([N]orthern, [C]entral, [S]outhern)')
    (options, args) = parser.parse_args()

    if options.glottal:
        glottal = 1
    if options.pham:
        pham = 1
    if options.cao:
        cao = 1
    if options.palatals:
        palatals = 1
    if options.tokenize:
        tokenize = 1
    if options.output_ortho:
        output_ortho = 1
    if options.delimit:
        delimit = options.delimit[0]
    if options.dialect:
        dialect = options.dialect[0].lower()
    else:
        parser.error('Please enter a valid dialect.')
    if dialect not in ['n', 'c', 's']:
        parser.error('Please enter a valid dialect.')


    # read from stdin
    fh = StringIO.StringIO(unicode(sys.stdin.read(), 'utf-8'))

    # parse the input
    for line in fh:
        if line =='\n':
            pass
        else:
            compound = u''
            ortho = u'' 
            words = line.split()
            ## toss len==0 junk
            words = [word for word in words if len(word)>0]
            ## hack to get rid of single hyphens or underscores
            words = [word for word in words if word!=u'-']
            words = [word for word in words if word!=u'_']
            for i in xrange(0,len(words)):
                word = words[i].strip()
                ortho += word
                word = word.strip(punctuation).lower()
                ## 29.03.16: check if tokenize is true
                ## if true, call this routine for each substring
                ## and re-concatenate 
                if (tokenize and '-' in word) or (tokenize and '_' in word):
                    substrings = re.split(r'(_|-)', word)
                    values = substrings[::2]
                    delimiters = substrings[1::2] + ['']
                    ipa = [convert(x, dialect, glottal, pham, cao, palatals, delimit).strip() for x in values]
                    seq = ''.join(v+d for v,d in zip(ipa, delimiters))
                else:
                    seq = convert(word, dialect, glottal, pham, cao, palatals, delimit).strip()
                # concatenate
                if len(words) >= 2:
                    ortho += ' '
                if i < len(words)-1:
                    seq = seq+u' '
                compound = compound + seq
            
            ## entire line has been parsed
            if ortho == u'':
                pass
            else:
                ortho = ortho.strip()
                ## print orthography?
                if output_ortho: print(ortho.encode('utf-8'), end=','),
                print(compound.encode('utf-8'))

    # If we have an open filehandle, close it
    try:     
        fh.close()
    except AttributeError:
        sys.exit(0)

if __name__ == '__main__':
    main()
