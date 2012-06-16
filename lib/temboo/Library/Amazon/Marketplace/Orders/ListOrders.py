
###############################################################################
#
# ListOrders
# Returns orders created during a time frame that you specify.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class ListOrders(Choreography):

    """
    Create a new instance of the ListOrders Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Amazon/Marketplace/Orders/ListOrders')


    def new_input_set(self):
        return ListOrdersInputSet()

    def _make_result_set(self, result, path):
        return ListOrdersResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListOrdersChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the ListOrders
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class ListOrdersInputSet(InputSet):
        """
        Set the value of the AWSAccessKeyId input for this choreography. ((required, string) The Access Key ID provided by Amazon Web Services.)
        """
        def set_AWSAccessKeyId(self, value):
            InputSet._set_input(self, 'AWSAccessKeyId', value)

        """
        Set the value of the AWSMarketplaceId input for this choreography. ((required, string) The Marketplace ID provided by Amazon Web Services.)
        """
        def set_AWSMarketplaceId(self, value):
            InputSet._set_input(self, 'AWSMarketplaceId', value)

        """
        Set the value of the AWSMerchantId input for this choreography. ((required, string) The Merchant ID provided by Amazon Web Services.)
        """
        def set_AWSMerchantId(self, value):
            InputSet._set_input(self, 'AWSMerchantId', value)

        """
        Set the value of the AWSSecretKeyId input for this choreography. ((required, string) The Secret Key ID provided by Amazon Web Services.)
        """
        def set_AWSSecretKeyId(self, value):
            InputSet._set_input(self, 'AWSSecretKeyId', value)

        """
        Set the value of the CreatedAfter input for this choreography. ((optional, date) A date used for selecting orders created after (or at) a specified time, in ISO 8601 date format (i.e. 2012-01-01). Defaults to today's date if not provided.)
        """
        def set_CreatedAfter(self, value):
            InputSet._set_input(self, 'CreatedAfter', value)

        """
        Set the value of the CreatedBefore input for this choreography. ((optional, date) A date used for selecting orders created before (or at) a specified time, in ISO 8601 date format (i.e. 2012-01-01).)
        """
        def set_CreatedBefore(self, value):
            InputSet._set_input(self, 'CreatedBefore', value)

        """
        Set the value of the Endpoint input for this choreography. ((optional, string) The base URL for the MWS endpoint. Defaults to mws.amazonservices.co.uk.)
        """
        def set_Endpoint(self, value):
            InputSet._set_input(self, 'Endpoint', value)

        """
        Set the value of the FullfillmentChannel input for this choreography. ((optional, string) A string indicating how an order was fulfilled. Use "AFN" for Amazon fulfilled orders, and "MFN" for seller fulfilled orders.)
        """
        def set_FullfillmentChannel(self, value):
            InputSet._set_input(self, 'FullfillmentChannel', value)

        """
        Set the value of the MaxResultsPerPage input for this choreography. ((optional, integer) A number that indicates the maximum number of orders that can be returned per page. Valid values are: 1-100.)
        """
        def set_MaxResultsPerPage(self, value):
            InputSet._set_input(self, 'MaxResultsPerPage', value)

        """
        Set the value of the OrderStatus input for this choreography. ((optional, string) An OrderStatus value to select only orders with a certain status. Valid values are: Pending, Unshipped, PartiallyShipped, Shipped, Canceled, Unfulfillable.)
        """
        def set_OrderStatus(self, value):
            InputSet._set_input(self, 'OrderStatus', value)

        """
        Set the value of the PaymentMethod input for this choreography. ((optional, string) Used to select only orders of a certain payment type. Valid values are: COD (cash on delivery), CSV (convenience store payment), or Other (Any payment method other than COD or CVS).)
        """
        def set_PaymentMethod(self, value):
            InputSet._set_input(self, 'PaymentMethod', value)


"""
A ResultSet with methods tailored to the values returned by the ListOrders choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class ListOrdersResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) Stores the response from Amazon.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class ListOrdersChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ListOrdersResultSet(response, path)
