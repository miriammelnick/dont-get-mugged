
###############################################################################
#
# TransactionSearch
# Retrieves transaction history for transactions that meet a specified criteria.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class TransactionSearch(Choreography):

    """
    Create a new instance of the TransactionSearch Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/PayPal/TransactionSearch')


    def new_input_set(self):
        return TransactionSearchInputSet()

    def _make_result_set(self, result, path):
        return TransactionSearchResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return TransactionSearchChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the TransactionSearch
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class TransactionSearchInputSet(InputSet):
        """
        Set the value of the Account input for this choreography. ((optional, string) Search by credit card number.)
        """
        def set_Account(self, value):
            InputSet._set_input(self, 'Account', value)

        """
        Set the value of the AuctionItemNumber input for this choreography. ((optional, string) Search by auction item number of the purchased item.)
        """
        def set_AuctionItemNumber(self, value):
            InputSet._set_input(self, 'AuctionItemNumber', value)

        """
        Set the value of the CurrencyCode input for this choreography. ((optional, string) Search by currency code (i.e. USD).)
        """
        def set_CurrencyCode(self, value):
            InputSet._set_input(self, 'CurrencyCode', value)

        """
        Set the value of the Email input for this choreography. ((optional, string) Search by email.)
        """
        def set_Email(self, value):
            InputSet._set_input(self, 'Email', value)

        """
        Set the value of the EndDate input for this choreography. ((optional, date) The latest transaction date to return. Must be an epoch timestamp in milliseconds or formatted in UTC like: 2011-05-19T00:00:00Z.)
        """
        def set_EndDate(self, value):
            InputSet._set_input(self, 'EndDate', value)

        """
        Set the value of the Endpoint input for this choreography. ((optional, string) Set to api-3t.paypal.com when running in production. Defaults to api-3t.sandbox.paypal.com for sandbox testing.)
        """
        def set_Endpoint(self, value):
            InputSet._set_input(self, 'Endpoint', value)

        """
        Set the value of the InvoiceNumber input for this choreography. ((optional, string) Search by invoice number.)
        """
        def set_InvoiceNumber(self, value):
            InputSet._set_input(self, 'InvoiceNumber', value)

        """
        Set the value of the Password input for this choreography. ((required, string) The API Password provided by PayPal.)
        """
        def set_Password(self, value):
            InputSet._set_input(self, 'Password', value)

        """
        Set the value of the ReceiptId input for this choreography. ((optional, string) Search by the PayPal receipt ID.)
        """
        def set_ReceiptId(self, value):
            InputSet._set_input(self, 'ReceiptId', value)

        """
        Set the value of the Receiver input for this choreography. ((optional, string) Search by the email address of the receiver.)
        """
        def set_Receiver(self, value):
            InputSet._set_input(self, 'Receiver', value)

        """
        Set the value of the Signature input for this choreography. ((required, string) The API Signature provided by PayPal.)
        """
        def set_Signature(self, value):
            InputSet._set_input(self, 'Signature', value)

        """
        Set the value of the StartDate input for this choreography. ((required, date) The earliest transaction date to return. Must be an epoch timestamp in milliseconds or formatted in UTC like: 2011-05-19T00:00:00Z.)
        """
        def set_StartDate(self, value):
            InputSet._set_input(self, 'StartDate', value)

        """
        Set the value of the TransactionAmount input for this choreography. ((optional, decimal) Search by transaction amount.)
        """
        def set_TransactionAmount(self, value):
            InputSet._set_input(self, 'TransactionAmount', value)

        """
        Set the value of the TransactionClass input for this choreography. ((optional, string) Search by classification of transaction (i.e. All, Sent, Recieved, etc).)
        """
        def set_TransactionClass(self, value):
            InputSet._set_input(self, 'TransactionClass', value)

        """
        Set the value of the TransactionId input for this choreography. ((optional, string) Search by the transaction ID)
        """
        def set_TransactionId(self, value):
            InputSet._set_input(self, 'TransactionId', value)

        """
        Set the value of the TransactionStatus input for this choreography. ((optional, string) Search by transaction status (i.e. Pending, Processing, Success, Denied, Reversed).)
        """
        def set_TransactionStatus(self, value):
            InputSet._set_input(self, 'TransactionStatus', value)

        """
        Set the value of the User input for this choreography. ((required, string) The API Username provided by PayPal.)
        """
        def set_User(self, value):
            InputSet._set_input(self, 'User', value)


"""
A ResultSet with methods tailored to the values returned by the TransactionSearch choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class TransactionSearchResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((string) Response from PayPal formatted in name/value pairs.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class TransactionSearchChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return TransactionSearchResultSet(response, path)
