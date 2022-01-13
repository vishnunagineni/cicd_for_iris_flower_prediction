import pytest
class NotInRange(Exception):
    def __init__(self,message="value not in Range"):
        self.message=message
        super().__init__(self.message)
def test_gen():
    a=10
    with pytest.raises(NotInRange):
        if a not in range(15,20):
            raise NotInRange