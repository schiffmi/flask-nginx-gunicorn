#!/bin/bash
gunicorn flaskapp:app app.pid -D
