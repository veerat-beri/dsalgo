def check_only_one_elem_is_true(iterable):
    # Ref: https://stackoverflow.com/questions/16801322/how-can-i-check-that-a-list-has-one-and-only-one-truthy-value
    iterator = iter(iterable)
    return any(iterator) and not any(iterator)


def assert_only_one_arg_is_present(error_message: str = None, *args):
    assert check_only_one_elem_is_true(args), error_message
