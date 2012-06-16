
###############################################################################
#
# CreateNewChargeForExistingCustomer
# Creates a new charge object in order to charge a credit card for an existing customer.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class CreateNewChargeForExistingCustomer(Choreography):

    """
    Create a new instance of the CreateNewChargeForExistingCustomer Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Stripe/CreateNewChargeForExistingCustomer')


    def new_input_set(self):
        return CreateNewChargeForExistingCustomerInputSet()

    def _make_result_set(self, result, path):
        return CreateNewChargeForExistingCustomerResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateNewChargeForExistingCustomerChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the CreateNewChargeForExistingCustomer
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class CreateNewChargeForExistingCustomerInputSet(InputSet):
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
        Set the value of the CustomerId input for this choreography. ((string) The id for the customer to charge)
        """
        def set_CustomerId(self, value):
            InputSet._set_input(self, 'CustomerId', value)

        """
        Set the value of the Description input for this choreography. ((optional, string) An arbitrary string of text that will be associated with the charge as a description)
        """
        def set_Description(self, value):
            InputSet._set_input(self, 'Description', value)


"""
A ResultSet with methods tailored to the values returned by the CreateNewChargeForExistingCustomer choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class CreateNewChargeForExistingCustomerResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((XML) The response from Stripe)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class CreateNewChargeForExistingCustomerChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CreateNewChargeForExistingCustomerResultSet(response, path)
