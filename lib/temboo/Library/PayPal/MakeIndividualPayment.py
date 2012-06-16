
###############################################################################
#
# MakeIndividualPayment
# Retrieves the available balance for a PayPal account.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class MakeIndividualPayment(Choreography):

    """
    Create a new instance of the MakeIndividualPayment Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/PayPal/MakeIndividualPayment')


    def new_input_set(self):
        return MakeIndividualPaymentInputSet()

    def _make_result_set(self, result, path):
        return MakeIndividualPaymentResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return MakeIndividualPaymentChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the MakeIndividualPayment
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class MakeIndividualPaymentInputSet(InputSet):
        """
        Set the value of the CurrencyCode input for this choreography. ((optional, string) The currency code associated with the PaymentAmount. Defaults to "USD".)
        """
        def set_CurrencyCode(self, value):
            InputSet._set_input(self, 'CurrencyCode', value)

        """
        Set the value of the EmailAddress input for this choreography. ((required, string) The email address used to identify the recipient of the payment.)
        """
        def set_EmailAddress(self, value):
            InputSet._set_input(self, 'EmailAddress', value)

        """
        Set the value of the EmailSubject input for this choreography. ((optional, string) The subject line of the email that PayPal sends when the transaction is completed. Character length and limitations: 255 single-byte alphanumeric characters.)
        """
        def set_EmailSubject(self, value):
            InputSet._set_input(self, 'EmailSubject', value)

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
        Set the value of the PaymentAmount input for this choreography. ((required, decimal) The amount to be paid.)
        """
        def set_PaymentAmount(self, value):
            InputSet._set_input(self, 'PaymentAmount', value)

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
A ResultSet with methods tailored to the values returned by the MakeIndividualPayment choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class MakeIndividualPaymentResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((string) The full response from PayPal formatted in name/value pairs.)
        """
        def get_Response(self):
            return self._output.get('Response', None)
        """
        Retrieve the value for the "Acknowledged" output from this choreography execution. ((string) Indicates the status of the request. Should contain "Sucess" or "Failure".)
        """
        def get_Acknowledged(self):
            return self._output.get('Acknowledged', None)
        """
        Retrieve the value for the "CorrelationId" output from this choreography execution. ((string) A unique id returned by PayPal for this payment.)
        """
        def get_CorrelationId(self):
            return self._output.get('CorrelationId', None)
        """
        Retrieve the value for the "ErrorMessage" output from this choreography execution. ((string) This will contain any error message returned by PayPal during this operation.)
        """
        def get_ErrorMessage(self):
            return self._output.get('ErrorMessage', None)
        """
        Retrieve the value for the "Timestamp" output from this choreography execution. ((date) The timestamp associated with the payment request.)
        """
        def get_Timestamp(self):
            return self._output.get('Timestamp', None)

class MakeIndividualPaymentChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return MakeIndividualPaymentResultSet(response, path)
