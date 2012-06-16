
###############################################################################
#
# ProcessDirectPayment
# Enables you to process a credit card payment.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class ProcessDirectPayment(Choreography):

    """
    Create a new instance of the ProcessDirectPayment Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/PayPal/ProcessDirectPayment')


    def new_input_set(self):
        return ProcessDirectPaymentInputSet()

    def _make_result_set(self, result, path):
        return ProcessDirectPaymentResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ProcessDirectPaymentChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the ProcessDirectPayment
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class ProcessDirectPaymentInputSet(InputSet):
        """
        Set the value of the Amount input for this choreography. ((required, decimal) The total cost of the transaction to the buyer.)
        """
        def set_Amount(self, value):
            InputSet._set_input(self, 'Amount', value)

        """
        Set the value of the CardSecurityCode input for this choreography. ((required, integer) The card Verification value found on the back of the user's credit card. For Visa, MasterCard, and Discover, the value is exactly 3 digits. For American Express, the value is exactly 4 digits.)
        """
        def set_CardSecurityCode(self, value):
            InputSet._set_input(self, 'CardSecurityCode', value)

        """
        Set the value of the City input for this choreography. ((required, string) The buyer's city.)
        """
        def set_City(self, value):
            InputSet._set_input(self, 'City', value)

        """
        Set the value of the CountryCode input for this choreography. ((required, string) The country code associated with the buyer's address.)
        """
        def set_CountryCode(self, value):
            InputSet._set_input(self, 'CountryCode', value)

        """
        Set the value of the CreditCardNumber input for this choreography. ((required, integer) The credit card number used in this payment.)
        """
        def set_CreditCardNumber(self, value):
            InputSet._set_input(self, 'CreditCardNumber', value)

        """
        Set the value of the CreditCardType input for this choreography. ((required, string) The type of credit card being used for this payment.)
        """
        def set_CreditCardType(self, value):
            InputSet._set_input(self, 'CreditCardType', value)

        """
        Set the value of the Email input for this choreography. ((optional, string) The email address of buyer.)
        """
        def set_Email(self, value):
            InputSet._set_input(self, 'Email', value)

        """
        Set the value of the Endpoint input for this choreography. ((optional, string) Set to api-3t.paypal.com when running in production. Defaults to api-3t.sandbox.paypal.com for sandbox testing.)
        """
        def set_Endpoint(self, value):
            InputSet._set_input(self, 'Endpoint', value)

        """
        Set the value of the ExpirationDate input for this choreography. ((required, date) The credit card expiration date. Include leading zero in month if it exists. Formatted like MMYYYY.)
        """
        def set_ExpirationDate(self, value):
            InputSet._set_input(self, 'ExpirationDate', value)

        """
        Set the value of the FirstName input for this choreography. ((required, string) The buyer's first name.)
        """
        def set_FirstName(self, value):
            InputSet._set_input(self, 'FirstName', value)

        """
        Set the value of the IPAddress input for this choreography. ((required, string) The IP address of the buyer's browser.)
        """
        def set_IPAddress(self, value):
            InputSet._set_input(self, 'IPAddress', value)

        """
        Set the value of the LastName input for this choreography. ((required, string) The buyer's last name.)
        """
        def set_LastName(self, value):
            InputSet._set_input(self, 'LastName', value)

        """
        Set the value of the Password input for this choreography. ((required, string) The API Password provided by PayPal.)
        """
        def set_Password(self, value):
            InputSet._set_input(self, 'Password', value)

        """
        Set the value of the PaymentAction input for this choreography. ((optional, string) Indicates how you want to obtain payment. Accepted values are "Authorization" or "Sale". Defaults to "Sale".)
        """
        def set_PaymentAction(self, value):
            InputSet._set_input(self, 'PaymentAction', value)

        """
        Set the value of the PhoneNumber input for this choreography. ((optional, string) The buyer's phone number.)
        """
        def set_PhoneNumber(self, value):
            InputSet._set_input(self, 'PhoneNumber', value)

        """
        Set the value of the ReturnFMFDetails input for this choreography. ((optional, boolean) Flag  to indicate whether you want the results returned by Fraud Management Fitlers. Defaults to 0.)
        """
        def set_ReturnFMFDetails(self, value):
            InputSet._set_input(self, 'ReturnFMFDetails', value)

        """
        Set the value of the Signature input for this choreography. ((required, string) The API Signature provided by PayPal.)
        """
        def set_Signature(self, value):
            InputSet._set_input(self, 'Signature', value)

        """
        Set the value of the State input for this choreography. ((required, string) The buyer's state or province.)
        """
        def set_State(self, value):
            InputSet._set_input(self, 'State', value)

        """
        Set the value of the Street2 input for this choreography. ((optional, string) The second line of the buyer's address (if it exists).)
        """
        def set_Street2(self, value):
            InputSet._set_input(self, 'Street2', value)

        """
        Set the value of the Street input for this choreography. ((required, string) The buyer's street address (line 1 of address).)
        """
        def set_Street(self, value):
            InputSet._set_input(self, 'Street', value)

        """
        Set the value of the User input for this choreography. ((required, string) The API Username provided by PayPal.)
        """
        def set_User(self, value):
            InputSet._set_input(self, 'User', value)

        """
        Set the value of the Zip input for this choreography. ((required, string) The postal code associated with the buyer's address.)
        """
        def set_Zip(self, value):
            InputSet._set_input(self, 'Zip', value)


"""
A ResultSet with methods tailored to the values returned by the ProcessDirectPayment choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class ProcessDirectPaymentResultSet(ResultSet):
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

class ProcessDirectPaymentChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ProcessDirectPaymentResultSet(response, path)
