
###############################################################################
#
# GetGalleryList
# Get a gallery list for a specfied user.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetGalleryList(Choreography):

    """
    Create a new instance of the GetGalleryList Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Flickr/Galleries/GetGalleryList')


    def new_input_set(self):
        return GetGalleryListInputSet()

    def _make_result_set(self, result, path):
        return GetGalleryListResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetGalleryListChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetGalleryList
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetGalleryListInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) Enter your application API key.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the GalleriesPerPage input for this choreography. ((optional, any) Specify the number of galleries that are to be returned per page.  If null, defaults to 100 galleries returned.  Maximum is 500.)
        """
        def set_GalleriesPerPage(self, value):
            InputSet._set_input(self, 'GalleriesPerPage', value)

        """
        Set the value of the Page input for this choreography. ((optional, integer) Enter the number of results pages to be returned.  Default is: 1.)
        """
        def set_Page(self, value):
            InputSet._set_input(self, 'Page', value)

        """
        Set the value of the UserID input for this choreography. ((required, any) Provide the NSID for the user whose gallery list(s) are to be retreived.)
        """
        def set_UserID(self, value):
            InputSet._set_input(self, 'UserID', value)


"""
A ResultSet with methods tailored to the values returned by the GetGalleryList choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetGalleryListResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response in XML from Flickr.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetGalleryListChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetGalleryListResultSet(response, path)
