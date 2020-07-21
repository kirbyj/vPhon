# tests.py

import os, subprocess, sys, time, filecmp, difflib
from glob import glob

# not doing full range of tests at the moment but should, eventually
dialects = ['n', 's', 'c']
tones = ['', '-c']
reps = ['', '-p']
lower = ['']
glottal = ['']

print("Starting tests...")
print("user:", os.environ['USER'])
print("path:", os.getcwd())
print("time:", time.asctime(), "\n")

# set exit status: default is OK
exit_status = 0

# for all matching input files
for test in glob('test/*.in'):     
    
    # generate vPhon calls based on arg combos
    infile = test.split('.')[0]

    # generate flag combos and associated testfiles
    testfiles = []
    flags = []

    for dialect in dialects:
        for tone in tones:
            for level in reps:
                for g in glottal:
                    flags.append("-d %s %s %s %s" % (dialect, tone, level, g))
                    testfiles.append("%s_%s%s%s%s" % (infile, dialect, tone, level, g))
        
    for i in range(0, len(testfiles)):
        if not os.path.exists('%s.out' % testfiles[i]):
            # no prior results
            os.system("python vPhon.py %s < %s.in > %s.out 2>&1" % (flags[i], infile, testfiles[i]))
            print('GENERATED:', testfiles[i],)
        else:
            # backup, run, compare
            os.rename(testfiles[i] + '.out', testfiles[i] + '.out.bk')
            os.system("python vPhon.py %s < %s.in > %s.out 2>&1" % (flags[i], infile, testfiles[i]))
            result = filecmp.cmp(testfiles[i] + '.out', testfiles[i] + '.out.bk')
            if result == True:
                print('PASSED:', testfiles[i])
            else:
                print('FAILED:', testfiles[i], '(see %s.diffs)' % testfiles[i])
                os.system('diff %s.out %s.out.bk > %s.diffs' % ((testfiles[i],)*3) )
                exit_status = 1

# explicit exit status
sys.exit(exit_status)    
