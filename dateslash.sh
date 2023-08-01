#!/bin/sh

DATE=$1

if [ "$DATE" -gt 1012000 ]; then
	if [ "$DATE" -lt 12319999 ]; then
		MM=`/bin/expr "$DATE" / 1000000`
		DDYY=`/bin/expr "$DATE" % 1000000`
		DD=`/bin/expr "$DDYY" / 10000`
		YY=`/bin/expr "$DDYY" % 10000`
		echo "$MM/$DD/$YY                       "
		exit
	fi
fi
echo " "
exit
