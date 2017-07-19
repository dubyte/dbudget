from dbudget.controller import BudgetStateMachine, App
import unittest


class TestBudgetStateMachine(unittest.TestCase, BudgetStateMachine):
    def setUp(self):
        BudgetStateMachine.__init__(self)

    def test_initialState(self):
        self.assertTrue(self.is_BudgetSelection())

    def test_selectBudget(self):
        self.select_budget()

        self.assertTrue(self.is_BudgetDisplay())

    def test_EditCategory(self):
        self.state = 'BudgetDisplay'

        self.edit_category()

        self.assertTrue(self.is_CategoryEdition())

    def test_CloseCategory(self):
        self.state = 'CategoryEdition'

        self.close_category()

        self.assertTrue(self.is_BudgetDisplay())

    def test_CloseBudget(self):
        self.state = 'BudgetDisplay'

        self.close_budget()

        self.assertTrue(self.is_BudgetSelection())


class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = App()

