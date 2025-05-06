#!/bin/sh

set -e

rm -rf data

mkdir -p data/wili
wget 'https://zenodo.org/records/841984/files/wili-2018.zip?download=1' -O /tmp/wili.zip
unzip /tmp/wili.zip '*_test.txt' -d data/wili
rm /tmp/wili.zip

mkdir -p data/profiles
wget 'https://github.com/DoodleBears/langdetect/archive/refs/heads/master.zip' -O /tmp/langdetect.zip
unzip -j /tmp/langdetect.zip 'langdetect-master/langdetect/profiles/*' -d data/profiles
rm /tmp/langdetect.zip
