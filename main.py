#
# Behavior Tree framework for A1 Behavior trees assignment.
# CS131 - Artificial Intelligence
#
# version 1.0.2 - copyright (c) 2023 Santini Fabrizio. All rights reserved.
#

import bt_library as btl

from battery_less_than_30 import BatteryLessThan30
from find_home import FindHome
from globals import BATTERY_LEVEL, GENERAL_CLEANING, SPOT_CLEANING, DUSTY_SPOT_SENSOR, HOME_PATH

# Instantiate the tree according to the assignment. The following are just examples.

# tree_root = btl.Timer(5, FindHome())

tree_root = btl.Sequence(
    [
        BatteryLessThan30(),
        btl.Timer(10, FindHome())
    ]
)

# tree_root = btl.Sequence(
#     [
#         BatteryLessThan30(),
#         FindHome()
#     ]
# )

# Main body of the assignment
current_blackboard = btl.Blackboard()
current_blackboard.set_in_environment(BATTERY_LEVEL, 29)
current_blackboard.set_in_environment(SPOT_CLEANING, False)
current_blackboard.set_in_environment(GENERAL_CLEANING, True)
current_blackboard.set_in_environment(DUSTY_SPOT_SENSOR, False)
current_blackboard.set_in_environment(HOME_PATH, "")

cycles = 10
while cycles > 0:
    # Change the environment

    # Evaluating the tree
    result = tree_root.run(current_blackboard)

    # Going through the cycles
    cycles = cycles - 1
