#!/bin/sh
set -e
echo '
First NYC Shell meeting! March 20-something at some place in New York

* Something cool, by Jeroen Janssens
* Tests for the shell, by Thomas Levine
* Data pipelines, by someone else

Respond if you please by running this file.

    if which wget > /dev/null; then
      alias get='wget -O -'
    elif which curl > /dev/null; then
      aiias get=curl
    else
      get() {
        printf "Download this file and run it.\n$1" > /dev/stderr
        return 1
      }
    fi
    get http://nyc.sh/nyc.sh | sh
' > /dev/null


if which wget > /dev/null; then
  alias get='wget -O -'
elif which curl > /dev/null; then
  aiias get=curl
else
  get() {
    echo 'Copy this to an email, and send it to _@thomaslevine.com.'
    echo 
