
###############################################################################
#
# ListAllFulfillmentOrders
# Returns a list of fulfillment orders fulfilled after (or at) a specified date or by fulfillment method.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class ListAllFulfillmentOrders(Choreography):

    """
    Create a new instance of the ListAllFulfillmentOrders Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Amazon/Marketplace/OutboundShipments/ListAllFulfillmentOrders')


    def new_input_set(self):
        return ListAllFulfillmentOrdersInputSet()

    def _make_result_set(self, result, path):
        return ListAllFulfillmentOrdersResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListAllFulfillmentOrdersChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the ListAllFulfillmentOrders
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class ListAllFulfillmentOrdersInputSet(InputSet):
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
        Set the value of the Endpoint input for this choreography. ((optional, string) The base URL for the MWS endpoint. Defaults to mws.amazonservices.co.uk.)
        """
        def set_Endpoint(self, value):
            InputSet._set_input(self, 'Endpoint', value)

        """
        Set the value of the FulfillmentMethod input for this choreography. ((optional, string) A value used for selecting fulfillment orders based on their fulfillment method. "Consumer" indicates a customer order, and "Removal" indicates that the inventory should be returned to the specified.)
        """
        def set_FulfillmentMethod(self, value):
            InputSet._set_input(self, 'FulfillmentMethod', value)

        """
        Set the value of the QueryStartDateTime input for this choreography. ((optional, date) A date used for selecting items that have had changes in inventory availability after (or at) a specified time, in ISO 8601 date format (i.e. 2012-01-01).)
        """
        def set_QueryStartDateTime(self, value):
            InputSet._set_input(self, 'QueryStartDateTime', value)


"""
A ResultSet with methods tailored to the values returned by the ListAllFulfillmentOrders choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class ListAllFulfillmentOrdersResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) Stores the response from Amazon.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class ListAllFulfillmentOrdersChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ListAllFulfillmentOrdersResultSet(response, path)
