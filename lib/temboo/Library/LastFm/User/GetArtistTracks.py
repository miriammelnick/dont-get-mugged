
###############################################################################
#
# GetArtistTracks
# Retrieves a list of tracks by a given artist scrobbled by this user, including scrobble time.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetArtistTracks(Choreography):

    """
    Create a new instance of the GetArtistTracks Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/LastFm/User/GetArtistTracks')


    def new_input_set(self):
        return GetArtistTracksInputSet()

    def _make_result_set(self, result, path):
        return GetArtistTracksResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetArtistTracksChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetArtistTracks
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetArtistTracksInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) Your Last.fm API Key.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the Artist input for this choreography. ((required, string) The artist name you are interested in.)
        """
        def set_Artist(self, value):
            InputSet._set_input(self, 'Artist', value)

        """
        Set the value of the EndTimestamp input for this choreography. ((optional, date) A unix timestamp to end at.)
        """
        def set_EndTimestamp(self, value):
            InputSet._set_input(self, 'EndTimestamp', value)

        """
        Set the value of the Page input for this choreography. ((optional, integer) The page number to fetch. Defaults to 1.)
        """
        def set_Page(self, value):
            InputSet._set_input(self, 'Page', value)

        """
        Set the value of the StartTimestamp input for this choreography. ((optional, date) A unix timestamp to start at.)
        """
        def set_StartTimestamp(self, value):
            InputSet._set_input(self, 'StartTimestamp', value)

        """
        Set the value of the User input for this choreography. ((required, string) The last.fm username to fetch the recent tracks of.)
        """
        def set_User(self, value):
            InputSet._set_input(self, 'User', value)


"""
A ResultSet with methods tailored to the values returned by the GetArtistTracks choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetArtistTracksResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Last.fm.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetArtistTracksChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetArtistTracksResultSet(response, path)
