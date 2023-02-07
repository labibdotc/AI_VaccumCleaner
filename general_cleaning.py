#
# Behavior Tree framework for A1 Behavior trees assignment.
# CS131 - Artificial Intelligence
#
# Version 1.0.2 - copyright (c) 2023 Santini Fabrizio. All rights reserved.
#

import bt_library as btl
from globals import GENERAL_CLEANING


class GeneralCleaning(btl.Condition):
    """
    Implementation of the condition "General Cleaning".
    """
    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:
        self.print_message("Checking for general cleaning")

        return self.report_succeeded(blackboard) \
            if blackboard.get_in_environment(GENERAL_CLEANING, False) == True \
            else self.report_failed(blackboard)
