"""
zip(*iterables) --> A zip object yielding tuples until an input is exhausted
 - the N iterables passed to the function are zipped, as the name suggests
 - the zip object have N-length tuples, for N the numbers of iterables
 - It will return M tuples, where M is the size of the smaller iterable
 - only ordered iterables will work properly as arguments to zip()
"""
