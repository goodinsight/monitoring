@echo off
conda activate monitoring
$env:FLASK_APP = "pybo"
$env:FLASK_DEBUG = true