#!/bin/bash
if pip list | grep 'pytest'; then
    echo "Pytest installed"
else
    pip install pytest
    echo "Pytest now installed"
fi

pytest test.py