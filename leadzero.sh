#!/bin/sh

AMOUNT=$1

NEWAMOUNT= `echo $AMOUNT | sed 's/^0*//'`

cat $NEWAMOUNT
exit 0
