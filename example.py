#!/usr/bin/env python
# The MIT License (MIT)
#
# Copyright (c) 2015 Matthew Taylor
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import automatatron
import time

print "EXAMPLE 1:"
print "Print the first 10 rows of all possible automaton:"
for rule in range(1,257):
  automaton = automatatron.Engine(rule)
  automaton.run(iterations=10)
  print automaton

print "EXAMPLE 2:"
print "Print the first 50 rows of Rule 30"
automaton = automatatron.Engine(30)
automaton.run(iterations=50)
print automaton

print "EXAMPLE 3:"
print "Run the next 10 iterations, and pass results into specified handler."
def row_handler(row, _):
  print row
automaton.run(handler=row_handler, iterations=10)

print "EXAMPLE 4:"
print "Stream the middle 101 columns to stdout"
automaton = automatatron.Engine(30)
def stream_handler(row, _):
  print automatatron.default_string_formatter(row)
  time.sleep(0.05)
automaton.run(handler=stream_handler, width=101)
