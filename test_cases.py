from client.ena_cram import enaCRAM
import pytest

ena = enaCRAM()

# test with good MD5 string
def test_for_valid():
    sid = "3050107579885e1608e6fe50fae3f8d0"
    assert ena.validate_sid(sid)

def test_for_value_err():
    sid = "an invalid string"
    with pytest.raises(Exception) as e:
        ena.validate_sid(sid)

def test_for_type_err():
    sid = 1234567890
    with pytest.raises(Exception) as e:
        ena.validate_sid(sid)