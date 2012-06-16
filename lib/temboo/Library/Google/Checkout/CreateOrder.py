
###############################################################################
#
# CreateOrder
# Populates a shopping cart and sends order information to your merchant  account allowing a user to complete an order using Google Checkout.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class CreateOrder(Choreography):

    """
    Create a new instance of the CreateOrder Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Google/Checkout/CreateOrder')


    def new_input_set(self):
        return CreateOrderInputSet()

    def _make_result_set(self, result, path):
        return CreateOrderResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateOrderChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the CreateOrder
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class CreateOrderInputSet(InputSet):
        """
        Set the value of the Endpoint input for this choreography. ((optional, string) Set to checkout.google.com when running in production. Defaults to sandbox.google.com for sandbox testing.)
        """
        def set_Endpoint(self, value):
            InputSet._set_input(self, 'Endpoint', value)

        """
        Set the value of the ItemDescription input for this choreography. ((string) The description of the shopping cart item)
        """
        def set_ItemDescription(self, value):
            InputSet._set_input(self, 'ItemDescription', value)

        """
        Set the value of the ItemName input for this choreography. ((string) A name of the shopping cart item)
        """
        def set_ItemName(self, value):
            InputSet._set_input(self, 'ItemName', value)

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
        Set the value of the Quanity input for this choreography. ((integer) The quantity of the shopping cart item)
        """
        def set_Quanity(self, value):
            InputSet._set_input(self, 'Quanity', value)

        """
        Set the value of the ShippingMethod input for this choreography. ((string) The shipping method for the order (i.e. SuperShip Ground))
        """
        def set_ShippingMethod(self, value):
            InputSet._set_input(self, 'ShippingMethod', value)

        """
        Set the value of the ShippingPrice input for this choreography. ((decimal) The shipping price for the order)
        """
        def set_ShippingPrice(self, value):
            InputSet._set_input(self, 'ShippingPrice', value)

        """
        Set the value of the UnitPrice input for this choreography. ((decimal) The unit price of the item that is added to the shopping cart)
        """
        def set_UnitPrice(self, value):
            InputSet._set_input(self, 'UnitPrice', value)


"""
A ResultSet with methods tailored to the values returned by the CreateOrder choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class CreateOrderResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((XML) The response from Google.  Contains the redirect URL that a customer will use to complete the order.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class CreateOrderChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CreateOrderResultSet(response, path)
