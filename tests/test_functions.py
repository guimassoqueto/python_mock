from unittest.mock import patch
from app.utils import get_fullname_and_len


@patch("app.utils.get_user")
def test_get_f_l(mock_get_user):
    mock_get_user.return_value = {"first_name": "Guilherme", "last_name": "Massoqueto"}
    assert get_fullname_and_len() == ("Guilherme Massoqueto", 20)
    assert mock_get_user.called == True

