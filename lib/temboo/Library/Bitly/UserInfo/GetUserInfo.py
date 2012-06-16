
###############################################################################
#
# GetUserInfo
# Returns information about a specified user.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetUserInfo(Choreography):

    """
    Create a new instance of the GetUserInfo Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Bitly/UserInfo/GetUserInfo')


    def new_input_set(self):
        return GetUserInfoInputSet()

    def _make_result_set(self, result, path):
        return GetUserInfoResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetUserInfoChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetUserInfo
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetUserInfoInputSet(InputSet):
        """
        Set the value of the AccessToken input for this choreography. ((required, string) The oAuth access token provided by Bitly.)
        """
        def set_AccessToken(self, value):
            InputSet._set_input(self, 'AccessToken', value)

        """
        Set the value of the FullName input for this choreography. ((optional, string) The users full name value (only available for the authenticated user).)
        """
        def set_FullName(self, value):
            InputSet._set_input(self, 'FullName', value)

        """
        Set the value of the Login input for this choreography. ((optional, string) The bitly login of the user whose info to look up. If not given, the authenticated user will be used.)
        """
        def set_Login(self, value):
            InputSet._set_input(self, 'Login', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) The format that you want the response to be in. Accepted values are "json" or "xml". Defaults to "json".)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)


"""
A ResultSet with methods tailored to the values returned by the GetUserInfo choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetUserInfoResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Bitly.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetUserInfoChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetUserInfoResultSet(response, path)
