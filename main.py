#
# Behavior Tree framework for A1 Behavior trees assignment.
# CS131 - Artificial Intelligence
#
# version 1.0.2 - copyright (c) 2023 Santini Fabrizio. All rights reserved.
#

import bt_library as btl

from battery_less_than_30 import BatteryLessThan30
from find_home import FindHome
from go_home import GoHome
from dock import Dock
from dusty_spot import DustySpot

#another root
from spot import Spot
from clean_spot import CleanSpot
from done_spot import DoneSpot

#another root
from general_cleaning import GeneralCleaning

#another root
from clean_floor import CleanFloor

#another root
from done_general import DoneGeneral

#another root
from do_nothing import DoNothing

from globals import BATTERY_LEVEL, GENERAL_CLEANING, SPOT_CLEANING, DUSTY_SPOT_SENSOR, HOME_PATH

# Instantiate the tree according to the assignment. The following are just examples.

# tree_root = btl.Timer(5, FindHome())



battery_tree = btl.Sequence(
    [
        BatteryLessThan30(),
        FindHome(),
        GoHome(),
        Dock()
    ]
)
spot_tree = btl.Sequence(
    [
        Spot(),
        btl.Timer(20, CleanSpot()),
        DoneSpot()
    ]
)


# p

dusty_tree = btl.Sequence(
    [
        DustySpot(),
        btl.Timer(35, CleanSpot())
    ]
)

clean_floor_untilFail = btl.UntilFails(CleanFloor())


dusty_tree.priority = 1
clean_floor_untilFail.priority = 2


lower_priority = btl.Priority(
    [
        dusty_tree,
        clean_floor_untilFail
    ]
)

general_cleaning_subtree = btl.Sequence(
    [
        lower_priority,
        DoneGeneral()
    ]
)

general_cleaning_tree = btl.Sequence(
    [
        GeneralCleaning(),
        general_cleaning_subtree
    ]
)

selection_root = btl.Selection(
    [
        spot_tree,
        general_cleaning_tree
    ]
)
Do_Nothing = DoNothing()


battery_tree.priority = 1
selection_root.priority = 2
Do_Nothing.priority = 3
main_root = btl.Priority(
    [
        battery_tree,
        selection_root,
        Do_Nothing
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
current_blackboard.set_in_environment(SPOT_CLEANING, True)
current_blackboard.set_in_environment(GENERAL_CLEANING, True)
current_blackboard.set_in_environment(DUSTY_SPOT_SENSOR, True)
current_blackboard.set_in_environment(HOME_PATH, "")

cycles = 10
while cycles > 0:
    # Change the environment
    decreased_battery_level = current_blackboard.get_in_environment(BATTERY_LEVEL, 31) - 10
    current_blackboard.set_in_environment(BATTERY_LEVEL, decreased_battery_level)
    result = main_root.run(current_blackboard)
    # Going through the cycles
    cycles = cycles - 1
