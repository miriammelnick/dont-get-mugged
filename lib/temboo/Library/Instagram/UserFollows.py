
###############################################################################
#
# UserFollows
# Retrieve the list of users that this user is following.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class UserFollows(Choreography):

    """
    Create a new instance of the UserFollows Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Instagram/UserFollows')


    def new_input_set(self):
        return UserFollowsInputSet()

    def _make_result_set(self, result, path):
        return UserFollowsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UserFollowsChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the UserFollows
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class UserFollowsInputSet(InputSet):
        """
        Set the value of the AccessToken input for this choreography. ((required, string) The access token retrieved during the Oauth 2.0 process. )
        """
        def set_AccessToken(self, value):
            InputSet._set_input(self, 'AccessToken', value)

        """
        Set the value of the UserID input for this choreography. ((required, integer) The ID of the user that you want to retrieve. Defaults to 'self' which will return the user associated with the access token.)
        """
        def set_UserID(self, value):
            InputSet._set_input(self, 'UserID', value)


"""
A ResultSet with methods tailored to the values returned by the UserFollows choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class UserFollowsResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((json) The response from Instagram.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class UserFollowsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return UserFollowsResultSet(response, path)
