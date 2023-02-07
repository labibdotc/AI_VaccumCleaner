#
# Behavior Tree framework for A1 Behavior trees assignment.
# CS131 - Artificial Intelligence
#
# Version 1.0.2 - copyright (c) 2023 Santini Fabrizio. All rights reserved.
#

import bt_library as btl
from globals import DUSTY_SPOT_SENSOR


class DustySpot(btl.Condition):
    """
    Implementation of the condition "dusty spot".
    """
    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:
        self.print_message("Checking for spot")
        x = input("Is there a dusty spot? ('yes','no')")
        blackboard.set_in_environment(DUSTY_SPOT_SENSOR, x == 'yes')

        return self.report_succeeded(blackboard) \
            if blackboard.get_in_environment(DUSTY_SPOT_SENSOR, True) == True \
            else self.report_failed(blackboard)
