import pytest
import PythonCharm.Python.yield_training_age.UtillsAge as utills
import PythonCharm.Python.yield_training_age.BaseAge1 as base




# @pytest.mark.parametrize("data_row",data)

def test_age_analyzer():
    list_to_test = base.age_list1
    for row_to_test in list_to_test:
        age = utills.age_parser(row_to_test)
        is_flu = utills.flu_parser(row_to_test)
        results =utills.age_counter(age,is_flu)

# utills.results_parser()

