
###############################################################################
#
# CancelOrder
# Cancels an order that's been submitted to a Google Checkout merchant account.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class CancelOrder(Choreography):

    """
    Create a new instance of the CancelOrder Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Google/Checkout/CancelOrder')


    def new_input_set(self):
        return CancelOrderInputSet()

    def _make_result_set(self, result, path):
        return CancelOrderResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CancelOrderChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the CancelOrder
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class CancelOrderInputSet(InputSet):
        """
        Set the value of the Comment input for this choreography. ((required, string) The comment for the order cancellation)
        """
        def set_Comment(self, value):
            InputSet._set_input(self, 'Comment', value)

        """
        Set the value of the Endpoint input for this choreography. ((optional, string) Set to checkout.google.com when running in production. Defaults to sandbox.google.com for sandbox testing.)
        """
        def set_Endpoint(self, value):
            InputSet._set_input(self, 'Endpoint', value)

        """
        Set the value of the MerchantId input for this choreography. ((required, integer) The Merchant Id provided by Google)
        """
        def set_MerchantId(self, value):
            InputSet._set_input(self, 'MerchantId', value)

        """
        Set the value of the MerchantKey input for this choreography. ((required, string) The Merchant Key provided by Google)
        """
        def set_MerchantKey(self, value):
            InputSet._set_input(self, 'MerchantKey', value)

        """
        Set the value of the OrderNumber input for this choreography. ((required, integer) The unique identifier for the order (There is an order number column in your Google Checkout Inbox).)
        """
        def set_OrderNumber(self, value):
            InputSet._set_input(self, 'OrderNumber', value)

        """
        Set the value of the Reason input for this choreography. ((required, string) The reason for the cancellation)
        """
        def set_Reason(self, value):
            InputSet._set_input(self, 'Reason', value)


"""
A ResultSet with methods tailored to the values returned by the CancelOrder choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class CancelOrderResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Google)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class CancelOrderChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CancelOrderResultSet(response, path)
