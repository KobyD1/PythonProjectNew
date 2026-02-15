import pytest


@pytest.mark.parametrize("param1", [
    (1),
    (2),
    (3),
])
@pytest.mark.parametrize("param2", [
    (4),
    (5),
    (6),
])
def test_eval(param1, param2):
    print('\n noPom between param1=', param1, 'param2=', param2)


