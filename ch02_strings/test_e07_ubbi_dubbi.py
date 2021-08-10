from e07_a_ubbi_dubbi import ubbi_dubbi
import pytest


@pytest.mark.parametrize('input_word, output_word', [
    ('papaya', 'pubapubayuba'),
    ('elephant', 'ubelubephubant'),
    ('testing', 'tubestubing'),
    ('Banana', 'Bubanubanuba'),
])
def test_simple(input_word, output_word):
    assert ubbi_dubbi(input_word) == output_word
