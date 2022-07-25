#!/bin/sh

# clean out extra whitespaces first
for f in greatscott*xml
do
	# remove all newlines so as to purge the errant ones
	# tr -d '\n' < x.xml > y.xml
	perl -p -i -e 's/\n//g' $f

	# add the right newlines...
	gsed -i 's/<\/div2> <div2 /<\/div2>\n\n<div2 /g' $f
done

cat great* > logeion.lsj.xml
gzip logeion.lsj.xml
