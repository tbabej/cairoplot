#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# series.py
#
# The MIT License (MIT)
#
# Copyright (c) 2013 Cairoplot team
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the "Software"), to deal in
# the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
# the Software, and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
# FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
# COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
# IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

NUM_TYPES = (int, float, long)
DATA_TYPES = (int, float, long, tuple)
STR_TYPES = (str, unicode)
FILLING_TYPES = ['solid', 'radial', 'horizontal', 'vertical']
DEFAULT_COLOR_FILLING = 'solid'
#TODO: Define default color list
DEFAULT_COLOR_LIST = None


class Data(object):
    '''
        Model the smallest data structure.
        Will always contain a tuple representing a tridimensional point.

        Common usage:
            >>> d = Data(name='simple value', 1); print d
            empty: (1, 0, 0)
            >>> d = Data('point a', (1,1)); print d
            point a: (1, 1, 0)
            >>> d = Data('point b', (1,2,3)); print d
            point b: (1, 2, 3)
    '''
    def __init__(self, name=None, content=None):
        '''Initiate the objects variables.'''
        self.content = content
        self.name = name

    @property
    def content(self):
        '''
        Property to validate the object's content.

            >>> d = Data(content = 13); print d
            (13, 0, 0)
            >>> d = Data(content = (1,2)); print d
            (1, 2, 0)
            >>> d = Data(content = (1,2,3)); print d
            (1, 2, 3)

        :raises TypeError: If the input's type is not in :const:`DATA_TYPES`. Also, if the input's type is a tuple but its values' types are not in :const:`NUM_TYPES` or its length is not two or three.
        '''
        return self._content

    @content.setter
    def content(self, content):
        '''Ensure that content is a valid tuple or a number (int, float or long).'''
        # Type: None
        if content is None:
            self._content = None

        # Type: Int or Float
        elif type(content) in NUM_TYPES:
            self._content = (content, 0, 0)

        # Type: Tuple
        elif type(content) is tuple:
            # Ensures the correct size
            if len(content) not in (2, 3):
                raise TypeError("Content representing points must have two or three items.")

            # Ensures that all items in tuple are numbers
            is_num = lambda x: type(x) not in NUM_TYPES

            if max(map(is_num, content)):
                # An item's type isn't int, float or long
                raise TypeError("All content must be a number (int, float or long)")
            # Create 3D point from 2D value
            if len(content) == 2:
                self._content = (content[0], content[1], 0)
            # Create 3D point from 3D value
            elif len(content) == 3:
                self._content = content[:]

        # Unknown type!
        else:
            self._content = 0
            raise TypeError("Content must be int, float, long or a tuple with two or three items")

    # Name property
    @property
    def name(self):
        '''
        Property to validate the object's name.

            >>> d = Data('data_name', 13); print d
            data_name: 13

        :raises TypeError: If the input's type is not in :const:`STR_TYPES`
        '''
        return self._name

    @name.setter
    def name(self, name):
        '''Sets the name of the Data'''
        if type(name) in STR_TYPES and len(name) > 0:
            self._name = name
        elif name is None:
            self._name = None
        else:
            self._name = None
            raise TypeError("Data name must be string or unicode.")

    def clear(self):
        '''Sets name to None and content to 0.'''
        self.name = None
        self.content = None

    def copy(self):
        '''Return a copy of the object'''
        new_data = Data()
        # If it has a name
        if self.name is not None:
            new_data.name = self.name

        new_data.content = self.content[:]

        return new_data

    def __eq__(self, other_data):
        '''Compare Data variables'''
        return self.name == other_data.name and \
               self.content == other_data.content

    def __len__(self):
        '''
            Return the length of the content.

            :return: **1**, if content is a number or **length** if a tuple.
        '''
        return len(self.content)

    def __str__(self):
        '''Return a string representation of the Data object'''
        if self.name is None:
            return str(self.content)
        else:
            return self.name + ": " + str(self.content)


class Series(object):
    '''
        Model a list of values that must be either:

        - Numbers (int, float or long);
        - Tuples representing points with 2 or 3 items (x,y,z).

        Common usage:
            >>> s = Series("number_series", [1,2,3]); print s
            number_series ['(1, 0, 0)', '(2, 0, 0)', '(3, 0, 0)']
            >>> s = Series("point_series", [(1,1,1), (2,2,2), (3,3,3)]); print s
            point_series ['(1, 1, 1)', '(2, 2, 2)', '(3, 3, 3)']
    '''

    def __init__(self, name=None, content=None):
        '''Initiate the objects variables.'''
        self.name = name
        self.content = content

    @property
    def content(self):
        '''
        Property to validate the series.

            >>> s = Series(content=[1,2,3]); print s
            ['(1, 0, 0)', '(2, 0, 0)', '(3, 0, 0)']
            >>> s = Series(content=[(1,1,1), (2,2,2), (3,3,3)]); print s
            ['(1, 1, 1)', '(2, 2, 2)', '(3, 3, 3)']

        :raises TypeError: If the input's is not a list or if the list contains tuples and numbers (int, float or long) mixed.
        '''
        return self._content

    @content.setter
    def content(self, content):
        '''Ensure that content is a list of numbers (int, float or long) or tuples. Lists containing Data objects along the primitive types are also accepted if they have the same length.'''
        is_num = lambda x: type(x) in NUM_TYPES
        is_tuple = lambda x: type(x) is tuple

        # If content is None
        if content is None:
            self._content = []
        # If content is not a List
        elif type(content) is not list:
            self._content = []
            raise TypeError("Series must be a list containing numbers (int, float or long) or 2 or 3 dimensions tuples.")
        # If content is an empty list
        elif len(content) == 0:
            self._content = []
        # If content contains numbers and tuples
        elif max(map(is_num, content)) and max(map(is_tuple, content)):
            # Content contains numbers and tuples
            raise TypeError("Series must contain either a list of numbers (int, float or long) or 2 or 3 dimensions tuples. Not both types.")
        #Content is either a list of points or a list of numbers
        else:
            self._content = []
            for item in content:
                if type(item) is Data:
                    self._content.append(item.copy())
                else:
                    self._content.append(Data(content=item))

    # Name property
    @property
    def name(self):
        '''
        Property to validate the object's name.
            >>> s = Series("number_series", [1,2,3]); print s
            number_series ['(1, 0, 0)', '(2, 0, 0)', '(3, 0, 0)']

        :raises TypeError: If the input's type is not in :const:`STR_TYPES`
        '''
        return self._name

    @name.setter
    def name(self, name):
        '''Sets the name of the Data'''
        if type(name) in STR_TYPES and len(name) > 0:
            self._name = name
        elif name is None:
            self._name = None
        else:
            self._name = None
            raise TypeError("Data name must be string or unicode.")

    def clear(self):
        '''Set name to None and content to [].'''
        self.name = None
        self.content = []

    def __eq__(self, other_series):
        '''Compare Series objects'''
        return self.name == other_series.name and \
               self.content == other_series.content

    def __len__(self):
        '''Return the length of the content.'''
        return len(self.content)

    def __str__(self):
        '''Return a string that represents the object'''
        ret = ""
        if self.name is not None:
            ret += self.name + " "
        if len(self.content) > 0:
            list_str = [str(item) for item in self.content]
            ret += str(list_str)
        else:
            ret += "[]"
        return ret
