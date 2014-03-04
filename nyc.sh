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

# Ask a question
ask() {
  question="$1"
  error_message="$2"
  validation_function="$3"
  printf "$question " > /dev/stderr
  read x
  while ! $validation_function $x; do
    printf "$error_message " > /dev/stderr
    read x
  done
  echo "$x"
}

# Validations
validate_yes_no() {
  anysize="$1"
  miniscule=$(echo "$anysize" | tr '[YN]' '[yn]')
  test "$miniscule" = y || test "$miniscule" = n || test -z "$miniscule"
  return "$?"
}
validate_number() {
  x="$1"
  return test -z $(echo "$x" | tr -d '[0-9]')
}

url=http://nyc.sh/rsvp # Switch this for another form processer so we don't have to run it.
get_wget() {
  wget --post-data "name=$1&email.address=$2&how.many=$3" "$url"
}
get_curl() {
  curl -d "name=$1" -d "email.address=$2" -d "how.many=$3" "$url"
}
get_other() {
  echo 'Copy this to an email, and send it to _@thomaslevine.com.'
  echo "name,email.address,how.many"
}

main() {
  # HTTP GET requests
  if which wget > /dev/null; then
    alias get=get_wget
  elif which curl > /dev/null; then
    alias get=get_curl
  else
    alias get=get_other
  fi

  # Respond if you please.
  echo Respond if you please.
  echo
  name=$(ask 'What is your name?' 'Please type your name and hit enter' 'test -n')
  email_address=$(ask 'What is your email address?' 'Please type your email address and hit enter.' 'test -n')
  raw_guests=$(ask 'Is anyone else coming with you? (y/N)' '"y" or "Y" for yes, "n" or "N" for no' validate_yes_no)
  
  if test "$raw_guests" = y; then
    guests=$(ask 'How many people other than you?' 'Please enter a number, like "1" or "2".' )
    how_many=$(($guests + 1))
  else
    how_many=1
  fi
}

if test -z $TESTING; then
  main
fi
