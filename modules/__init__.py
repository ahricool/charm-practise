import glob
import os
def func():
    s=glob.glob(os.path.join("/Users/huazhang/workspace/CharmTest/modules/celery_tutorial", '*.py'))
    yield  s

class Enum(object):

    # @deprecated('Please use aa-common-utilities')
    def __init__(self, all):
        """
            'all' is either a dict that looks like this:
            {'MEMBER_NAME_1': (1, "Member description 1", ...),
             'MEMBER_NAME_2': (2, "Member description 2", ...), ...}
            or a list that looks like this:
            [(1, "Member 1", ...),
             (2, "Member 2", ...), ...]
        """
        if isinstance(all, dict):
            self.all = all.copy()
        else:
            name = lambda desc: re.sub(
                "[^A-Z0-9_]", "X", re.sub(" ", "_", desc.upper()))
            self.all = dict((name(e[1]), e) for e in all)
        self.all_by_value = dict((i[1][0], (i[0],) + i[1][1:])
                                 for i in self.all.items())
        self.all_by_description = dict((i[1][1], (i[1][0],) + (i[0],))
                                       for i in self.all.items())

    # @deprecated('Please use aa-common-utilities')
    def __repr__(self):
        return '<Enum %s>' % ','.join(self.items)

    __str__ = __repr__
    __unicode__ = __repr__

    # @deprecated('Please use aa-common-utilities')
    def __getattr__(self, name):
        return self.all[name][0]

    # @deprecated('Please use aa-common-utilities')
    def __dir__(self):
        return self.all.keys()

    # @deprecated('Please use aa-common-utilities')
    def __call__(self, value):
        value = int(value)
        if value not in self.values:
            raise ValueError()
        return value

    @property
    # @deprecated('Please use aa-common-utilities')
    def choices(self):
        return sorted([v[0:2] for v in self.all.values()], key=lambda c: c[0])

    @property
    # @deprecated('Please use aa-common-utilities')
    def items(self):
        return self.all.keys()

    @property
    # @deprecated('Please use aa-common-utilities')
    def values(self):
        return self.all_by_value.keys()

    # @deprecated('Please use aa-common-utilities')
    def get_value(self, name):
        return self.all[name][0]

    # @deprecated('Please use aa-common-utilities')
    def get_description(self, value):
        return self.all_by_value[value][1]

    # @deprecated('Please use aa-common-utilities')
    def get_extra(self, value):
        return self.all_by_value[value][2:]

    # @deprecated('Please use aa-common-utilities')
    def get_name(self, value):
        return self.all_by_value[value][0]

    # @deprecated('Please use aa-common-utilities')
    def append(self, enum_with_new_values):
        """
        Update the values in `self` with the values in enum_with_new_values,
        returns a new Enum.
        """
        new_dict = self.all.copy()
        new_dict.update(enum_with_new_values.all)
        return Enum(new_dict)

    # @deprecated('Please use aa-common-utilities')
    def get_by_description(self, description):
        """
        Get the enum by its descriptional value.
        :param str description The enum description.
        :rtype: Enum|None
        :return The enum or None when no enum exists with that name.
        """
        descriptions = self.all_by_description
        if description not in descriptions:
            return None
        else:
            return descriptions[description][0]

if __name__=="__main__":
    GP_ANALYTICS_DIMENSION = Enum({
        'COUNTRY': ('country', 'country breakdown'),
        'SOURCE': ('source', 'source breakdown')
    })

    print(GP_ANALYTICS_DIMENSION.SOURCE)


