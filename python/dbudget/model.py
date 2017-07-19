class Budget(object):
    def __init__(self):
        self.groups = {}

    def add_category_group(self, category_group):
        self.groups[category_group.name] = category_group

    def get_expected(self, group_name, category_name):
        category = self._get_category(group_name, category_name)
        return category.expected

    def get_actual(self, group_name, category_name):
        category = self._get_category(group_name, category_name)
        return category.actual

    def _get_category(self, group_name, category_name):
        return self.groups.get(group_name).get_category(category_name)

    def set_expected(self, group_name, category_name, expected):
        category = self._get_category(group_name, category_name)
        category.expected = expected
        self.groups[group_name].set_category(category)

    def set_actual(self, group_name, category_name, actual):
        category = self._get_category(group_name, category_name)
        category.actual = actual
        self.groups[group_name].set_category(category)

    def __toml__(self):
        result = {}
        for group_name in self.groups:
            result[group_name] = self.groups[group_name].__toml__()

        return result


class CategoryGroup(object):

    def __init__(self, name):
        self.name = name
        self.categories = {}

    def set_category(self, category):
        self.categories[category.name] = category

    def get_category(self, name):
        return self.categories.get(name)

    def get_expected_total(self):
        return reduce(lambda x, y: x+y, [c.expected for c in self.categories.values()])

    def get_actual_total(self):
        return reduce(lambda x, y: x+y, [c.actual for c in self.categories.values()])

    def get_difference_total(self):
        return reduce(lambda x, y: x+y, [c.get_difference() for c in self.categories.values()])

    def __toml__(self):
        result = {}
        for category_name in self.categories:
            result[category_name] = self.categories[category_name].__toml__()
        return result


class Category(object):
    def __init__(self, name, expected=0, actual=0):
        self.name = name
        self.expected = expected
        self.actual = actual

    def get_difference(self):
        return self.expected - self.actual

    def __toml__(self):
        result = {'expected': self.expected, 'actual': self.actual}
        return result


def create_budget(categories_groups):
    budget = Budget()
    for group_name in categories_groups:
        group = _create_category_group(group_name, categories_groups[group_name])
        budget.add_category_group(group)
    return budget


def _create_category_group(group_name, categories):
    group = CategoryGroup(group_name)
    for category_name in categories:
        category = _create_category(category_name)
        group.set_category(category)
    return group


def _create_category(name, expected=0, actual=0):
    return Category(name, expected, actual)
