# -*- coding: utf-8 -*-
"""
HipparchiaServer: an interface to a database of Greek and Latin texts
Copyright: E Gunderson 2016-20
License: GNU GENERAL PUBLIC LICENSE 3
	(see LICENSE in the top level directory of the distribution)
"""

import os
import subprocess

"""

rather than build the morphology one could load the tables: greek_lemmata, greek_morphology, ...

this will let you archive a built table

note that the script assumes that it can descend into './prebuiltmorphology/'; but 'scripts/' is on the same
level as that directory; so move something around before running this

"""

dir_path = os.path.dirname(os.path.realpath(__file__))

thepath = dir_path+'/prebuiltmorphology/'
gramtables = ['morphology', 'lemmata']
languages = ['greek', 'latin']
theuser = 'hippa_rd'

cmd = 'pg_dump'
hostarg = '--host=localhost'
portarg = '--port=5432'
userarg = '--username={u}'.format(u=theuser)
formarg = '--format=plain'
verb = '--verbose'
tablearg = '--table=public.{lg}_{gr}'
dbname = 'hipparchiaDB'

# pg_dump --host localhost --port 5432 --username postgres --format plain --ignore-version --verbose --file "<abstract_file_path>" --table public.tablename dbname

for lg in languages:
	for gram in gramtables:
		thefile = '{p}{lg}_{gr}.sql'.format(p=thepath, lg=lg, gr=gram)
		sp = [cmd, hostarg, portarg, userarg, formarg, verb]
		sp.append('--file={f}'.format(f=thefile))
		sp.append(tablearg.format(lg=lg, gr=gram))
		sp.append(dbname)
		subprocess.run(sp)
		subprocess.run(['gzip', '{f}'.format(f=thefile)])
