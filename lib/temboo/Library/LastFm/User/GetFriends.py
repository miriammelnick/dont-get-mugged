
###############################################################################
#
# GetFriends
# Retrieves a list of the user's friends on Last.fm.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetFriends(Choreography):

    """
    Create a new instance of the GetFriends Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/LastFm/User/GetFriends')


    def new_input_set(self):
        return GetFriendsInputSet()

    def _make_result_set(self, result, path):
        return GetFriendsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetFriendsChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetFriends
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetFriendsInputSet(InputSet):
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
        Set the value of the RecentTracks input for this choreography. ((optional, boolean) Whether or not to include information about friends' recent listening in the response. Defaults to 0 for false.)
        """
        def set_RecentTracks(self, value):
            InputSet._set_input(self, 'RecentTracks', value)

        """
        Set the value of the User input for this choreography. ((string) The last.fm username to fetch the friends of.)
        """
        def set_User(self, value):
            InputSet._set_input(self, 'User', value)


"""
A ResultSet with methods tailored to the values returned by the GetFriends choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetFriendsResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((XML) The response from Last.fm.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetFriendsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetFriendsResultSet(response, path)
