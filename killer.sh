#!/bin/bash
kill -HUP `cat app.pid`
kill -9 `cat app.pid`
