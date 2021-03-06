
###############################################################################
#
# GetInfo
# Get information about a user profile.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetInfo(Choreography):

    """
    Create a new instance of the GetInfo Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/LastFm/User/GetInfo')


    def new_input_set(self):
        return GetInfoInputSet()

    def _make_result_set(self, result, path):
        return GetInfoResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetInfoChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetInfo
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetInfoInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) Your Last.fm API Key.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the User input for this choreography. ((required, string) The user to fetch info for.)
        """
        def set_User(self, value):
            InputSet._set_input(self, 'User', value)


"""
A ResultSet with methods tailored to the values returned by the GetInfo choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetInfoResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Last.fm.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetInfoChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetInfoResultSet(response, path)
