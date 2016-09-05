Ansible Role: nginx
===================

[![Build Status](https://travis-ci.org/BaxterStockman/ansible-role-nginx.svg?branch=master)](https://travis-ci.org/BaxterStockman/ansible-role-nginx)

An Ansible role for managing the NGINX webserver

Role Variables
--------------

```yaml
### From defaults/main.yml:
nginx_config_homedir: /etc/nginx
nginx_config_dest: "{{ nginx_config_homedir }}/nginx.conf"

nginx_user: root
nginx_group: root
nginx_config_file_mode: '0644'

# For the `service` module
nginx_service_name: nginx

### Other variables; most are 'omit' by default:

# For the `stat` module
follow: "{{ nginx_config_follow | default(omit) }}"

# For the `service` module
arguments: "{{ nginx_service_arguments | default(omit) }}"
enabled: "{{ nginx_service_enabled | default(omit) | bool }}"
pattern: "{{ nginx_service_pattern | default(omit) }}"
runlevel: "{{ nginx_service_runlevel | default(omit) }}"
sleep: "{{ nginx_service_sleep | default(omit) }}"
# The `service` module is only invoked when this is defined, and the NGINX
# service is only restarted when this is true.
enabled: "{{ nginx_service_enabled }}"
```

Dependencies
------------

This role requires the
[`nginxparser`](https://github.com/fatiherikli/nginxparser) Python library to
be installed on target machines.  This library is included with the
[`certbot`](https://github.com/certbot/certbot) project, which is available
through some distributions' package management systems -- at least, it's
available on Arch Linux as `certbot-nginx`.

Example Playbook
----------------

Please see [`tests/test.yml`](tests/tests.yml) for example usage.

Rather than limit your ability to customize the NGINX configuration file as you
see fit, this role provides an `nginx_config` task that can be used from your
playbook once you include the `nginx` role:

```yaml
- hosts: all
  roles:
    role: nginx
  tasks:
    nginx_config:
      # Settings here...
```

License
-------

GPLv3

Author Information
------------------

[Matt Schreiber](https://github.com/BaxterStockman)
