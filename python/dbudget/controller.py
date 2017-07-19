from transitions import Machine
from cmd2 import cmd


class BudgetStateMachine(object):

    def __init__(self):
        states = ['BudgetSelection', 'BudgetDisplay', 'CategoryEdition']
        transitions = [
            {'trigger': 'select_budget', 'source': 'BudgetSelection', 'dest': 'BudgetDisplay'},
            {'trigger': 'edit_category', 'source': 'BudgetDisplay', 'dest': 'CategoryEdition'},
            {'trigger': 'close_category', 'source': 'CategoryEdition', 'dest': 'BudgetDisplay'},
            {'trigger': 'close_budget', 'source': 'BudgetDisplay', 'dest': 'BudgetSelection'},
        ]

        Machine(model=self, initial='BudgetSelection', states=states, transitions=transitions)


class App(cmd.Cmd, BudgetStateMachine):
    def __init__(self):
        cmd.Cmd.__init__(self)
        BudgetStateMachine.__init__(self)
