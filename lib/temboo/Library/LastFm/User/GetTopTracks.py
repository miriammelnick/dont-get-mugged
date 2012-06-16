
###############################################################################
#
# GetTopTracks
# Retrieves the top tracks listened to by a user.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetTopTracks(Choreography):

    """
    Create a new instance of the GetTopTracks Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/LastFm/User/GetTopTracks')


    def new_input_set(self):
        return GetTopTracksInputSet()

    def _make_result_set(self, result, path):
        return GetTopTracksResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetTopTracksChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetTopTracks
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetTopTracksInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((string) Your Last.fm API Key.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the Limit input for this choreography. ((optional, integer) The number of results to fetch per page. Defaults to 50.)
        """
        def set_Limit(self, value):
            InputSet._set_input(self, 'Limit', value)

        """
        Set the value of the Page input for this choreography. ((optional, integer) The page number to fetch. Defaults to 1.)
        """
        def set_Page(self, value):
            InputSet._set_input(self, 'Page', value)

        """
        Set the value of the Period input for this choreography. ((optional, string) The time period over which to retrieve top tracks for. Valid values are: overall, 7day, 3month, 6month, 12month. Defaults to 'overall'.)
        """
        def set_Period(self, value):
            InputSet._set_input(self, 'Period', value)

        """
        Set the value of the User input for this choreography. ((string) The Last.fm username to fetch top tracks for.)
        """
        def set_User(self, value):
            InputSet._set_input(self, 'User', value)


"""
A ResultSet with methods tailored to the values returned by the GetTopTracks choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetTopTracksResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((XML) The response from Last.fm.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetTopTracksChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetTopTracksResultSet(response, path)
