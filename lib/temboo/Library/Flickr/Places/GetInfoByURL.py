
###############################################################################
#
# GetInfoByURL
# Obtain geo-location information for a place using its flickr.com/places URL.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetInfoByURL(Choreography):

    """
    Create a new instance of the GetInfoByURL Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Flickr/Places/GetInfoByURL')


    def new_input_set(self):
        return GetInfoByURLInputSet()

    def _make_result_set(self, result, path):
        return GetInfoByURLResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetInfoByURLChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetInfoByURL
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetInfoByURLInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) Enter your application API key.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the URL input for this choreography. ((required, string) Enter a flickr.com/places URL in the following form: /country/region/city. For example: /USA/NewYork/Rochester.)
        """
        def set_URL(self, value):
            InputSet._set_input(self, 'URL', value)


"""
A ResultSet with methods tailored to the values returned by the GetInfoByURL choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetInfoByURLResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response in XML from Flickr.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetInfoByURLChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetInfoByURLResultSet(response, path)
