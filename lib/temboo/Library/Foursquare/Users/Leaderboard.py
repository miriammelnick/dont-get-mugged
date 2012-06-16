
###############################################################################
#
# Leaderboard
# Return the user's Leaderboard
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class Leaderboard(Choreography):

    """
    Create a new instance of the Leaderboard Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Foursquare/Users/Leaderboard')


    def new_input_set(self):
        return LeaderboardInputSet()

    def _make_result_set(self, result, path):
        return LeaderboardResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return LeaderboardChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the Leaderboard
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class LeaderboardInputSet(InputSet):
        """
        Set the value of the Neighbors input for this choreography. ((optional, integer) The number of friends' scores to return that are adjacent to your score, in ranked order.)
        """
        def set_Neighbors(self, value):
            InputSet._set_input(self, 'Neighbors', value)

        """
        Set the value of the OauthToken input for this choreography. ((required, string) The FourSquare API Oauth token string.)
        """
        def set_OauthToken(self, value):
            InputSet._set_input(self, 'OauthToken', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) The format that response should be in. Can be set to xml or json. Defaults to json.)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)


"""
A ResultSet with methods tailored to the values returned by the Leaderboard choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class LeaderboardResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Foursquare. Corresponds to the ResponseFormat input. Defaults to JSON.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class LeaderboardChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return LeaderboardResultSet(response, path)
