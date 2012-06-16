
###############################################################################
#
# UpdateAccountObject
# Updates an Account Object name.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class UpdateAccountObject(Choreography):

    """
    Create a new instance of the UpdateAccountObject Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Salesforce/UpdateAccountObject')


    def new_input_set(self):
        return UpdateAccountObjectInputSet()

    def _make_result_set(self, result, path):
        return UpdateAccountObjectResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UpdateAccountObjectChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the UpdateAccountObject
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class UpdateAccountObjectInputSet(InputSet):
        """
        Set the value of the AccountId input for this choreography. ((required, string) The ID for the account you want to update)
        """
        def set_AccountId(self, value):
            InputSet._set_input(self, 'AccountId', value)

        """
        Set the value of the AccountName input for this choreography. ((required, string) A new name to update the Account with)
        """
        def set_AccountName(self, value):
            InputSet._set_input(self, 'AccountName', value)

        """
        Set the value of the Password input for this choreography. ((required, string) Your Salesforce password.)
        """
        def set_Password(self, value):
            InputSet._set_input(self, 'Password', value)

        """
        Set the value of the SecurityToken input for this choreography. ((required, string) Your Salesforce security token used for making API calls.)
        """
        def set_SecurityToken(self, value):
            InputSet._set_input(self, 'SecurityToken', value)

        """
        Set the value of the Username input for this choreography. ((required, string) Your Salesforce username.)
        """
        def set_Username(self, value):
            InputSet._set_input(self, 'Username', value)


"""
A ResultSet with methods tailored to the values returned by the UpdateAccountObject choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class UpdateAccountObjectResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Salesforce)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class UpdateAccountObjectChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return UpdateAccountObjectResultSet(response, path)
