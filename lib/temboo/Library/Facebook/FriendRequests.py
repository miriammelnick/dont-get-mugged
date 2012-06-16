
###############################################################################
#
# FriendRequests
# Retrieves a list of friend requests for a specified user.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class FriendRequests(Choreography):

    """
    Create a new instance of the FriendRequests Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Facebook/FriendRequests')


    def new_input_set(self):
        return FriendRequestsInputSet()

    def _make_result_set(self, result, path):
        return FriendRequestsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return FriendRequestsChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the FriendRequests
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class FriendRequestsInputSet(InputSet):
        """
        Set the value of the AccessToken input for this choreography. ((required, string) The access token retrieved from the final step of the OAuth process.)
        """
        def set_AccessToken(self, value):
            InputSet._set_input(self, 'AccessToken', value)

        """
        Set the value of the ProfileId input for this choreography. ((optional, integer) The profile id associated with the Graph API object you want to access. Defaults to "me" indicating that you want to access an object associated with the authenticated user.)
        """
        def set_ProfileId(self, value):
            InputSet._set_input(self, 'ProfileId', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) The format that the response should be in. Can be set to xml or json. Defaults to json.)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)


"""
A ResultSet with methods tailored to the values returned by the FriendRequests choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class FriendRequestsResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Facebook. Corresponds to the ResponseFormat input. Defaults to JSON.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class FriendRequestsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return FriendRequestsResultSet(response, path)
