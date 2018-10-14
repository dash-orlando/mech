#!/bin/bash
#################
# Installation
#################

## Updating Raspbian Software
echo ">> Updating OS"
sudo apt-get update -y

## Install python-dev
echo ">> Install Additional Packages and Modules"
sudo apt-get install build-essential python-dev python-pip

## Cloning Adafruit Raspberry Pi HAT Repo
echo ">> Cloning Repository"
sudo git clone https://github.com/adafruit/Adafruit-Motor-HAT-Python-Library.git

## Install
echo ">> Installing Python Library"
cd Adafruit-Motor-HAT-Python-Library
sudo python setup.py install

## Done
echo ">> DONE!"

