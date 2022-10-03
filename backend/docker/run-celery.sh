#!/usr/bin/env sh

set -x
set -o errexit
set -o nounset

celery -A crawler worker -l info -n worker-1
