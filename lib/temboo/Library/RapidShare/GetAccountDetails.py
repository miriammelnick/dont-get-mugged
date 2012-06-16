
###############################################################################
#
# GetAccountDetails
# Returns details about a RapidShare account in key-value pairs.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetAccountDetails(Choreography):

    """
    Create a new instance of the GetAccountDetails Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/RapidShare/GetAccountDetails')


    def new_input_set(self):
        return GetAccountDetailsInputSet()

    def _make_result_set(self, result, path):
        return GetAccountDetailsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetAccountDetailsChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetAccountDetails
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetAccountDetailsInputSet(InputSet):
        """
        Set the value of the Login input for this choreography. ((string) Your RapidShare username)
        """
        def set_Login(self, value):
            InputSet._set_input(self, 'Login', value)

        """
        Set the value of the Password input for this choreography. ((string) Your RapidShare password)
        """
        def set_Password(self, value):
            InputSet._set_input(self, 'Password', value)

        """
        Set the value of the WithCookie input for this choreography. ((optional, boolean) If value "1" is specified, a cookie is returned in the response)
        """
        def set_WithCookie(self, value):
            InputSet._set_input(self, 'WithCookie', value)

        """
        Set the value of the WithPublicId input for this choreography. ((optional, boolean) If value "1" is specified, the public id is returned in the response)
        """
        def set_WithPublicId(self, value):
            InputSet._set_input(self, 'WithPublicId', value)


"""
A ResultSet with methods tailored to the values returned by the GetAccountDetails choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetAccountDetailsResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((string) The response from RapidShare formatted in key / value pairs.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetAccountDetailsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetAccountDetailsResultSet(response, path)
