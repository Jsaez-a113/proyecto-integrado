#!/bin/bash

# Install dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --noinput

# Note: Migrations should be run manually after deployment
# using Vercel CLI or from a local environment connected to production DB
