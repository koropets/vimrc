#!/bin/bash
set -e
bundle_dir=`dirname $0`/../bundle
cd "$bundle_dir"
if [ -d $bundle_dir ]
then
    git clone https://github.com/davidhalter/jedi-vim.git
fi
sudo pip3 install jedi
