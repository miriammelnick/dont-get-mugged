
###############################################################################
#
# GetBalance
# Retrieves the available balance for a PayPal account.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetBalance(Choreography):

    """
    Create a new instance of the GetBalance Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/PayPal/GetBalance')


    def new_input_set(self):
        return GetBalanceInputSet()

    def _make_result_set(self, result, path):
        return GetBalanceResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetBalanceChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetBalance
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetBalanceInputSet(InputSet):
        """
        Set the value of the Endpoint input for this choreography. ((optional, string) Set to api-3t.paypal.com when running in production. Defaults to api-3t.sandbox.paypal.com for sandbox testing.)
        """
        def set_Endpoint(self, value):
            InputSet._set_input(self, 'Endpoint', value)

        """
        Set the value of the Password input for this choreography. ((required, string) The API Password provided by PayPal.)
        """
        def set_Password(self, value):
            InputSet._set_input(self, 'Password', value)

        """
        Set the value of the Signature input for this choreography. ((required, string) The API Signature provided by PayPal.)
        """
        def set_Signature(self, value):
            InputSet._set_input(self, 'Signature', value)

        """
        Set the value of the User input for this choreography. ((required, string) The API Username provided by PayPal.)
        """
        def set_User(self, value):
            InputSet._set_input(self, 'User', value)


"""
A ResultSet with methods tailored to the values returned by the GetBalance choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetBalanceResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((string) Response from PayPal formatted in name/value pairs.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetBalanceChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetBalanceResultSet(response, path)
