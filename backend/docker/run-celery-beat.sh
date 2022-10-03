#!/usr/bin/env sh

set -x
set -o errexit
set -o nounset

celery -A crawler beat -l info --pidfile= --scheduler django_celery_beat.schedulers:DatabaseScheduler
