#!/bin/bash

#while IFS= read -r line; do
 # printf '%s\n' "$line"
#done

var=$(cat)
echo "$var" > /tmp/log_test.txt

#echo "ici"
#printf 'content of file on stdin: %s\n' "$(</dev/stdin)"
#echo "ici"
#sudo find /var/spool/mail -type f -printf '%T@ %p\n' | sort -n | tail -1 | cut -f2- -d" "
#sudo cat /var/spool/mail/souidi # > /home/meldiffere/mail_recu.txt
#service postfix stop
#postcat -vq mailq | awk '$7 ~/@/ { print $1 }'
