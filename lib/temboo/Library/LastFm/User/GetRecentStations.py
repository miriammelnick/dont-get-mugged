
###############################################################################
#
# GetRecentStations
# Retrieves a list of the recent Stations listened to by this user.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetRecentStations(Choreography):

    """
    Create a new instance of the GetRecentStations Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/LastFm/User/GetRecentStations')


    def new_input_set(self):
        return GetRecentStationsInputSet()

    def _make_result_set(self, result, path):
        return GetRecentStationsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetRecentStationsChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetRecentStations
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetRecentStationsInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) Your Last.fm API Key.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the APISecret input for this choreography. ((required, string) Your Last.fm API Secret.)
        """
        def set_APISecret(self, value):
            InputSet._set_input(self, 'APISecret', value)

        """
        Set the value of the Limit input for this choreography. ((optional, integer) The number of results to fetch per page. Defaults to 10. Maximum is 25.)
        """
        def set_Limit(self, value):
            InputSet._set_input(self, 'Limit', value)

        """
        Set the value of the Page input for this choreography. ((optional, integer) The page number to fetch. Defaults to first page.)
        """
        def set_Page(self, value):
            InputSet._set_input(self, 'Page', value)

        """
        Set the value of the SessionKey input for this choreography. ((required, string) The session key retrieved in the last step of the authorization process.)
        """
        def set_SessionKey(self, value):
            InputSet._set_input(self, 'SessionKey', value)

        """
        Set the value of the User input for this choreography. ((required, string) The last.fm username to fetch the recent Stations of.)
        """
        def set_User(self, value):
            InputSet._set_input(self, 'User', value)


"""
A ResultSet with methods tailored to the values returned by the GetRecentStations choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetRecentStationsResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Last.fm.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetRecentStationsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetRecentStationsResultSet(response, path)
