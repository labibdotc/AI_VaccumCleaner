#
# Behavior Tree framework for A1 Behavior trees assignment.
# CS131 - Artificial Intelligence
#
# Version 1.0.2 - copyright (c) 2023 Santini Fabrizio. All rights reserved.
#

import bt_library as btl
from globals import SPOT_CLEANING


class DoneSpot(btl.Task):
    """
    Implementation of the Task "done Spot".
    """
    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:
        self.print_message("Done spot")
        blackboard.set_in_environment(SPOT_CLEANING, False)

        return self.report_succeeded(blackboard)
