#
# Behavior Tree framework for A1 Behavior trees assignment.
# CS131 - Artificial Intelligence
#
# Version 1.0.2 - copyright (c) 2023 Santini Fabrizio. All rights reserved.
#

import bt_library as btl
from globals import GENERAL_CLEANING


class DoneGeneral(btl.Task):
    """
    Implementation of the Task "done general".
    """
    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:
        self.print_message("Done General cleaning")
        blackboard.set_in_environment(GENERAL_CLEANING, False)

        return self.report_succeeded(blackboard)
