# Taiwan (include outlying islands) Area Code Processor

This module provides a set of tools for automating the download, processing, and integration of administrative district data for Taiwan and its outlying islands (including Kinmen, Matsu, Penghu, etc.). The data includes the latitude and longitude of administrative districts, Chinese-English name comparisons, and administrative district codes. The final output is a `AREA_CODES.json` file containing information on all administrative districts, aimed at providing a convenient, unified solution for users in need of administrative district information for Taiwan and its outlying islands.

For detailed information on Central Meteorological Administration data conversion, please click the link below to view more detailed instructions.

- [Central Meteorological Administration Data Conversion](https://alerts.ncdr.nat.gov.tw/CAPfiledownload.aspx)

## Features

- Automatically download the latest administrative district latitude and longitude data, Chinese-English name comparison tables, and administrative district code tables for Taiwan and its outlying islands from official websites.
- Parse downloaded XML, .xls (old version of Excel) and .xlsx (new version of Excel) files to extract relevant information.
- The extracted information is integrated to generate structured JSON files for API connection and service development, with the purpose of maintaining data consistency with the administrative region of the platform.

## Getting Started

### Prerequisites

- Python 3.11+
- requests

### Installing Dependencies

Execute the following command in the terminal to install the required Python packages:

```bash
pip install -r requirements.txt
```

### How to update AREA_CODES.json?

Use the following command to run the program:

```bash
source venv/bin/activate
python src/area_codes/convert.py
```

### Optional Parameters

The program supports the following command-line parameters for specifying the paths of data files and the name of the output file:

- `-g` or `--geoxml`: Specifies the path or URI to the GeoXML file containing administrative district latitude and longitude data.
- `-a` or `--areacode`: Specifies the path to the Excel file containing administrative district codes.
- `-e` or `--enname`: Specifies the path to the XLS file containing Chinese-English name comparisons for administrative districts.
- `-o` or `--outfile`: Specifies the name of the output JSON file.

Usage:

```bash
python src/area_codes/convert.py [-g Path to GeoXML file] [-a Path to administrative district code file] [-e Path to Chinese-English comparison file] [-o Name of output JSON file]
```

## JSON Data Format
The data is stored in a JSON file. Each entry in the JSON file contains the following fields:

```json
{
    "1": {
        "zip_code": "100",
        "area_name": "臺北市中正區",
        "area_name_en": "Zhongzheng Dist., Taipei City",
        "geo_code_103": "6300500",
        "county_name": "臺北市",
        "county_name_en": "Taipei City",
        "county_geo_code_103": "63",
        "county_full_name": "臺北市",
        "city_name": "中正區",
        "city_name_en": "Jhongjhen District",
        "longitude": 121.5198839,
        "latitude": 25.03240487
    },
    "2": {
        "zip_code": "103",
        "area_name": "臺北市大同區",
        "area_name_en": "Datong Dist., Taipei City",
        "geo_code_103": "6300600",
        "county_name": "臺北市",
        "county_name_en": "Taipei City",
        "county_geo_code_103": "63",
        "county_full_name": "臺北市",
        "city_name": "大同區",
        "city_name_en": "Datong District",
        "longitude": 121.5130417,
        "latitude": 25.06342433
    },    
    ...
}
```

## Fields
- `Key` (string): The serial number of the data.
  - `zip_code` (string): The zip code of the area.
  - `area_name` (string): The Chinese name of the area.
  - `area_name_en` (string): English name of the area.
  - `geo_code_103` (string): Area code table (Taiwan_code_103)
  - `county_name` (string): The Chinese name of the township/town.
  - `county_name_en` (string): English name of the county/town.
  - `county_geo_code_103` (string): Area code table for county (Taiwan_code_103)
  - `county_full_name` (string): The full name of the county/town.
  - `city_name` (string): The city name.
  - `city_name_en` (string): English name of the city.
  - `longitude` (string): The longitude of the center area.
  - `latitude` (string): The latitude of the center area.


# Future Work

## Update test case

----

## API Endpoints

Hope to continue to implement the following api

### URIs
* https://{{host}}:{{port}}/allareas

    List all administrative areas

* https://{{host}}:{{port}}/get_data_by_zip_code/{{zip_code}}

    Obtain administrative area information by postal code

* https://{{host}}:{{port}}/get_geo_103_by_zip_code/{{zip_code}}

    Get GEO_103 encoding data by zip code

* https://{{host}}:{{port}}/get_data_by_latlng/{{latitude}}/{{longitude}}

    Get the nearest administrative area data by latitude and longitude

### Request Method
GET

### Request Parameters
None

### Response Body
The response will return a JSON object

```json
[
    {
        "id": 1,
        "zip_code": "100",
        "area_name": "臺北市中正區",
        "area_name_en": "Zhongzheng Dist., Taipei City",
        "geo_code_103": "6300500",
        "county_name": "臺北市",
        "county_name_en": "Taipei City",
        "county_geo_code_103": "63",
        "county_full_name": "臺北市",
        "city_name": "中正區",
        "city_name_en": "Jhongjhen District",
        "longitude": 121.5198839,
        "latitude": 25.03240487
    },
    {
        "id", 2,
        "zip_code": "103",
        "area_name": "臺北市大同區",
        "area_name_en": "Datong Dist., Taipei City",
        "geo_code_103": "6300600",
        "county_name": "臺北市",
        "county_name_en": "Taipei City",
        "county_geo_code_103": "63",
        "county_full_name": "臺北市",
        "city_name": "大同區",
        "city_name_en": "Datong District",
        "longitude": 121.5130417,
        "latitude": 25.06342433
    },
    ...
]
```

### Response Fields
- Response data containing the following fields:
  - `id` (int): The serial number of the data.
  - `zip_code` (string): The zip code of the area.
  - `area_name` (string): The Chinese name of the area.
  - `area_name_en` (string): English name of the area.
  - `geo_code_103` (string): Area code table (Taiwan_code_103)
  - `county_name` (string): The Chinese name of the township/town.
  - `county_name_en` (string): English name of the county/town.
  - `county_geo_code_103` (string): Area code table for county (Taiwan_code_103)
  - `county_full_name` (string): The full name of the county/town.
  - `city_name` (string): The city name.
  - `city_name_en` (string): English name of the city.
  - `longitude` (string): The longitude of the center area.
  - `latitude` (string): The latitude of the center area.

----

## Module that can be used by direct internal calls

### CwaCAP
