import io
from main import *
from unittest import mock

@mock.patch("main.open_file")
def test_read_csv(mock_close_file_and_exit):
    f = io.StringIO("some initial text data")
    mock_close_file_and_exit.return_value = f
    got_data = read_csv("does_not_exist.csv")
    assert got_data == {}


def test_read_csv_with_file():
    expected_dict = {'0': {'user_pseudo_id': '0', 'First': 'John', 'Last': 'Doe', 'Age': '55', 'Country': 'USA'}, '1': {'user_pseudo_id': '1', 'First': 'Ajay', 'Last': 'Moktan', 'Age': '35', 'Country': 'AUS'}}
    got_data = read_csv("data/test_csv_correct.csv")
    assert expected_dict == got_data
    got_data = read_csv("data/test_csv.csv")
    assert got_data == {}


@mock.patch("main.sys.exit")
def test_close_file_and_exit(mock_sys_exit):

    # Testing happy path
    close_file_and_exit(None, "example file")
    mock_sys_exit.assert_called_with(1)
    # Testing with incorrect file handler path
    close_file_and_exit("incorrect file", "example file")
    mock_sys_exit.assert_called_with(1)



def test_open_file_with_correct_file():
    file_path = "data/test_csv.csv"
    file = open_file(file_path, 'r')
    assert file.name == file_path


@mock.patch("main.close_file_and_exit")
def test_open_file_with_incorrect_file(mock_close_file_and_exit):
    file_path = "does_not_exist_test_file.csv"
    error_message = "Error in file operation [Errno 2] No such file or directory: '{}'".format(file_path)
    open_file(file_path, 'r')

    mock_close_file_and_exit.assert_called_with(None, error_message)
