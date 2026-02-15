# find the nearest  number by dived
# for example (47,5 return 45, 69,5 return 70)
# assert of lower or higher num found
import pytest


@pytest.mark.parametrize(
    'base_number, ref_dived',
    [
        (46, 5),
        (69, 5),
        (76, 7),
        (108, 9)

    ])
def test_near_not_include(base_number, ref_dived):
    print('\n #start test for', base_number, 'ref number=', ref_dived)
    # near.test_divied_by(base_number, ref_dived)
