
###############################################################################
#
# GetPopularMedia
# Retrieves a list of what media is most popular at the moment.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetPopularMedia(Choreography):

    """
    Create a new instance of the GetPopularMedia Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Instagram/GetPopularMedia')


    def new_input_set(self):
        return GetPopularMediaInputSet()

    def _make_result_set(self, result, path):
        return GetPopularMediaResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetPopularMediaChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetPopularMedia
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetPopularMediaInputSet(InputSet):
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
A ResultSet with methods tailored to the values returned by the GetPopularMedia choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetPopularMediaResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((json) The response from Instagram.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetPopularMediaChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetPopularMediaResultSet(response, path)
