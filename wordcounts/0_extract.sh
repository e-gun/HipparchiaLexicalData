#!/bin/sh

# the various solutions below work... if you are not on macOS: can't shake the UTF8 error...
# pg_dump: error: query failed: ERROR:  invalid byte sequence for encoding "UTF8": 0xee 0xbe 0x29

# [A]

# items="0abcdefghijklmnopqrstuvwxyzαβγδεζηθικλμνξοπρϲτυφχψω"

#for (( i=0; i<${#items}; i++ )); do
#  t="${items:$i:1}"
#  echo dumping ${t}
#  pg_dump -t wordcounts_${t} hipparchiaDB > wordcounts_${t}.sql
#done

# [B]

#loopme=`echo ${items} | sed -e 's/\(.\)/\1\n/g'`
#echo ${loopme}
#
#while IFS=read -r < echo ${loopme}
#do
#    echo "$line"
#done

# [C]

#items="0 a b c d e f g h i j k l m n o p q r s t u v w x y z α β γ δ ε ζ η θ ι κ λ μ ν ξ ο π ρ ϲ τ υ φ χ ψ ω"
#IFS=' ' read -r -a array <<< "${items}"
#for element in "${array[@]}"
#do
#  echo dumping ${element}
#  pg_dump -t wordcounts_${element} hipparchiaDB > wordcounts_${element}.sql
#done
#

# [D]

# export PGPASSWORD=yourpass
# export PGUSER=hippa_wr

H="localhost"
U="hippa_wr"
P="mypass"
DB="hipparchiaDB"

# TABLES="$(psql -d hipparchiaDB --username=${U} -t -c "SELECT table_name FROM information_schema.tables WHERE table_type='BASE TABLE' AND table_name LIKE '%wordcount%' ORDER BY table_name")"
# TABLES="$(psql postgresql://${U}:${P}@${H}:5433/hipparchiaDB?sslmode=require -t -c "SELECT table_name FROM information_schema.tables WHERE table_type='BASE TABLE' AND table_name LIKE '%wordcount%' ORDER BY table_name")"
TABLES="$(PGPASSWORD=${P} PGUSER=${U} psql -d ${DB} --username=${U} -t -c "SELECT table_name FROM information_schema.tables WHERE table_type='BASE TABLE' AND table_name LIKE '%wordcount%' ORDER BY table_name")"

for table in $TABLES; do
  echo backup $table ...
  pg_dump -t ${table} hipparchiaDB > ${table}.sql
done
