
###############################################################################
#
# RefundOrder
# Allows you to refund an order that's been submitted to your Google Checkout merchant account.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class RefundOrder(Choreography):

    """
    Create a new instance of the RefundOrder Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Google/Checkout/RefundOrder')


    def new_input_set(self):
        return RefundOrderInputSet()

    def _make_result_set(self, result, path):
        return RefundOrderResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RefundOrderChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the RefundOrder
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class RefundOrderInputSet(InputSet):
        """
        Set the value of the Amount input for this choreography. ((decimal) The amount to refund)
        """
        def set_Amount(self, value):
            InputSet._set_input(self, 'Amount', value)

        """
        Set the value of the Comment input for this choreography. ((string) The comment for the order refund)
        """
        def set_Comment(self, value):
            InputSet._set_input(self, 'Comment', value)

        """
        Set the value of the Endpoint input for this choreography. ((optional, string) Set to checkout.google.com when running in production. Defaults to sandbox.google.com for sandbox testing.)
        """
        def set_Endpoint(self, value):
            InputSet._set_input(self, 'Endpoint', value)

        """
        Set the value of the MerchantId input for this choreography. ((integer) The Merchant Id provided by Google)
        """
        def set_MerchantId(self, value):
            InputSet._set_input(self, 'MerchantId', value)

        """
        Set the value of the MerchantKey input for this choreography. ((string) The Merchant Key provided by Google)
        """
        def set_MerchantKey(self, value):
            InputSet._set_input(self, 'MerchantKey', value)

        """
        Set the value of the OrderNumber input for this choreography. ((integer) The unique identifier for the order (There is an order number column in your Google Checkout Inbox).)
        """
        def set_OrderNumber(self, value):
            InputSet._set_input(self, 'OrderNumber', value)

        """
        Set the value of the Reason input for this choreography. ((string) The reason for the refund)
        """
        def set_Reason(self, value):
            InputSet._set_input(self, 'Reason', value)

        """
        Set the value of the SandboxMode input for this choreography. ((optional, boolean) Set this flag to 1 when using this Choreo with the Google Checkout sandbox endpoint (i.e. sandbox.google.com). Defaults to 0.)
        """
        def set_SandboxMode(self, value):
            InputSet._set_input(self, 'SandboxMode', value)


"""
A ResultSet with methods tailored to the values returned by the RefundOrder choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class RefundOrderResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((XML) The response from Google)
        """
        def get_Response(self):
            return self._output.get('Response', None)
        """
        Retrieve the value for the "ExecutionStatus" output from this choreography execution. (Contains status information on the Choreo execution)
        """
        def get_ExecutionStatus(self):
            return self._output.get('ExecutionStatus', None)

class RefundOrderChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return RefundOrderResultSet(response, path)
