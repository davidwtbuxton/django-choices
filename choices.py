class Choices(object):
    """Helper for storing enumerable Django choices. Takes a sequence of
    (name, label) pairs. Idea copied from https://github.com/adamalton/django-choices

    >>> status = c.Choices([('new', 'new'), ('complete', 'code complete')])
    >>> status.new, status.complete
    ('new', 'complete')
    >>> status.new == 'new'
    True
    >>> status.choices
    (('new', 'new'), ('complete', 'code complete'))
    >>> status.finished = 'finished'
    Traceback (most recent call last):
        ...
    AttributeError: 'Choices' object does not permit assigning attribute 'finished'
    """
    def __init__(self, pairs):
        _choices = tuple(pairs)
        _names = tuple(name for name, value in _choices)

        self.__dict__['_choices'] = _choices
        self.__dict__['_names'] = _names

        for name in _names:
            if hasattr(self, name):
                raise ValueError('Cannot use reserved name %r' % name)

        for name in _names:
            self.__dict__[name] = name

    def __setattr__(self, name, value):
        message = '%r object does not permit assigning attribute %r'
        raise AttributeError(message % (self.__class__.__name__, name))

    def __iter__(self):
        return iter(self._names)

    @property
    def choices(self):
        return self._choices

    @property
    def constants(self):
        return self._names

