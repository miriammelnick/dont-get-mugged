
###############################################################################
#
# ChargeAndShipOrder
# Charge and ship an order once a shopping cart order has arrived in your Google Checkout Inbox.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class ChargeAndShipOrder(Choreography):

    """
    Create a new instance of the ChargeAndShipOrder Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Google/Checkout/ChargeAndShipOrder')


    def new_input_set(self):
        return ChargeAndShipOrderInputSet()

    def _make_result_set(self, result, path):
        return ChargeAndShipOrderResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ChargeAndShipOrderChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the ChargeAndShipOrder
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class ChargeAndShipOrderInputSet(InputSet):
        """
        Set the value of the Amount input for this choreography. ((decimal) The dollar amount to charge (i.e. 25.50))
        """
        def set_Amount(self, value):
            InputSet._set_input(self, 'Amount', value)

        """
        Set the value of the Carrier input for this choreography. ((string) The desired postal carrier (i.e. UPS))
        """
        def set_Carrier(self, value):
            InputSet._set_input(self, 'Carrier', value)

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
        Set the value of the TrackingNumber input for this choreography. ((string) The tracking number for the order package)
        """
        def set_TrackingNumber(self, value):
            InputSet._set_input(self, 'TrackingNumber', value)


"""
A ResultSet with methods tailored to the values returned by the ChargeAndShipOrder choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class ChargeAndShipOrderResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((XML) The response from Google)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class ChargeAndShipOrderChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ChargeAndShipOrderResultSet(response, path)
