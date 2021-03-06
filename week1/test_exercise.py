import exercise
import pytest

def test_get_rad():
    assert round(exercise.get_rad(1,0,0,1),2) == 1.57
    assert round(exercise.get_rad(1,0,1,0),2) == 0
    assert round(exercise.get_rad(1,0,-1,0),2) == 3.14
    assert round(exercise.get_rad(1,0,0,-1),2) == 1.57
    with pytest.raises(RuntimeError):
        exercise.get_rad(0,0,0,0)
