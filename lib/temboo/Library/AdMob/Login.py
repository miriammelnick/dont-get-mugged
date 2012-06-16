
###############################################################################
#
# Login
# Log into AdMob service  and obtain an authorization token.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class Login(Choreography):

    """
    Create a new instance of the Login Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/AdMob/Login')


    def new_input_set(self):
        return LoginInputSet()

    def _make_result_set(self, result, path):
        return LoginResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return LoginChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the Login
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class LoginInputSet(InputSet):
        """
        Set the value of the ClientKey input for this choreography. ((required, string) Enter user AdMob client key.)
        """
        def set_ClientKey(self, value):
            InputSet._set_input(self, 'ClientKey', value)

        """
        Set the value of the Email input for this choreography. ((required, string) The email address registered to your AdMob account.)
        """
        def set_Email(self, value):
            InputSet._set_input(self, 'Email', value)

        """
        Set the value of the Password input for this choreography. ((required, string) Your Admob password.)
        """
        def set_Password(self, value):
            InputSet._set_input(self, 'Password', value)


"""
A ResultSet with methods tailored to the values returned by the Login choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class LoginResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from AdMob in XML format)
        """
        def get_Response(self):
            return self._output.get('Response', None)
        """
        Retrieve the value for the "Token" output from this choreography execution. ((string) The token obtained by running this choreo.)
        """
        def get_Token(self):
            return self._output.get('Token', None)

class LoginChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return LoginResultSet(response, path)
