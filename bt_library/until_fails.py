#
# Behavior Tree framework for A1 Behavior trees assignment.
# CS131 - Artificial Intelligence
#
# Version 1.0.2 - copyright (c) 2023 Santini Fabrizio. All rights reserved.
#

from .blackboard import Blackboard
from .common import NodeIdType, ResultEnum
from .decorator import Decorator
from .tree_node import TreeNode


class UntilFails(Decorator):
    """
    Specific implementation of the until fails decorator.
    """

    def __init__(self, child: TreeNode):
        """
        Default constructor.
        :param child: Child associated to the decorator
        """
        super().__init__(child)

    def run(self, blackboard: Blackboard) -> ResultEnum:
        """
        Execute the behavior of the node.

        :param blackboard: Blackboard with the current state of the problem
        :return: The result of the execution
        """

        result_child = self.child.run(blackboard)
        if result_child == ResultEnum.FAILED:
            return self.report_succeeded(blackboard)
        return self.report_running(blackboard)



