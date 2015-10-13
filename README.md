Role Name
=========

[![Build Status](https://travis-ci.org/BaxterStockman/ansible-role-nginx.svg?branch=bootstrap_migrate)](https://travis-ci.org/BaxterStockman/ansible-role-nginx)

An Ansible role for managing the NGINX webserver

Role Variables
--------------

```yaml
### From defaults/main.yml:
nginx_homedir: /etc/nginx
nginx_config_dest: "{{ nginx_homedir }}/nginx.conf"

nginx_owner: root
nginx_group: root
nginx_file_mode: '0644'

# For the `service` module
nginx_service_name: nginx

### Other variables; most are 'omit' by default:

# For the `stat` module
follow: "{{ nginx_follow | default(omit) }}"

# For the `service` module
arguments: "{{ nginx_service_arguments | default(omit) }}"
enabled: "{{ nginx_service_enabled | default(omit) | bool }}"
pattern: "{{ nginx_service_pattern | default(omit) }}"
runlevel: "{{ nginx_service_runlevel | default(omit) }}"
sleep: "{{ nginx_service_sleep | default(omit) }}"
# The `service` module is only invoked when this is defined, and the NGINX
service is only restarted when this is true.
enabled: "{{ nginx_service_enabled }}"
```

Dependencies
------------

This role requires the
[`bootstrap`](https://github.com/BaxterStockman/bootstrap) Ansible module in
order to temporarily install the
[`nginxparser`](https://github.com/fatiherikli/nginxparser) Python library,
which it uses to manage the NGINX configuration file.

Example Playbook
----------------

Please see [`test/playbook.yml`](test/playbook.yml) for example usage.

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

This module restarts the NGINX service if and only if the configuration file
has changed during the course of the play, and `nginx_service_enable` is true.

License
-------

GPLv3

Author Information
------------------

[Matt Schreiber](https://github.com/BaxterStockman)
