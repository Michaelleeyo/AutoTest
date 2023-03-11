#!coding:utf-8
import pytest
import requests
import json
import yaml
import csv
import xlrd


def readJson():
    return json.load(open('login.json', 'r'))['item']


def readYaml():
    with open('login.yaml', 'r') as f:
        return list(yaml.safe_load_all(f))


def readCsv():
    data = list()
    with open('login.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader)
        for item in reader:
            data.append(item)
    return data


def readExcel():
    data = list()
    book = xlrd.open_workbook('login.xls')
    sheet = book.sheet_by_index(0)
    for item in range(1, sheet.nrows):
        data.append(sheet.row_values(item))
    return data


@pytest.mark.parametrize('data', readJson())
def test_json_login(data):
    r = requests.post(
        url=data['request']['url'],
        json=data['request']['body'])
    assert r.json() == data['response'][0]


@pytest.mark.parametrize('data', readYaml())
def test_yaml_login(data):
    r = requests.post(
        url=data['url'],
        json=json.load(data['body']))
    assert r.json() == json.loads(data[2])


@pytest.mark.parametrize('data', readCsv())
def test_csv_login(data):
    r = requests.post(
        url=data[0],
        json=json.loads(data[1]))
    assert r.json() == json.loads(data[2])


@pytest.mark.parametrize('data', readExcel())
def test_excel_login(data):
    r = requests.post(
        url=data[0],
        json=json.loads(data[1]))
    assert r.json() == json.loads(data[2])
