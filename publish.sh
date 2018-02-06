#!/bin/bash

HOST='ftp.fundor333.com'
USER='fundor333.com'
PASS="$1"

TARGETFOLDER=/htdocs
SOURCEFOLDER=$PWD/public

echo
echo $SOURCEFOLDER
echo
echo $TARGETFOLDER
echo

cd $PWD
rm -r $SOURCEFOLDER

hugo
lftp -f "
open $HOST
user $USER $PASS
lcd $SOURCEFOLDER
mirror --reverse --delete --verbose $SOURCEFOLDER $TARGETFOLDER
bye
"
