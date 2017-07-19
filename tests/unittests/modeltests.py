import unittest
from dbudget.model import Category, CategoryGroup, create_budget


class TestCreateBudget(unittest.TestCase):
    def setUp(self):
        self.categories = {'Food': ['Groceries']}

    def test_createBudget_NullObj(self):
        categories = {}

        budget = create_budget(categories)

        self.assertIsNotNone(budget)

    def test_createBudget_withCategories(self):
        budget = create_budget(self.categories)

        self.assertIsNotNone(budget.groups['Food'])


class TestBudget(unittest.TestCase):
    def setUp(self):
        self.categories = {'Food': ['Groceries', 'Dinning out']}
        self.budget = create_budget(self.categories)

    def test_getExpected_defaultValues(self):
        expected_value = self.budget.get_expected('Food', 'Groceries')

        self.assertEquals(expected_value, 0)

    def test_getActual_defaultValues(self):
        actual_value = self.budget.get_actual('Food', 'Groceries')

        self.assertEquals(actual_value, 0)

    def test_setExpected(self):
        self.budget.set_expected('Food', 'Groceries', 1234)

        expected = self.budget.groups['Food'].categories['Groceries'].expected
        self.assertEquals(expected, 1234)

    def test_setActual(self):
        self.budget.set_actual('Food', 'Groceries', 4324)

        actual = self.budget.groups['Food'].categories['Groceries'].actual
        self.assertEquals(actual, 4324)

    def test_budgetToml(self):
        expected = {'Food': {'Dinning out': {'actual': 0, 'expected': 0}, 'Groceries': {'actual': 0, 'expected': 0}}}

        self.assertEquals(expected, self.budget.__toml__())


class TestCategory(unittest.TestCase):
    def setUp(self):
        self.category = Category('any')

    def test_getDifference_nullObj(self):
        diff = self.category.get_difference()

        self.assertEquals(diff, 0)

    def test_getDifference_positive(self):
        self.category.expected = 10

        diff = self.category.get_difference()

        self.assertEquals(diff, 10)

    def test_getDifference_negative(self):
        self.category.actual = 10

        diff = self.category.get_difference()

        self.assertEquals(diff, -10)


class TestCategoryGroup(unittest.TestCase):
    def setUp(self):
        self.category1 = Category('category1')
        self.category2 = Category('category2')
        self.categories_group = CategoryGroup('a group')
        self.categories_group.set_category(self.category1)
        self.categories_group.set_category(self.category2)

    def test_getExpectedTotal_nullObj(self):
        total = self.categories_group.get_expected_total()

        self.assertEquals(total, 0)

    def test_getExpectedTotal(self):
        category = Category('category3', expected=10)
        self.categories_group.set_category(category)

        total = self.categories_group.get_expected_total()

        self.assertEquals(total, 10)

    def test_getActualTotal(self):
        category = Category('category3', actual=11)
        self.categories_group.set_category(category)

        total = self.categories_group.get_actual_total()

        self.assertEquals(total, 11)

    def test_getDifferenceTotal(self):
        category = Category('category3', expected=10, actual=5)
        self.categories_group.set_category(category)

        total = self.categories_group.get_difference_total()

        self.assertEquals(total, 5)
