
###############################################################################
#
# RefundTransaction
# Issue a refund to a PayPal buyer by specifying a transaction ID.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class RefundTransaction(Choreography):

    """
    Create a new instance of the RefundTransaction Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/PayPal/RefundTransaction')


    def new_input_set(self):
        return RefundTransactionInputSet()

    def _make_result_set(self, result, path):
        return RefundTransactionResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RefundTransactionChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the RefundTransaction
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class RefundTransactionInputSet(InputSet):
        """
        Set the value of the Amount input for this choreography. ((optional, decimal) Refund amount. Amount is required if RefundType is set to Partial. If RefundType is set to Full, leave input blank.)
        """
        def set_Amount(self, value):
            InputSet._set_input(self, 'Amount', value)

        """
        Set the value of the CurrencyCode input for this choreography. ((optional, string) A three-character currency code (i.e. USD). Required for partial refunds. Leave this field blank for full refunds. Defaults to USD.)
        """
        def set_CurrencyCode(self, value):
            InputSet._set_input(self, 'CurrencyCode', value)

        """
        Set the value of the Endpoint input for this choreography. ((optional, string) Set to api-3t.paypal.com when running in production. Defaults to api-3t.sandbox.paypal.com for sandbox testing.)
        """
        def set_Endpoint(self, value):
            InputSet._set_input(self, 'Endpoint', value)

        """
        Set the value of the InvoiceID input for this choreography. ((optional, string) Your own invoice or tracking number. Character length limitation is 127 alphanumeric characters.)
        """
        def set_InvoiceID(self, value):
            InputSet._set_input(self, 'InvoiceID', value)

        """
        Set the value of the Note input for this choreography. ((optional, string) Custom note about the refund. Character length limitation is 255 alphanumeric characters.)
        """
        def set_Note(self, value):
            InputSet._set_input(self, 'Note', value)

        """
        Set the value of the Password input for this choreography. ((required, string) The API Password provided by PayPal.)
        """
        def set_Password(self, value):
            InputSet._set_input(self, 'Password', value)

        """
        Set the value of the RefundType input for this choreography. ((required, string) The refund type must be set to Full or Partial.  This flag effects what values some other input variables should have. Defaults to Full.)
        """
        def set_RefundType(self, value):
            InputSet._set_input(self, 'RefundType', value)

        """
        Set the value of the Signature input for this choreography. ((required, string) The API Signature provided by PayPal.)
        """
        def set_Signature(self, value):
            InputSet._set_input(self, 'Signature', value)

        """
        Set the value of the TransactionID input for this choreography. ((required, string) The ID for the transaction you want to retrieve data for.)
        """
        def set_TransactionID(self, value):
            InputSet._set_input(self, 'TransactionID', value)

        """
        Set the value of the User input for this choreography. ((required, string) The API Username provided by PayPal.)
        """
        def set_User(self, value):
            InputSet._set_input(self, 'User', value)


"""
A ResultSet with methods tailored to the values returned by the RefundTransaction choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class RefundTransactionResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((string) Response from PayPal formatted in name/value pairs.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class RefundTransactionChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return RefundTransactionResultSet(response, path)
