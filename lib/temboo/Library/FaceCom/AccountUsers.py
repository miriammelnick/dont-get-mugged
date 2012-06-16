
###############################################################################
#
# AccountUsers
# Obtain a list of current users registered in the account's private namespaces.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class AccountUsers(Choreography):

    """
    Create a new instance of the AccountUsers Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/FaceCom/AccountUsers')


    def new_input_set(self):
        return AccountUsersInputSet()

    def _make_result_set(self, result, path):
        return AccountUsersResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return AccountUsersChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the AccountUsers
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class AccountUsersInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) Enter your face.com API Key.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the APISecret input for this choreography. ((required, string) Enter your face.com API Secret.)
        """
        def set_APISecret(self, value):
            InputSet._set_input(self, 'APISecret', value)

        """
        Set the value of the Namespaces input for this choreography. ((required, string) Enter a comma-delimited list of one or more private face.com namespaces.)
        """
        def set_Namespaces(self, value):
            InputSet._set_input(self, 'Namespaces', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) You have the option of selecting json or xml. Defaults to 'xml'.)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)


"""
A ResultSet with methods tailored to the values returned by the AccountUsers choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class AccountUsersResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Face.com. Corresponds to the ResponseFormat input. Defaults to XML.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class AccountUsersChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return AccountUsersResultSet(response, path)
