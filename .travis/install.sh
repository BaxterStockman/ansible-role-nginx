#!/usr/bin/env bash

: "${BOOTSTRAP_URL:=https://github.com/BaxterStockman/ansible-bootstrap.git}"
: "${BOOTSTRAP_VERSION:=master}"
: "${BOOTSTRAP_ROLE_NAME:=bootstrap}"
: "${ANSIBLE_HOME:=~/.ansible}"

tmpdir=$(mktemp -d)

ansible-galaxy install -p "$tmpdir" \
    "${BOOTSTRAP_URL},${BOOTSTRAP_VERSION},${BOOTSTRAP_ROLE_NAME}"

mkdir "$ANSIBLE_HOME"

cp -a "${tmpdir}/${BOOTSTRAP_NAME}/library" "$ANSIBLE_HOME"

for plugin_type in action_modules callback_modules; do
    mkdir -p "${ANSIBLE_HOME}/plugins/${plugin_type}"
    cp -a "${tmpdir}/${BOOTSTRAP_NAME}/${plugin_type}"
    "${ANSIBLE_HOME}/plugins"
done

