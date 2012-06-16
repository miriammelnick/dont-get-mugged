
###############################################################################
#
# GetCurrentLocationInfo
# Returns the authenticated user's current location.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetCurrentLocationInfo(Choreography):

    """
    Create a new instance of the GetCurrentLocationInfo Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Google/Latitude/GetCurrentLocationInfo')


    def new_input_set(self):
        return GetCurrentLocationInfoInputSet()

    def _make_result_set(self, result, path):
        return GetCurrentLocationInfoResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetCurrentLocationInfoChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetCurrentLocationInfo
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetCurrentLocationInfoInputSet(InputSet):
        """
        Set the value of the AccessToken input for this choreography. ((string) The access token retrieved in the last step of the OAuth process. Access tokens that are expired will be refreshed and returned in the Choreo output.)
        """
        def set_AccessToken(self, value):
            InputSet._set_input(self, 'AccessToken', value)

        """
        Set the value of the ClientID input for this choreography. ((string) The client ID provided by Google when you register your application.)
        """
        def set_ClientID(self, value):
            InputSet._set_input(self, 'ClientID', value)

        """
        Set the value of the ClientSecret input for this choreography. ((string) The client secret provided by Google when you registered your application.)
        """
        def set_ClientSecret(self, value):
            InputSet._set_input(self, 'ClientSecret', value)

        """
        Set the value of the Granularity input for this choreography. ((optional, string) Specify the level of detailed returned.  Enter: best, or city.  Default is city.)
        """
        def set_Granularity(self, value):
            InputSet._set_input(self, 'Granularity', value)

        """
        Set the value of the RefreshToken input for this choreography. ((string) The refresh token retrieved in the last step of the OAuth process. This is used whenever your access token expires.)
        """
        def set_RefreshToken(self, value):
            InputSet._set_input(self, 'RefreshToken', value)


"""
A ResultSet with methods tailored to the values returned by the GetCurrentLocationInfo choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetCurrentLocationInfoResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((XML) The response from Google.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetCurrentLocationInfoChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetCurrentLocationInfoResultSet(response, path)
