
###############################################################################
#
# ListInventorySupplyBySKU
# Returns information about the availability of a seller's inventory using a given SellerSKU.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class ListInventorySupplyBySKU(Choreography):

    """
    Create a new instance of the ListInventorySupplyBySKU Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Amazon/Marketplace/Inventory/ListInventorySupplyBySKU')


    def new_input_set(self):
        return ListInventorySupplyBySKUInputSet()

    def _make_result_set(self, result, path):
        return ListInventorySupplyBySKUResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListInventorySupplyBySKUChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the ListInventorySupplyBySKU
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class ListInventorySupplyBySKUInputSet(InputSet):
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
        Set the value of the ResponseGroup input for this choreography. ((optional, string) Indicates whether or not to return the SupplyDetail element in the response. Valid values are: "Basic" (does not include SupplyDetail), and "Detailed" (includes SupplyDetail). Defaults to "Basic".)
        """
        def set_ResponseGroup(self, value):
            InputSet._set_input(self, 'ResponseGroup', value)

        """
        Set the value of the SellerSKU input for this choreography. ((required, string) A seller SKU for an item that you want inventory availability information about.)
        """
        def set_SellerSKU(self, value):
            InputSet._set_input(self, 'SellerSKU', value)


"""
A ResultSet with methods tailored to the values returned by the ListInventorySupplyBySKU choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class ListInventorySupplyBySKUResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) Stores the response from Amazon.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class ListInventorySupplyBySKUChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ListInventorySupplyBySKUResultSet(response, path)
