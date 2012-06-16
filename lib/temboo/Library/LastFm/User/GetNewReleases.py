
###############################################################################
#
# GetNewReleases
# Retrieves a list of forthcoming releases based on a user's musical taste. 
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetNewReleases(Choreography):

    """
    Create a new instance of the GetNewReleases Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/LastFm/User/GetNewReleases')


    def new_input_set(self):
        return GetNewReleasesInputSet()

    def _make_result_set(self, result, path):
        return GetNewReleasesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetNewReleasesChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetNewReleases
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetNewReleasesInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((string) Your Last.fm API Key.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the UserRecommendations input for this choreography. ((optional, boolean) If 1, the feed contains new releases based on Last.fm's artist recommendations for this user. Otherwise, it is based on their library.)
        """
        def set_UserRecommendations(self, value):
            InputSet._set_input(self, 'UserRecommendations', value)

        """
        Set the value of the User input for this choreography. ((string) The Last.fm username.)
        """
        def set_User(self, value):
            InputSet._set_input(self, 'User', value)


"""
A ResultSet with methods tailored to the values returned by the GetNewReleases choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetNewReleasesResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((XML) The response from Last.fm.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetNewReleasesChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetNewReleasesResultSet(response, path)
