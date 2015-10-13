#!/usr/bin/env bash

# Ensure that Ansible recognizes the short-form role name, rather than the
# name of the GitHub repo.  For instance, $PWD/../ansible-role-nginx gets
# symlinked to $PWD/../nginx so the playbook can contain "role: nginx".
: "${DESTDIR:="$PWD"}"

dirname="${DESTDIR##*/}"

if [[ -z "$ROLE_NAME" ]]; then
    ROLE_NAME="${dirname##*-}"
fi

ln -sf "$dirname" ../"$ROLE_NAME"
