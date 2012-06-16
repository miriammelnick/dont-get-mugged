
###############################################################################
#
# GetMediaByID
# Retrieves information about a specified media object.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetMediaByID(Choreography):

    """
    Create a new instance of the GetMediaByID Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Instagram/GetMediaByID')


    def new_input_set(self):
        return GetMediaByIDInputSet()

    def _make_result_set(self, result, path):
        return GetMediaByIDResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetMediaByIDChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetMediaByID
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetMediaByIDInputSet(InputSet):
        """
        Set the value of the AccessToken input for this choreography. ((conditional, string) The access token retrieved during the Oauth 2.0 process. Required unless you provide the ClientID.)
        """
        def set_AccessToken(self, value):
            InputSet._set_input(self, 'AccessToken', value)

        """
        Set the value of the ClientID input for this choreography. ((conditional, string) The Client ID provided by Instagram after registering your application. Required unless you provide the AccessToken.)
        """
        def set_ClientID(self, value):
            InputSet._set_input(self, 'ClientID', value)

        """
        Set the value of the MediaID input for this choreography. ((required, integer) The ID of the media object you want to retrieve. For example, a valid MediaID could be 3.)
        """
        def set_MediaID(self, value):
            InputSet._set_input(self, 'MediaID', value)


"""
A ResultSet with methods tailored to the values returned by the GetMediaByID choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetMediaByIDResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((json) The response from Instagram.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetMediaByIDChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetMediaByIDResultSet(response, path)
