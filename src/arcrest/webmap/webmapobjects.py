import json
from geometry import Envelope

########################################################################
class Bookmark(object):
    """ A bookmark is a saved geographic extent that allows end users to
        quickly navigate to a particular area of interest.
    """
    _extents = None
    #----------------------------------------------------------------------
    @property
    def bookmarks(self):
        """ returns the bookmarks """
        if self._extents is None:
            self._extents = []
        return self._extents
    #----------------------------------------------------------------------
    def add(self, extent, name):
        """ adds an extent to the bookmarks object """
        bm = {}
        if isinstance(extent, Envelope):
            bm['extent'] = extent.asDictionary
            bm['name'] = name
            self._extents.append(
                bm
            )
            return True
        else:
            return False
    #----------------------------------------------------------------------
    def remove(self, index):
        """ removes a bookmark via index location """
        if index <= len(self._extents) - 1:
            self._extents.remove(self._extents[index])
            return True
        else:
            return False
    #----------------------------------------------------------------------
    def __str__(self):
        """ returns string representation of the object """
        return json.dumps(self.__dict__())
    #----------------------------------------------------------------------
    @property
    def asDictionary(self):
        """ returns a dictionary representation of the object """
        return {"bookmarks" : self._extents}











