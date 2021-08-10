import e05_pig_latin as pl
import pytest


@pytest.mark.parametrize('input_word, output_word', [
    ('computer', 'omputercay'),
    ('table', 'abletay'),
    ('papaya', 'apayapay'),
    ('elephant', 'elephantway'),
    ('octopus', 'octopusway'),
    ('insightful', 'insightfulway')])
def test_simple(input_word, output_word):
    assert pl.pig_latina(input_word) == output_word


