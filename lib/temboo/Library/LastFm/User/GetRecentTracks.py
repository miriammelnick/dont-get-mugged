
###############################################################################
#
# GetRecentTracks
# Get a list of the recent tracks listened to by this user.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetRecentTracks(Choreography):

    """
    Create a new instance of the GetRecentTracks Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/LastFm/User/GetRecentTracks')


    def new_input_set(self):
        return GetRecentTracksInputSet()

    def _make_result_set(self, result, path):
        return GetRecentTracksResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetRecentTracksChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetRecentTracks
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetRecentTracksInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((string) Your Last.fm API Key.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the EndTimestamp input for this choreography. ((optional, date) End timestamp of a range - only display scrobbles before this time, in UNIX timestamp format. This must be in the UTC time zone.)
        """
        def set_EndTimestamp(self, value):
            InputSet._set_input(self, 'EndTimestamp', value)

        """
        Set the value of the Limit input for this choreography. ((optional, integer) The number of results to fetch per page. Defaults to 50. Maximum is 200.)
        """
        def set_Limit(self, value):
            InputSet._set_input(self, 'Limit', value)

        """
        Set the value of the Page input for this choreography. ((optional, integer) The page number to fetch. Defaults to 1.)
        """
        def set_Page(self, value):
            InputSet._set_input(self, 'Page', value)

        """
        Set the value of the StartTimestamp input for this choreography. ((optional, date) Beginning timestamp of a range - only display scrobbles after this time, in UNIX timestamp format. This must be in the UTC time zone.)
        """
        def set_StartTimestamp(self, value):
            InputSet._set_input(self, 'StartTimestamp', value)

        """
        Set the value of the User input for this choreography. ((string) The last.fm username to fetch the recent tracks of.)
        """
        def set_User(self, value):
            InputSet._set_input(self, 'User', value)


"""
A ResultSet with methods tailored to the values returned by the GetRecentTracks choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetRecentTracksResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((XML) The response from Last.fm.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetRecentTracksChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetRecentTracksResultSet(response, path)
