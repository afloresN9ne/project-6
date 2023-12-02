"""
Nose tests for acp_times.py

Write your tests HERE AND ONLY HERE.
"""

import nose    # Testing framework
import logging
import arrow
from acp_times import open_time,close_time 
logging.basicConfig(format='%(levelname)s:%(message)s',
                    level=logging.WARNING)
log = logging.getLogger(__name__)

def test_200():
    #min brevet case (same for every first test case)
    assert open_time(0,200,arrow.get('2021-01-01T00:00')).format('YYYY-MM-DDTHH:mm') ==arrow.get('2021-01-01T00:00').format('YYYY-MM-DDTHH:mm')
    assert close_time(0,200,arrow.get('2021-01-01T00:00')).format('YYYY-MM-DDTHH:mm') ==arrow.get('2021-01-01T01:00').format('YYYY-MM-DDTHH:mm')
    
    #max brevet case (same for every 2nd test case)
    assert open_time(200,200,arrow.get('2021-01-01T00:00')).format('YYYY-MM-DDTHH:mm') ==arrow.get('2021-01-01T05:53').format('YYYY-MM-DDTHH:mm')
    assert close_time(200,200,arrow.get('2021-01-01T00:00')).format('YYYY-MM-DDTHH:mm') ==arrow.get('2021-01-01T13:30').format('YYYY-MM-DDTHH:mm')

def test_300():
    assert open_time(0,300,arrow.get('2021-01-01T00:00')).format('YYYY-MM-DDTHH:mm') ==arrow.get('2021-01-01T00:00').format('YYYY-MM-DDTHH:mm')
    assert close_time(0,300,arrow.get('2021-01-01T00:00')).format('YYYY-MM-DDTHH:mm') ==arrow.get('2021-01-01T01:00').format('YYYY-MM-DDTHH:mm')

    assert open_time(300,300,arrow.get('2021-01-01T00:00')).format('YYYY-MM-DDTHH:mm') ==arrow.get('2021-01-01T09:00').format('YYYY-MM-DDTHH:mm')
    assert close_time(300,300,arrow.get('2021-01-01T00:00')).format('YYYY-MM-DDTHH:mm') ==arrow.get('2021-01-01T20:00').format('YYYY-MM-DDTHH:mm')

def test_400():
    assert open_time(0,400,arrow.get('2021-01-01T00:00')).format('YYYY-MM-DDTHH:mm') ==arrow.get('2021-01-01T00:00').format('YYYY-MM-DDTHH:mm')
    assert close_time(0,400,arrow.get('2021-01-01T00:00')).format('YYYY-MM-DDTHH:mm') ==arrow.get('2021-01-01T01:00').format('YYYY-MM-DDTHH:mm')

    assert open_time(400,400,arrow.get('2021-01-01T00:00')).format('YYYY-MM-DDTHH:mm') ==arrow.get('2021-01-01T12:08').format('YYYY-MM-DDTHH:mm')
    assert close_time(400,400,arrow.get('2021-01-01T00:00')).format('YYYY-MM-DDTHH:mm') ==arrow.get('2021-01-02T03:00').format('YYYY-MM-DDTHH:mm')
def test_600():
    assert open_time(0,600,arrow.get('2021-01-01T00:00')).format('YYYY-MM-DDTHH:mm') ==arrow.get('2021-01-01T00:00').format('YYYY-MM-DDTHH:mm')
    assert close_time(0,600,arrow.get('2021-01-01T00:00')).format('YYYY-MM-DDTHH:mm') ==arrow.get('2021-01-01T01:00').format('YYYY-MM-DDTHH:mm')

    assert open_time(600,600,arrow.get('2021-01-01T00:00')).format('YYYY-MM-DDTHH:mm') ==arrow.get('2021-01-01T18:48').format('YYYY-MM-DDTHH:mm')
    assert close_time(600,600,arrow.get('2021-01-01T00:00')).format('YYYY-MM-DDTHH:mm') ==arrow.get('2021-01-02T16:00').format('YYYY-MM-DDTHH:mm')
def test_1000():
    assert open_time(0,1000,arrow.get('2021-01-01T00:00')).format('YYYY-MM-DDTHH:mm') ==arrow.get('2021-01-01T00:00').format('YYYY-MM-DDTHH:mm')
    assert close_time(0,1000,arrow.get('2021-01-01T00:00')).format('YYYY-MM-DDTHH:mm') ==arrow.get('2021-01-01T01:00').format('YYYY-MM-DDTHH:mm')

    assert open_time(1000,1000,arrow.get('2021-01-01T00:00')).format('YYYY-MM-DDTHH:mm') ==arrow.get('2021-01-02T09:05').format('YYYY-MM-DDTHH:mm')
    assert close_time(1000,1000,arrow.get('2021-01-01T00:00')).format('YYYY-MM-DDTHH:mm') ==arrow.get('2021-01-04T03:00').format('YYYY-MM-DDTHH:mm')

    
