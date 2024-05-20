# -*- coding:utf-8 -*-
from __future__ import annotations

import json
import os
from src.area_codes.convert import convert, fetch_enname, fetch_areacode, fetch_geoxml


def test_convert(mocker):
    mocker.patch('area_codes.convert.fetch_geoxml', return_value=[{
            "行政區名": "臺北市中正區",
            "_x0033_碼郵遞區號": "100",
            "中心點經度": "121.5198839",
            "中心點緯度": "25.03240487",
            "TGOS_URL": "http://tgos.nat.gov.tw/tgos/Web/MetaData/TGOS_MetaData_View.aspx?MID=9C715A5CD330360D355AE105F908B29E&SHOW_BACK_BUTTON=false"
        },
        {
            "行政區名": "臺北市大同區",
            "_x0033_碼郵遞區號": "103",
            "中心點經度": "121.5130417",
            "中心點緯度": "25.06342433",
            "TGOS_URL": "http://tgos.nat.gov.tw/tgos/Web/MetaData/TGOS_MetaData_View.aspx?MID=9C715A5CD330360D355AE105F908B29E&SHOW_BACK_BUTTON=false"
        },
        {
            "行政區名": "臺北市中山區",
            "_x0033_碼郵遞區號": "104",
            "中心點經度": "121.5381597",
            "中心點緯度": "25.06969917",
            "TGOS_URL": "http://tgos.nat.gov.tw/tgos/Web/MetaData/TGOS_MetaData_View.aspx?MID=9C715A5CD330360D355AE105F908B29E&SHOW_BACK_BUTTON=false"
        }])
    mocker.patch('area_codes.convert.fetch_enname', return_value=[[
            "100",
            "臺北市中正區",
            "Zhongzheng Dist., Taipei City"
        ],
        [
            "103",
            "臺北市大同區",
            "Datong Dist., Taipei City"
        ],
        [
            "104",
            "臺北市中山區",
            "Zhongshan Dist., Taipei City"
        ]])
    mocker.patch('area_codes.convert.fetch_areacode', return_value={
        "臺北市中正區": "6300500", "臺北市大同區": "6300600", "臺北市中山區": "6300400"
    })

    result = convert(write_file=False)

    area_1 = {
        "area_code": "104",
        "area_name": "臺北市中山區",
        "county_name": "臺北市",
        "city_name": "中山區",
        "longitude": "121.5381597",
        "latitude": "25.06969917",
        "area_name_en": "Zhongshan Dist., Taipei City",
        "county_en": "Zhongshan Dist.",
        "area_en": "Taipei City",
        "geo_code_103": "6300400"
    }

    assert isinstance(result, dict), "convert should return a dict"
    assert area_1 in result.values(), "The result of convert should contain the area_1 data"


def test_fetch_geoxml():
    _file = os.path.join(os.path.dirname(__file__), "1050812_行政區經緯度(toPost).xml")
    result = fetch_geoxml(_file)

    print(json.dumps(result, indent=2, ensure_ascii=False))

    area_1 = {
        "行政區名": "新竹市北區",
        "_x0033_碼郵遞區號": "300",
        "中心點經度": "120.9491233",
        "中心點緯度": "24.82269542",
        "TGOS_URL": "http://tgos.nat.gov.tw/tgos/Web/MetaData/TGOS_MetaData_View.aspx?MID=9C715A5CD330360D355AE105F908B29E&SHOW_BACK_BUTTON=false"
    }

    assert isinstance(result, list), "open_xml_file should return a list"
    assert area_1 in result, "The result of open_xml_file should contain the area_1 data"


def test_fetch_enname():
    _file = os.path.join(os.path.dirname(__file__), "county_h_10706.xls")
    result = fetch_enname(_file)

    print(json.dumps(result, indent=2, ensure_ascii=False))

    area_1 = [100, '臺北市中正區', 'Zhongzheng Dist., Taipei City']

    assert isinstance(result, list), "open_csv_file should return a list"
    assert area_1 in result, "The result of open_csv_file should contain the area_1 data"


def test_fetch_areacode():
    _file = os.path.join(os.path.dirname(__file__), "行政區代碼表_Taiwan_Geocode.xlsx")
    result = fetch_areacode(_file)

    print(json.dumps(result, indent=2, ensure_ascii=False))

    assert isinstance(result, dict), "open_geo_code_file should return a dict"
    assert result["臺北市內湖區"] == "6301000", "The result of open_geo_code_file should contain the area_1 data"

    print(json.dumps(result, indent=2, ensure_ascii=False))
