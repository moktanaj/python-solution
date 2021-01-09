import analysis as ana
import pytest
import pandas as pd
from pandas.testing import assert_frame_equal


@pytest.fixture
def test_data_df():
    lst1 = ['China', 'USA', 'Nepal', 'China', 'Nepal', 'Australia', 'China', 'USA', 'Nepal', 'Australia']
    lst2 = ['1.12.11', '1.13.3', '1.18.1', '1.12.11', '1.18.1', '1.18.6', '1.18.2', '1.18.2', '1.18.1', '1.18.6']
    lst3 = ['Google Play', 'iOS', 'Google Play', 'Google Play', 'iOS', 'Google Play', 'iOS', 'Google Play',
            'Google Play', 'iOS']
    lst4 = ['cn.xender', 'com.android.chrome', 'com.android.packageinstaller', 'com.android.vending',
            'com.baidu.searchbox', 'cn.xender', 'com.android.vending', 'iTune', '123', '345']
    return pd.DataFrame(list(zip(lst1, lst2, lst3, lst4)), columns=['geo_country', 'app_version',
                                                                    'sku', 'install_source'])


def test_country_app_used_count(test_data_df):
    expected_data = {'geo_country': ['China', 'Nepal', 'Australia', 'USA'], 'count': [3, 3, 2, 2]}
    expected_df = pd.DataFrame(expected_data)
    actual_df = ana.country_app_used_count(test_data_df)
    assert_frame_equal(expected_df, actual_df)


def test_country_app_version_used_count(test_data_df):
    expected_data = {'app_version': ['1.12.11', '1.13.3', '1.18.1', '1.18.2','1.18.2', '1.18.6'],
                     'geo_country': ['China', 'USA', 'Nepal', 'China', 'USA', 'Australia'],
                     'count': [2, 1, 3, 1, 1, 2]}
    expected_df = pd.DataFrame(expected_data)
    actual_df = ana.country_app_version_used_count(test_data_df)
    assert_frame_equal(expected_df, actual_df)


def test_app_downloaded_src(test_data_df):
    expected_data = {'sku': ['Google Play', 'iOS'], 'count': [6, 4]}
    expected_df = pd.DataFrame(expected_data)
    actual_df = ana.app_downloaded_src(test_data_df)
    assert_frame_equal(expected_df, actual_df)


def test_app_installed_sources(test_data_df):
    expected_data = {'install_source': ['cn.xender', 'com.android.chrome', 'com.android.packageinstaller',
                                        'com.android.vending', 'com.baidu.searchbox', 'iTune'],
                     'count': [2, 1, 1, 2, 1, 1]}
    expected_df = pd.DataFrame(expected_data)
    actual_df = ana.app_installed_sources(test_data_df)
    assert_frame_equal(expected_df, actual_df)






