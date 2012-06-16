
###############################################################################
#
# CreateNewChargeWithToken
# Charges a credit card by creating a new charge object using a card token that is associated with the credit card details.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class CreateNewChargeWithToken(Choreography):

    """
    Create a new instance of the CreateNewChargeWithToken Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Stripe/CreateNewChargeWithToken')


    def new_input_set(self):
        return CreateNewChargeWithTokenInputSet()

    def _make_result_set(self, result, path):
        return CreateNewChargeWithTokenResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateNewChargeWithTokenChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the CreateNewChargeWithToken
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class CreateNewChargeWithTokenInputSet(InputSet):
        """
        Set the value of the APISecretKey input for this choreography. ((string) The secret API Key providied by Stripe)
        """
        def set_APISecretKey(self, value):
            InputSet._set_input(self, 'APISecretKey', value)

        """
        Set the value of the Amount input for this choreography. ((integer) The amount to charge a customer in cents)
        """
        def set_Amount(self, value):
            InputSet._set_input(self, 'Amount', value)

        """
        Set the value of the Currency input for this choreography. ((optional, string) 3-letter ISO code for currency. Defaults to 'usd' which is currently the only supported currency.)
        """
        def set_Currency(self, value):
            InputSet._set_input(self, 'Currency', value)

        """
        Set the value of the Description input for this choreography. ((optional, string) An arbitrary string of text that will be associated with the charge as a description)
        """
        def set_Description(self, value):
            InputSet._set_input(self, 'Description', value)

        """
        Set the value of the Token input for this choreography. ((string) The token associated with a set of credit card details. This can be generated with the CreateCardToken Choreo.)
        """
        def set_Token(self, value):
            InputSet._set_input(self, 'Token', value)


"""
A ResultSet with methods tailored to the values returned by the CreateNewChargeWithToken choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class CreateNewChargeWithTokenResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((XML) The response from Stripe)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class CreateNewChargeWithTokenChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CreateNewChargeWithTokenResultSet(response, path)
