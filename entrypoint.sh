#!/bin/bash
set -e

# Optional: Add custom initialization steps here

# For example, a database migration step
# echo "Running database migrations..."
# python manage.py migrate

# Execute the command passed to the container
exec "$@"
