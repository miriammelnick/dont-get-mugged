
###############################################################################
#
# DenyFriendRequest
# Denies a pending friend request from another user.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class DenyFriendRequest(Choreography):

    """
    Create a new instance of the DenyFriendRequest Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Foursquare/Users/DenyFriendRequest')


    def new_input_set(self):
        return DenyFriendRequestInputSet()

    def _make_result_set(self, result, path):
        return DenyFriendRequestResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DenyFriendRequestChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the DenyFriendRequest
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class DenyFriendRequestInputSet(InputSet):
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
        Set the value of the UserID input for this choreography. ((required, string) The user ID of a pending friend.)
        """
        def set_UserID(self, value):
            InputSet._set_input(self, 'UserID', value)


"""
A ResultSet with methods tailored to the values returned by the DenyFriendRequest choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class DenyFriendRequestResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Foursquare. Corresponds to the ResponseFormat input. Defaults to JSON.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class DenyFriendRequestChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return DenyFriendRequestResultSet(response, path)
