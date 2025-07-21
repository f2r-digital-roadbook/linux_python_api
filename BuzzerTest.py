#!/bin/python3

from f2r.gamma import *

# Play SOS ...---... 3 times
#
# This API works with a sequence of operations. There are three valid operations
#
# - PERFORM - Beeps over a period
# - PAUSE - Pauses the beep
# - LOOP - Repeat the previous sequence
# - CANCEL - Cancels immediately the active sequence. For this OP, there is a convenience method cancel.

# BuzzerSample - Parameters
# - op - Operation
# - amplitude - Sound level 0-255
# - duration - Duration in milliseconds

amp = 96 # Sound level form 0 - 254
buzseq = Buzzer( samples = [
            BuzzerSample(op=BuzzerOp.PERFORM, amplitude=amp, duration=125),
            BuzzerSample(op=BuzzerOp.PAUSE, duration=250),
            BuzzerSample(op=BuzzerOp.PERFORM, amplitude=amp, duration=125),
            BuzzerSample(op=BuzzerOp.PAUSE, duration=250),
            BuzzerSample(op=BuzzerOp.PERFORM, amplitude=amp, duration=125),
            BuzzerSample(op=BuzzerOp.PAUSE, duration=250),
            BuzzerSample(op=BuzzerOp.PERFORM, amplitude=amp, duration=250),
            BuzzerSample(op=BuzzerOp.PAUSE, duration=250),
            BuzzerSample(op=BuzzerOp.PERFORM, amplitude=amp, duration=250),
            BuzzerSample(op=BuzzerOp.PAUSE, duration=250),
            BuzzerSample(op=BuzzerOp.PERFORM, amplitude=amp, duration=250),
            BuzzerSample(op=BuzzerOp.PAUSE, duration=250),
            BuzzerSample(op=BuzzerOp.PERFORM, amplitude=amp, duration=125),
            BuzzerSample(op=BuzzerOp.PAUSE, duration=250),
            BuzzerSample(op=BuzzerOp.PERFORM, amplitude=amp, duration=125),
            BuzzerSample(op=BuzzerOp.PAUSE, duration=250),
            BuzzerSample(op=BuzzerOp.PERFORM, amplitude=amp, duration=125),
            BuzzerSample(op=BuzzerOp.PAUSE, duration=1250),
            BuzzerSample(op=BuzzerOp.LOOP, duration=2), # Loop sequence 2 times
        ] )

# Initialize clients
client = GammaClient()

# Cancel previous buzzer sequence...
print(buzseq.cancel(client))

# Perform S.O.S.
print(buzseq.perform(client))
