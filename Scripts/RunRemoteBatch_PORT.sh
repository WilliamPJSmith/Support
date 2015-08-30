#!/bin/sh

# paths assume we are running from cellmodeller dir
cd ~/cellmodeller

#==================================

# initiate simulation runner with arguments
RUNNER=Scripts/multi_batch.py
MODEL=TTWeek15_2DBinary_aa
NUM_REPEATS=20
DEV_NUM=0

# call runner inside a screen terminal
# this means the process will continue to run when we close the ssh connection
cmpython $RUNNER $MODEL $NUM_REPEATS $DEV_NUM

# initiate simulation runner with arguments
RUNNER=Scripts/multi_batch.py
MODEL=TTWeek15_2DBinary_aa
NUM_REPEATS=20
DEV_NUM=0

# call runner inside a screen terminal
# this means the process will continue to run when we close the ssh connection
cmpython $RUNNER $MODEL $NUM_REPEATS $DEV_NUM

# initiate simulation runner with arguments
RUNNER=Scripts/multi_batch.py
MODEL=TTWeek15_2DBinary_aa
NUM_REPEATS=20
DEV_NUM=0

# call runner inside a screen terminal
# this means the process will continue to run when we close the ssh connection
cmpython $RUNNER $MODEL $NUM_REPEATS $DEV_NUM

# initiate simulation runner with arguments
RUNNER=Scripts/multi_batch.py
MODEL=TTWeek15_2DBinary_aa
NUM_REPEATS=20
DEV_NUM=0

# call runner inside a screen terminal
# this means the process will continue to run when we close the ssh connection
cmpython $RUNNER $MODEL $NUM_REPEATS $DEV_NUM

#==================================

# initiate simulation runner with arguments
RUNNER=Scripts/multi_batch.py
MODEL=TTWeek15_2DBinary_bb
NUM_REPEATS=20
DEV_NUM=0

# call runner inside a screen terminal
# this means the process will continue to run when we close the ssh connection
cmpython $RUNNER $MODEL $NUM_REPEATS $DEV_NUM

# initiate simulation runner with arguments
RUNNER=Scripts/multi_batch.py
MODEL=TTWeek15_2DBinary_bb
NUM_REPEATS=20
DEV_NUM=0

# call runner inside a screen terminal
# this means the process will continue to run when we close the ssh connection
cmpython $RUNNER $MODEL $NUM_REPEATS $DEV_NUM

# initiate simulation runner with arguments
RUNNER=Scripts/multi_batch.py
MODEL=TTWeek15_2DBinary_bb
NUM_REPEATS=20
DEV_NUM=0

# call runner inside a screen terminal
# this means the process will continue to run when we close the ssh connection
cmpython $RUNNER $MODEL $NUM_REPEATS $DEV_NUM

# initiate simulation runner with arguments
RUNNER=Scripts/multi_batch.py
MODEL=TTWeek15_2DBinary_bb
NUM_REPEATS=20
DEV_NUM=0

# call runner inside a screen terminal
# this means the process will continue to run when we close the ssh connection
cmpython $RUNNER $MODEL $NUM_REPEATS $DEV_NUM


#==================================

# initiate simulation runner with arguments
RUNNER=Scripts/multi_batch.py
MODEL=TTWeek15_2DBinary_cc
NUM_REPEATS=20
DEV_NUM=0

# call runner inside a screen terminal
# this means the process will continue to run when we close the ssh connection
cmpython $RUNNER $MODEL $NUM_REPEATS $DEV_NUM

# initiate simulation runner with arguments
RUNNER=Scripts/multi_batch.py
MODEL=TTWeek15_2DBinary_cc
NUM_REPEATS=20
DEV_NUM=0

# call runner inside a screen terminal
# this means the process will continue to run when we close the ssh connection
cmpython $RUNNER $MODEL $NUM_REPEATS $DEV_NUM

# initiate simulation runner with arguments
RUNNER=Scripts/multi_batch.py
MODEL=TTWeek15_2DBinary_cc
NUM_REPEATS=20
DEV_NUM=0

# call runner inside a screen terminal
# this means the process will continue to run when we close the ssh connection
cmpython $RUNNER $MODEL $NUM_REPEATS $DEV_NUM

# initiate simulation runner with arguments
RUNNER=Scripts/multi_batch.py
MODEL=TTWeek15_2DBinary_cc
NUM_REPEATS=20
DEV_NUM=0

# call runner inside a screen terminal
# this means the process will continue to run when we close the ssh connection
cmpython $RUNNER $MODEL $NUM_REPEATS $DEV_NUM

#==================================

# initiate simulation runner with arguments
RUNNER=Scripts/multi_batch.py
MODEL=TTWeek15_2DBinary_dd
NUM_REPEATS=20
DEV_NUM=0

# call runner inside a screen terminal
# this means the process will continue to run when we close the ssh connection
cmpython $RUNNER $MODEL $NUM_REPEATS $DEV_NUM

# initiate simulation runner with arguments
RUNNER=Scripts/multi_batch.py
MODEL=TTWeek15_2DBinary_dd
NUM_REPEATS=20
DEV_NUM=0

# call runner inside a screen terminal
# this means the process will continue to run when we close the ssh connection
cmpython $RUNNER $MODEL $NUM_REPEATS $DEV_NUM

# initiate simulation runner with arguments
RUNNER=Scripts/multi_batch.py
MODEL=TTWeek15_2DBinary_dd
NUM_REPEATS=20
DEV_NUM=0

# call runner inside a screen terminal
# this means the process will continue to run when we close the ssh connection
cmpython $RUNNER $MODEL $NUM_REPEATS $DEV_NUM

# initiate simulation runner with arguments
RUNNER=Scripts/multi_batch.py
MODEL=TTWeek15_2DBinary_dd
NUM_REPEATS=20
DEV_NUM=0

# call runner inside a screen terminal
# this means the process will continue to run when we close the ssh connection
cmpython $RUNNER $MODEL $NUM_REPEATS $DEV_NUM

#==================================

# initiate simulation runner with arguments
RUNNER=Scripts/multi_batch.py
MODEL=TTWeek15_2DBinary_ab
NUM_REPEATS=20
DEV_NUM=0

# call runner inside a screen terminal
# this means the process will continue to run when we close the ssh connection
cmpython $RUNNER $MODEL $NUM_REPEATS $DEV_NUM

# initiate simulation runner with arguments
RUNNER=Scripts/multi_batch.py
MODEL=TTWeek15_2DBinary_ab
NUM_REPEATS=20
DEV_NUM=0

# call runner inside a screen terminal
# this means the process will continue to run when we close the ssh connection
cmpython $RUNNER $MODEL $NUM_REPEATS $DEV_NUM

# initiate simulation runner with arguments
RUNNER=Scripts/multi_batch.py
MODEL=TTWeek15_2DBinary_ab
NUM_REPEATS=20
DEV_NUM=0

# call runner inside a screen terminal
# this means the process will continue to run when we close the ssh connection
cmpython $RUNNER $MODEL $NUM_REPEATS $DEV_NUM

# initiate simulation runner with arguments
RUNNER=Scripts/multi_batch.py
MODEL=TTWeek15_2DBinary_ab
NUM_REPEATS=20
DEV_NUM=0

# call runner inside a screen terminal
# this means the process will continue to run when we close the ssh connection
cmpython $RUNNER $MODEL $NUM_REPEATS $DEV_NUM

#==================================

# when we're done, kill the screen
echo "All done."
