# cityloc

### Look up world city coordinates and country codes

Python (2 and 3) module to look up world city locations and country codes.
Uses data from the Basic World Cities Database provided by Simplemaps.com. The data is licensed under the [Creative Commons Attribution 4.0 license](https://creativecommons.org/licenses/by/4.0/).



## Installation

```
$ pip install cityloc
```

## Examples

### Look up city

```python
>>> from cityloc import city_lookup
>>> r = city_lookup('London', country='GB')
>>> pprint.pprint(r)
[{'capital': 1,
  'country': 'GB',
  'id': 6911,
  'lat_wgs84': 51.5,
  'long_wgs84': -0.1167,
  'name': 'London',
  'name_ascii': 'London',
  'population': 8567000,
  'region': ''}]
```

### Look up capital city for country

```python
>>> from cityloc import capital_for_cc
>>> r = capital_for_cc("FR")
>>> pprint.pprint(r)
{'capital': 1,
 'country': 'FR',
 'id': 6687,
 'lat_wgs84': 48.8667,
 'long_wgs84': 2.3333,
 'name': 'Paris',
 'name_ascii': 'Paris',
 'population': 9904000,
 'region': 'Île-de-France'}
```

## Version History

* 0.1.1: Added capital_for_cc (17/09/2019)
* 0.1.0: Initial release (03/01/2019)

## BSD License 

Copyright (C) 2019 Sveinbjorn Thordarson

Redistribution and use in source and binary forms, with or without modification,
are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this
list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, this
list of conditions and the following disclaimer in the documentation and/or other
materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors may
be used to endorse or promote products derived from this software without specific
prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT,
INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT
NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
POSSIBILITY OF SUCH DAMAGE.

