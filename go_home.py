#
# Behavior Tree framework for A1 Behavior trees assignment.
# CS131 - Artificial Intelligence
#
# Version 1.0.2 - copyright (c) 2023 Santini Fabrizio. All rights reserved.
# editted by Abdulrahman (Labib Afia)

import bt_library as btl
from globals import HOME_PATH


class GoHome(btl.Task):
    """
    Implementation of the Task "Go Home".
    """
    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:
        directions = blackboard.get_in_environment(HOME_PATH, "")
        self.print_message("Going home: " + directions)

        return self.report_succeeded(blackboard)