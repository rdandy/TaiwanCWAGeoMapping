# -*- coding:utf-8 -*-
from __future__ import annotations

import pytest
import requests
from unittest.mock import patch
from src.area_codes import convert


@patch('requests.get')
def test_fetch_geoxml_returns_expected_result(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.content = b'<xml></xml>'
    result = convert.fetch_geoxml('http://test.com')
    assert result == []

@patch('requests.get')
def test_fetch_geoxml_handles_file_not_found(mock_get):
    mock_get.return_value.status_code = 404
    with pytest.raises(SystemExit):
        convert.fetch_geoxml('http://test.com')

@patch('requests.get')
def test_fetch_enname_returns_expected_result(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.content = b'<xml></xml>'
    result = convert.fetch_enname('http://test.com')
    assert result == []

@patch('requests.get')
def test_fetch_enname_handles_file_not_found(mock_get):
    mock_get.return_value.status_code = 404
    with pytest.raises(SystemExit):
        convert.fetch_enname('http://test.com')

@patch('requests.get')
def test_fetch_areacode_returns_expected_result(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.content = b'<xml></xml>'
    result = convert.fetch_areacode('http://test.com')
    assert result == {}

@patch('requests.get')
def test_fetch_areacode_handles_file_not_found(mock_get):
    mock_get.return_value.status_code = 404
    with pytest.raises(SystemExit):
        convert.fetch_areacode('http://test.com')

@patch('convert.fetch_geoxml')
@patch('convert.fetch_enname')
@patch('convert.fetch_areacode')
def test_convert_returns_expected_result(mock_areacode, mock_enname, mock_geoxml):
    mock_geoxml.return_value = [{'_x0033_碼郵遞區號': '100', '行政區名': 'test'}]
    mock_enname.return_value = [['100', 'test', 'Test']]
    mock_areacode.return_value = {'test': {'geo_code_103': '6300500'}}
    result = convert.convert()
    assert result == {'1': {'zip_code': '100', 'area_name': 'test', 'area_name_en': 'Test', 'geo_code_103': '6300500', 'county_name': '', 'county_name_en': '', 'county_geo_code_103': '', 'county_full_name': '', 'city_name': '', 'city_name_en': '', 'longitude': 0.0, 'latitude': 0.0}}