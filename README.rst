===========================
nethserver-rh-php73-php-fpm
===========================

Configure default installation of PHP 7.3 running on FPM.
The default configuration of FPM is from upstream and has
been customized to listen on port 9003 (template: ``/etc/opt/rh/rh-php73/php-fpm.d/z_nethserver.conf``).

Adding new configuration
========================

If you need a new configuration, simply drop a file inside ``/etc/opt/rh/rh-php73/php-fpm.d/``
directory and execute: ::

    signal-event nethserver-rh-php73-php-fpm-update
