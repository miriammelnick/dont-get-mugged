
###############################################################################
#
# GetRecentPhotos
# Retrieve public photos that have been recently uploaded to Flickr.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetRecentPhotos(Choreography):

    """
    Create a new instance of the GetRecentPhotos Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Flickr/Photos/GetRecentPhotos')


    def new_input_set(self):
        return GetRecentPhotosInputSet()

    def _make_result_set(self, result, path):
        return GetRecentPhotosResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetRecentPhotosChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetRecentPhotos
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetRecentPhotosInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) Enter your application API key.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the Extras input for this choreography. ((optional, string) A comma-separated list returning additional photo information such as: license, description, date_upload, date_taken.  Additional options are listed on this method's API doc page.)
        """
        def set_Extras(self, value):
            InputSet._set_input(self, 'Extras', value)

        """
        Set the value of the Page input for this choreography. ((optional, integer) Specify the page of photos that is to be returned.  If unspecified, the first page is returned.)
        """
        def set_Page(self, value):
            InputSet._set_input(self, 'Page', value)

        """
        Set the value of the PerPage input for this choreography. ((optional, integer) Specify how many photos to display per page. Default is set to: 100. The mamimum allowed value is: 500.)
        """
        def set_PerPage(self, value):
            InputSet._set_input(self, 'PerPage', value)


"""
A ResultSet with methods tailored to the values returned by the GetRecentPhotos choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetRecentPhotosResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response in XML from Flickr.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetRecentPhotosChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetRecentPhotosResultSet(response, path)
