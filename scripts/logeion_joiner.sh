#!/bin/sh
# need to run this in a 'greatscott' folder
# i.e., clone https://github.com/helmadik/LSJLogeion first

for f in greatscott*xml
do
	# [a] remove all newlines so as to purge the errant ones
	perl -p -i -e 's/\n//g' $f

	# [b] remove the page break xml
	perl -p -i -e 's/<pb\sn=".*?"\s\/>//g' $f

	# [c] add the right newlines...
	gsed -i 's/<\/div2> <div2 /<\/div2>\n\n<div2 /g' $f
	gsed -i 's/<\/div2><div2 /<\/div2>\n\n<div2 /g' $f
done

cat great* > logeion.lsj.xml
gzip logeion.lsj.xml

