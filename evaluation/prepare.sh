#!/bin/bash
set -e
set -x
dt-easy_logs-download 20160312212935_magitek
filename=`dt-easy_logs-find 20160312212935_magitek`
cp $filename $CHALLENGE_EVALUATION/log0.bag
