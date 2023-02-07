#
# Behavior Tree framework for A1 Behavior trees assignment.
# CS131 - Artificial Intelligence
#
# Version 1.0.2 - copyright (c) 2023 Santini Fabrizio. All rights reserved.
# editted by Abdulrahman (Labib Afia)

import bt_library as btl
from globals import BATTERY_LEVEL


class Dock(btl.Task):
    """
    Implementation of the Task "Dock".
    """
    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:
        self.print_message("Docking...")
        blackboard.set_in_environment(BATTERY_LEVEL, 100)
        self.print_message("Battery fully charged...")

        return self.report_succeeded(blackboard)