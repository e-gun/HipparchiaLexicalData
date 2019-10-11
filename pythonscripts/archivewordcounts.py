# -*- coding: utf-8 -*-
"""
        HipparchiaServer: an interface to a database of Greek and Latin texts
        Copyright: E Gunderson 2016-19
        License: GNU GENERAL PUBLIC LICENSE 3
                (see LICENSE in the top level directory of the distribution)
"""
import os
import subprocess

# pg_dump --host localhost --port 5432 --username postgres --format plain --ignore-version --verbose --file "<abstract_file_path>" --table public.tablename dbname

# export PGPASSWORD="HIPPARDPASSHERE" python3 archivewordcounts.py

dir_path = os.path.dirname(os.path.realpath(__file__))

thepath = dir_path+'/wordcounts/'
wcprefix = 'wordcounts'
theuser = 'hippa_rd'

cmd = 'pg_dump'
hostarg = '--host=localhost'
portarg = '--port=5432'
userarg = '--username={u}'.format(u=theuser)
formarg = '--format=plain'
verb = '--verbose'
tablearg = '--table=public.wordcounts_{c}'
dbname = 'hipparchiaDB'

counter = 'abcdefghijklmnopqrstuvwxyzαβγδεζηθικλμνξοπρϲτυφχψω0'

for c in counter:
	thefile = '{p}{x}_{c}.sql'.format(p=thepath, x=wcprefix, c=c)
	# subprocess.run(['rm', '{f}'.format(f=thefile)])
	# subprocess.run(['touch', '{f}'.format(f=thefile)])
	sp = [cmd, hostarg, portarg, userarg, formarg, verb]
	sp.append('--file={f}'.format(f=thefile))
	sp.append(tablearg.format(c=c))
	sp.append(dbname)
	subprocess.run(sp)
	subprocess.run(['rm', '{f}.gz'.format(f=thefile)])
	subprocess.run(['gzip', '{f}'.format(f=thefile)])

thefile = '{p}dictionary_headword_wordcounts.sql'.format(p=thepath)
sp = [cmd, hostarg, portarg, userarg, formarg, verb]
sp.append('--file={f}'.format(f=thefile))
sp.append('--table=dictionary_headword_wordcounts')
sp.append(dbname)
subprocess.run(sp)
subprocess.run(['rm', '{f}.gz'.format(f=thefile)])
subprocess.run(['gzip', '{f}'.format(f=thefile)])
