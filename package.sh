#!/bin/bash
rm -rf dist/
rm -rf build/
rm -rf autox.egg-info/
python3 setup.py bdist_wheel
twine upload dist/*
