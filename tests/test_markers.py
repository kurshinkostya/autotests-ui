import pytest


@pytest.mark.smoke
def test_smoke_case():
    ...
    
@pytest.mark.regression
def test_regression_case():
    ...
    
@pytest.mark.smoke
class TestSuite:
    @pytest.mark.smoke
    def test_case1(self):
        ...
        
    @pytest.mark.smoke
    def test_case2(self):
        ...
        