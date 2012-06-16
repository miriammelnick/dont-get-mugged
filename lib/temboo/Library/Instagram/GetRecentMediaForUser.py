
###############################################################################
#
# GetRecentMediaForUser
# Retrieves the most recent media published by a user.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetRecentMediaForUser(Choreography):

    """
    Create a new instance of the GetRecentMediaForUser Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Instagram/GetRecentMediaForUser')


    def new_input_set(self):
        return GetRecentMediaForUserInputSet()

    def _make_result_set(self, result, path):
        return GetRecentMediaForUserResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetRecentMediaForUserChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetRecentMediaForUser
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetRecentMediaForUserInputSet(InputSet):
        """
        Set the value of the AccessToken input for this choreography. ((required, string) The access token retrieved during the Oauth 2.0 process.)
        """
        def set_AccessToken(self, value):
            InputSet._set_input(self, 'AccessToken', value)

        """
        Set the value of the Count input for this choreography. ((optional, integer) Count of media to return.)
        """
        def set_Count(self, value):
            InputSet._set_input(self, 'Count', value)

        """
        Set the value of the MaxID input for this choreography. ((optional, integer) Return media liked before this id.)
        """
        def set_MaxID(self, value):
            InputSet._set_input(self, 'MaxID', value)

        """
        Set the value of the MinID input for this choreography. ((optional, integer) Returns media later than this min_id.)
        """
        def set_MinID(self, value):
            InputSet._set_input(self, 'MinID', value)

        """
        Set the value of the MinTimestamp input for this choreography. ((optional, date) Returns media after this UNIX timestamp.)
        """
        def set_MinTimestamp(self, value):
            InputSet._set_input(self, 'MinTimestamp', value)

        """
        Set the value of the UserID input for this choreography. ((optional, integer) The ID of the user that you want to retrieve. Defaults to 'self' which will return the user associated with the access token.)
        """
        def set_UserID(self, value):
            InputSet._set_input(self, 'UserID', value)


"""
A ResultSet with methods tailored to the values returned by the GetRecentMediaForUser choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetRecentMediaForUserResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((json) The response from Instagram.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetRecentMediaForUserChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetRecentMediaForUserResultSet(response, path)
