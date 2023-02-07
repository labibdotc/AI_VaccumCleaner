#
# Behavior Tree framework for A1 Behavior trees assignment.
# CS131 - Artificial Intelligence
#
# Version 1.0.2 - copyright (c) 2023 Santini Fabrizio. All rights reserved.
# editted by Abdulrahman (Labib Afia)

import bt_library as btl
from globals import HOME_PATH


class CleanFloor(btl.Task):
    """
    Implementation of the Task "Clean Floor".
    """
    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:
        self.print_message("Cleaning floor...")
        x = input("Does floor need cleaning? ('yes','no')")

        return self.report_succeeded(blackboard) \
        if x == 'yes' \
        else self.report_failed(blackboard)